from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from students.models import Student

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
