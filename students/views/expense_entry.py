# students/views.py
from django.shortcuts import render, redirect
from students.forms import ExpenseForm

def expense_entry_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_entry')
    else:
        form = ExpenseForm()
    return render(request, 'students/expense_entry.html', {'form': form})
