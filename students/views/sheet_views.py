from django.shortcuts import render, redirect, get_object_or_404
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from django.conf import settings
from students.models import Student
import os

SERVICE_ACCOUNT_FILE = os.path.join(settings.BASE_DIR, 'collegemanagement-427410-71b9655c0e80.json')
SPREADSHEET_ID = '1c73XKHU1MwJTShx5rdMnkCBYdjxYFriWhBbYEZN4dLg'
RANGE_NAME = 'Sheet1!A1:Z'

def get_google_sheet_data():
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
    )

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])

    return values

def requests_view(request):
    sheet_data = get_google_sheet_data()
    context = {'update_requests': sheet_data}
    return render(request, 'students/requests.html', context)

def update_request(request, student_id):
    if request.GET.get('confirm') == 'yes':
        sheet_data = get_google_sheet_data()
        for row in sheet_data:
            if row[0] == student_id:
                new_phone_number = row[1]
                break
        student = get_object_or_404(Student, student_id=student_id)
        student.student_mobile_number = new_phone_number
        student.save()
    return redirect('requests')
