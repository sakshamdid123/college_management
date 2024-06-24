from django.db import models

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

class TallyResponse(models.Model):
    question = models.CharField(max_length=200)
    response = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question} - {self.response}"
