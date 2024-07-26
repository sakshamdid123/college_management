from django import forms
from .models import Expense

class StudentSearchForm(forms.Form):
    student_id = forms.CharField(max_length=10)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = [
            'unique_expense_id',
            'sc_name',
            'sc_email',
            'date',
            'company_name',
            'company_round',
            'bill_number',
            'bill_vendor',
            'bill_amount'
        ]