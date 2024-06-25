from django.contrib import admin
from django.urls import path
from students.views import student_views, contact_views, sheet_views  # Import views from the students folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_views.student_list, name='student_list'),
    path('students/student_detail/', student_views.student_detail, name='student_detail'),
    path('students/update_contact/', contact_views.update_contact, name='update_contact'),
    path('students/search_suggestions/', student_views.search_suggestions, name='search_suggestions'),
    path('requests/', sheet_views.requests_view, name='requests'),
    path('update_request/<str:student_id>/', sheet_views.update_request, name='update_request'),
]

