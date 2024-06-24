from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, requesting
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import csv
from django.core.files.storage import default_storage
from io import StringIO
from django.template.loader import render_to_string
from django.urls import reverse
import tempfile
import os
import logging

logger = logging.getLogger(__name__)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request):
    student_id = request.GET.get('student_id')
    try:
        student = Student.objects.get(student_id=student_id)
    except Student.DoesNotExist:
        student = None
    return render(request, 'students/student_detail.html', {'student': student})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.student_name = request.POST.get('student_name')
        student.college_email = request.POST.get('college_email')
        student.save()
        return redirect('student_list')
    return render(request, 'students/update_student.html', {'student': student})

def search_suggestions(request):
    query = request.GET.get('q', '')
    if query:
        suggestions = Student.objects.filter(student_id__icontains=query)[:3]
        students = Student.objects.filter(student_id__icontains=query)
    else:
        suggestions = []
        students = Student.objects.all()
    
    suggestions_data = [{'student_id': student.student_id, 'student_name': student.student_name} for student in suggestions]
    
    html = render_to_string('students/student_list_items.html', {'students': students})
    
    return JsonResponse({'suggestions': suggestions_data, 'html': html})

@csrf_exempt
def update_contact(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        new_phone = request.POST.get('new_phone')
        new_email = request.POST.get('new_email')
        
        student = get_object_or_404(Student, pk=student_id)
        
        if new_phone:
            student.student_mobile_number = new_phone
        if new_email:
            student.personal_email = new_email
        
        student.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student_id = data.get('student_id')
            new_phone_number = data.get('new_phone_number')
            
            if not student_id or not new_phone_number:
                logger.error('Missing student_id or new_phone_number in the request data')
                return JsonResponse({'status': 'failed', 'reason': 'missing_data'}, status=400)
            
            requesting.objects.create(student_id=student_id, new_phone_number=new_phone_number)
            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError:
            logger.error('Invalid JSON received')
            return JsonResponse({'status': 'failed', 'reason': 'invalid_json'}, status=400)
    return JsonResponse({'status': 'failed'}, status=400)
def requests(request):
    update_requests = requesting.objects.filter(confirmed=False)
    return render(request, 'students/requests.html', {'update_requests': update_requests})

def update_request(request, request_id):
    update_request = get_object_or_404(requesting, id=request_id)
    if request.GET.get('confirm') == 'yes':
        student = get_object_or_404(Student, student_id=update_request.student_id)
        student.student_mobile_number = update_request.new_phone_number
        student.save()
        update_request.confirmed = True
        update_request.save()
    else:
        update_request.delete()
    return redirect('requests')


