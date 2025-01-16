from django import forms
from .models import Attendance
from .models import Student

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']

class BulkAttendanceForm(forms.Form):
    student = forms.ModelChoiceField(queryset= Student.objects.all())
    dates = forms.CharField(widget=forms.Textarea, help_text="Enter dates separated by commas (YYYY-MM-DD)")
    status = forms.ChoiceField(choices=[('Present', 'Present'), ('Absent', 'Absent')])