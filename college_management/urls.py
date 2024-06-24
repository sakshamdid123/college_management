from django.contrib import admin
from django.urls import path
from students import views  # Import views from the students folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list, name='student_list'),
    path('student_detail/', views.student_detail, name='student_detail'),
    path('update/<str:pk>/', views.update_student, name='update_student'),
    path('students/update_contact/', views.update_contact, name='update_contact'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
]

