from django.contrib import admin
from .models import Student, Mark, Attendance

admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(Attendance)