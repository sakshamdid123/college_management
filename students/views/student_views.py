from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from students.models import Student

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