from django.contrib import admin
from django.urls import path
from students.views.CVVettingPortalView import CVVettingPortalView,SCLoginView, FNSAdminPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cv-vetting-portal/', CVVettingPortalView.as_view(), name='cv_vetting_portal'),
    path('sc-login/', SCLoginView.as_view(), name='sc_login'),  # Add this line
    path('fns-admin/', FNSAdminPageView, name='fns-admin-page'),
]

