from django import forms
from .models import Attendance, Mark, Student, Assignment, Announcement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }       

class MarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = '__all__'

class TeacherSignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = ""
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date']

        widgets = {
            'due_date': forms.TextInput(
                attrs={
                    'placeholder': 'YYYY-MM-DD'
                }
            )
        }

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

class StudentSignupForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'username',
            'password1',
            'password2'
        ]