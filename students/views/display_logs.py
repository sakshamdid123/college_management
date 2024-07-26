# display_logs.py

from django.shortcuts import render, get_object_or_404
from django.views import View
from students.models import StudentData, VettingLog

class StudentLogView(View):
    def get(self, request, roll_number):
        roll_number = get_object_or_404(StudentData, roll_number=roll_number)
        logs = VettingLog.objects.filter(roll_number=roll_number).order_by('-timestamp')
        return render(request, 'students/student_logs.html', {'roll_number': roll_number, 'logs': logs})
