from django.shortcuts import render, redirect
from .models import Student, Attendance
from .forms import AttendanceForm
from .forms import BulkAttendanceForm

def student_list(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = AttendanceForm()
    return render(request, 'student_list.html', {'students': students, 'form': form})

# def attendance_report(request):
#     students = Student.objects.all()
#     attendance_records = Attendance.objects.all()
#     return render(request, 'attendance_report.html', {'students': students, 'attendance_records': attendance_records})

from django.db.models import Count, Q
def attendance_report(request):
    students = Student.objects.annotate(
        present_days=Count('attendance', filter=Q(attendance__status='Present')),
        absent_days=Count('attendance', filter=Q(attendance__status='Absent'))
    )
    return render(request, 'attendance_report.html', {'students': students})

def bulk_attendance(request):
    if request.method == 'POST':
        form = BulkAttendanceForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            dates = form.cleaned_data['dates'].split(',')
            status = form.cleaned_data['status']
            for date in dates:
                Attendance.objects.create(student=student, date=date.strip(), status=status)
            return redirect('attendance_report')
    else:
        form = BulkAttendanceForm()
    return render(request, 'bulk_attendance.html', {'form': form})


