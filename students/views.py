from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import csv
from django.core.files.storage import default_storage
from io import StringIO
from django.template.loader import render_to_string
from django.urls import reverse
import tempfile
import os

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