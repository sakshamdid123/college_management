from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from students.models import StudentData, VettingSlot, SCLoginCredentials
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
import os

class SCLoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            sc_user = SCLoginCredentials.objects.get(username=username, password=password)
            request.session['sc_name'] = sc_user.sc_name
            return redirect('cv_vetting_portal')
        except SCLoginCredentials.DoesNotExist:
            return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})

class CVVettingPortalView(View):
    def get(self, request):
        if 'sc_name' not in request.session:
            return redirect('sc_login')

        sc_name = request.session['sc_name']
        current_date_str = request.GET.get('date', datetime.now().strftime('%Y-%m-%d'))
        current_date = datetime.strptime(current_date_str, '%Y-%m-%d').date()
        current_datetime = datetime.now()

        # Update NULL vetting_status values to 'Pending'
        VettingSlot.objects.filter(vetting_status__isnull=True).update(vetting_status='Pending')
        VettingSlot.objects.filter(revetting_status__isnull=True).update(revetting_status='No')

        student_data = StudentData.objects.all()
        vetting_slots = VettingSlot.objects.filter(date=current_date, sc_name=sc_name)

        data = [
            {
                'roll_number': sd.roll_number,
                'name': sd.name,
                'cv': sd.cv,
                'phone_number': sd.phone_number,
                'email_address': sd.email_address,
                'date': vs.date,
                'vetting_status': vs.vetting_status,
                'revetting_status': vs.revetting_status,
                'discrepancy_slot_date': vs.discrepancy_slot_date,
                'discrepancy_slot_time': vs.discrepancy_slot_time,
                'is_due': (datetime.combine(vs.discrepancy_slot_date, vs.discrepancy_slot_time) <= current_datetime if vs.discrepancy_slot_date and vs.discrepancy_slot_time else False),
            }
            for sd in student_data
            for vs in vetting_slots
            if sd.roll_number == vs.roll_number.roll_number
        ]


        # Pass current_date as a string
        return render(request, 'students/cv_vetting_portal.html', {'data': data, 'current_date': current_date_str})

    def post(self, request):
        roll_number = request.POST.get('roll_number')
        vetting_status = request.POST.get('vetting_status')
        discrepancy_slot_date = request.POST.get('discrepancy_slot_date')
        discrepancy_slot_time = request.POST.get('discrepancy_slot_time')

        update_data = {'vetting_status': vetting_status}

        if discrepancy_slot_date:
            update_data['discrepancy_slot_date'] = discrepancy_slot_date
        if discrepancy_slot_time:
            update_data['discrepancy_slot_time'] = discrepancy_slot_time

        VettingSlot.objects.filter(roll_number__roll_number=roll_number).update(**update_data)
        
        return JsonResponse({'success': True})