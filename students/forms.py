from django import forms

class StudentSearchForm(forms.Form):
    student_id = forms.CharField(max_length=10)
