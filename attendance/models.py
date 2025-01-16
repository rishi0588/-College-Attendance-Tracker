from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    division = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=7, choices=[('Present', 'Present'), ('Absent', 'Absent')])


    def __str__(self):
        return f"{self.student.name} - {self.date}: {self.status}"
