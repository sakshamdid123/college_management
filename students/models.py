from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from datetime import datetime, timedelta


class Student(models.Model):
    student_id = models.TextField(db_column='Student ID', primary_key=True)
    student_name = models.TextField(db_column='Student Name', blank=True, null=True)
    course = models.TextField(db_column='Course', blank=True, null=True)
    year_sem = models.IntegerField(db_column='Year/Sem', blank=True, null=True)
    category = models.TextField(db_column='Category', blank=True, null=True)
    gender = models.TextField(db_column='Gender', blank=True, null=True)
    college_email = models.TextField(db_column='College Email', blank=True, null=True)
    personal_email = models.TextField(db_column='Personal Email', blank=True, null=True)
    student_mobile_number = models.BigIntegerField(db_column='Student Mobile Number', blank=True, null=True)
    admission_criterion = models.TextField(db_column='Admission Criterion', blank=True, null=True)
    cuet_score = models.FloatField(db_column='CUET Score', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '2026_bcom'

    def __str__(self):
        return self.student_name

class Expense(models.Model):
    unique_expense_id = models.CharField(max_length=255)
    sc_name = models.CharField(max_length=255)
    sc_email = models.EmailField()
    date = models.DateField()
    company_name = models.CharField(max_length=255)
    company_round = models.CharField(max_length=255)
    bill_number = models.CharField(max_length=255)
    bill_vendor = models.CharField(max_length=255)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.sc_name} - {self.bill_amount}"

class StudentData(models.Model):
    roll_number = models.CharField(max_length=10, primary_key=True, db_column='Roll Number')
    name = models.CharField(max_length=100, db_column='Name')
    phone_number = models.CharField(max_length=10, db_column='Phone Number')
    email_address = models.CharField(max_length=100, db_column='Email Address')
    variant_a = models.TextField(db_column='Variant A')
    variant_b = models.TextField(db_column='Variant B')
    variant_c = models.TextField(db_column='Variant C')
    proofs = models.TextField(db_column='Proofs')
    repository = models.TextField(db_column='Repository')
    

    class Meta:
        db_table = 'student_data'
        app_label = 'vetting_2425'

    def __str__(self):
        return self.name

class VettingSlot(models.Model):
    DISCREPANCY = 'Discrepancy'
    CANCELLED = 'Cancelled'
    REVETTING = 'Revetting'
    VETTED = 'Vetted'
    RESCHEDULED = 'Rescheduled'
    PENDING = 'Pending'
    VETTING_STATUS_CHOICES = [
        (DISCREPANCY, 'Discrepancy'),
        (CANCELLED, 'Cancelled'),
        (REVETTING, 'Revetting'),
        (VETTED, 'Vetted'),
        (RESCHEDULED, 'Rescheduled'),
        (PENDING, 'Pending'),
    ]

    YES = 'Yes'
    NO = 'No'
    APPROVAL_STATUS_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]
    roll_number = models.ForeignKey(StudentData, on_delete=models.CASCADE, db_column='Roll Number', primary_key=True)
    date = models.DateField(db_column='Date')
    sc_name = models.CharField(max_length=100, db_column='SC Name')
    fns_buddy = models.CharField(max_length=100, db_column='FNS Buddy')
    vetting_status = models.CharField(
        max_length=20,
        choices=VETTING_STATUS_CHOICES,
        default=PENDING,
        db_column='Vetting Status',
    )
    revetting_status = models.CharField(
        max_length=20,
        choices=VETTING_STATUS_CHOICES,
        db_column='Revetting Status',
    )
    discrepancy_slot_date = models.DateField(db_column='Discrepancy Slot Date')
    discrepancy_slot_time = models.TimeField(db_column='Discrepancy Slot Time')
    link = models.TextField(db_column='Email Link')
    discrepancies = models.TextField(null=True, db_column='Discrepancies')

    class Meta:
        db_table = 'vetting_slots'
        app_label = 'vetting_2425'

    def __str__(self):
        return f"Vetting Slot for {self.roll_number} on {self.slot_date} at {self.slot_time}"

class SCLoginCredentials(models.Model):
    sc_name = models.CharField(max_length=100, db_column='SC Name', primary_key=True)
    email = models.CharField(max_length=100, db_column='Email')
    username = models.CharField(max_length=100, db_column='User Name', primary_key=True)
    password = models.CharField(max_length=100, db_column='Password', primary_key=True)

    class Meta:
        db_table = 'sc_login_credentials'
        app_label = 'vetting_2425'

    def __str__(self):
        return self.username

