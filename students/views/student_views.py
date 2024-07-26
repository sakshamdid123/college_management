import os
import csv
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from students.models import Student, Expense
from django.http import HttpResponse

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

def get_sheet_data():
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
    )

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    return values

def dashboard_data(request):
    # Query all expense data from the database
    expenses = Expense.objects.all().values(
        'unique_expense_id', 'sc_name', 'sc_email', 'date', 'company_name', 
        'company_round', 'bill_number', 'bill_vendor', 'bill_amount'
    )
    # Convert QuerySet to a list of dictionaries
    data = list(expenses)
    return JsonResponse(data, safe=False)

def dashboard_view(request):
    return render(request, 'students/dashboard.html')

def create_vcf_view(request):
    if request.method == 'POST':
        student_ids = request.POST['student_ids'].replace('\n', ',').replace(' ', ',').split(',')
        company_name = request.POST['company_name']
        students = Student.objects.filter(student_id__in=student_ids)
        
        response = HttpResponse(content_type='text/vcard')
        response['Content-Disposition'] = 'attachment; filename=students.vcf'
        
        vcard_entries = []
        for student in students:
            full_name = f"{student.student_name}_{student.student_id}_{company_name}"
            vcard_entries.append(
                "BEGIN:VCARD\n"
                "VERSION:3.0\n"
                f"FN:{full_name}\n"
                f"TEL;TYPE=CELL:{student.student_mobile_number}\n"
                "END:VCARD\n"
            )
        response.writelines(vcard_entries)
        return response
    return render(request, 'students/base.html')