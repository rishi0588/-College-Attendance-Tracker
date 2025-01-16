from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('report/', views.attendance_report, name='attendance_report'),
    path('bulk/', views.bulk_attendance, name='bulk_attendence')
]
