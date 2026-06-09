from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    roll_no = models.CharField(max_length=20)

    student_class = models.CharField(max_length=20)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Attendance(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20
    )

    class Meta:
        unique_together = (
            'student',
            'date'
        )

    def __str__(self):
        return f"{self.student.name} - {self.date}"
    
class Mark(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    computer = models.IntegerField()

    def __str__(self):
        return self.student.name
    
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class AcademicEvent(models.Model):

    title = models.CharField(
        max_length=100
    )

    event_date = models.DateField()

    description = models.TextField()

    def __str__(self):
        return self.title
    