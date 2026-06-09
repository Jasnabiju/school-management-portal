from django.shortcuts import render, redirect
from .forms import AttendanceForm, MarkForm, TeacherSignupForm, StudentForm, AssignmentForm, AnnouncementForm, StudentSignupForm
from .models import Attendance, Mark, Student, Assignment, Announcement, AcademicEvent
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count, Q
from django.http import HttpResponse

def is_student(user):

    return Student.objects.filter(
        user=user
    ).exists()


def is_teacher(user):

    return not Student.objects.filter(
        user=user
    ).exists()

def home(request):
    return render(request, 'index.html')

def teacher(request):
    return render(request, 'teacher.html')

def student(request):
    return render(request, 'student.html')

@login_required
def teacher_dashboard(request):

    return render(
        request,
        'teacherDashboard.html'
    )

@login_required
def student_dashboard(request):

    print("LOGGED USER =", request.user)

    if is_teacher(request.user):
        return HttpResponse("Access Denied")

    return render(
        request, 
        'studentDashboard.html'
    )

@login_required
def attendance(request):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    today = timezone.now().date()

    students = Student.objects.all()

    already_marked = Attendance.objects.filter(
        date=today
    ).exists()

    if request.method == "POST" and not already_marked:

        for student in students:

            status = request.POST.get(
                f"status_{student.id}"
            )

            Attendance.objects.create(
                student=student,
                date=today,
                status=status
            )

        return redirect('/attendance/')

    attendance_records = Attendance.objects.all().order_by(
        '-date'
    )

    return render(
        request,
        'attendance.html',
        {
            'students': students,
            'attendance_records': attendance_records,
            'already_marked': already_marked
        }
    )

@login_required
def marks(request):

    if is_student(request.user):
        return HttpResponse("Access Denied")

    students = Student.objects.all()

    if request.method == "POST":

        for student in students:

            Mark.objects.update_or_create(

                student=student,

                defaults={

                    'english': request.POST.get(
                        f'english_{student.id}', 0
                    ),

                    'maths': request.POST.get(
                        f'maths_{student.id}', 0
                    ),

                    'science': request.POST.get(
                        f'science_{student.id}', 0
                    ),

                    'social': request.POST.get(
                        f'social_{student.id}', 0
                    ),

                    'computer': request.POST.get(
                        f'computer_{student.id}', 0
                    ),
                }
            )

        return redirect('view_marks')

    return render(
        request,
        'marks.html',
        {'students': students}
    )

@login_required
def assignments(request):    
    
    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()

    form = AssignmentForm()
    assignments = Assignment.objects.all()

    return render(request, 'assignments.html', {
        'form': form,
        'assignments': assignments
    })

@login_required
def announcements(request):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    if request.method == "POST":
        Announcement.objects.create(
            title=request.POST.get("title"),
            message=request.POST.get("message")
        )
        return redirect('announcements')

    announcements = Announcement.objects.all().order_by('-id')

    return render(request, 'announcements.html', {
        'announcements': announcements
    })

@login_required
def profile(request):

    student = Student.objects.get(
        user=request.user
    )

    return render(
        request,
        'profile.html',
        {
            'student': student
        }
    )

@login_required
def view_marks(request):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    marks = Mark.objects.all()

    return render(
        request,
        'viewMarks.html',
        {'marks': marks}
    )

@login_required
def allAttendance(request):
        
    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    students = Student.objects.all()

    attendance_data = []

    for student in students:

        present = Attendance.objects.filter(
            student=student,
            status='Present'
        ).count()

        absent = Attendance.objects.filter(
            student=student,
            status='Absent'
        ).count()

        total = present + absent

        percentage = 0

        if total > 0:
            percentage = round(
                (present / total) * 100,
                2
            )

        attendance_data.append({
            'student': student,
            'present': present,
            'absent': absent,
            'percentage': percentage
        })

    return render(
        request,
        'allAttendance.html',
        {
            'attendance_data': attendance_data
        }
    )

@login_required
def studentViewMarks(request):

    if is_teacher(request.user):
        return HttpResponse(
            "Access Denied"
        )

    student = Student.objects.get(
        user=request.user
    )

    marks = Mark.objects.filter(
        student=student
    )

    return render(
        request,
        'studentViewMarks.html',
        {
            'marks': marks
        }
    )

@login_required
def studentViewAttendance(request):

    if is_teacher(request.user):
        return HttpResponse(
            "Access Denied"
        )

    student = Student.objects.get(
        user=request.user
    )

    attendance_records = Attendance.objects.filter(
        student=student
    ).order_by('-date')

    return render(
        request,
        'viewAttendance.html',
        {
            'attendance_records': attendance_records
        }
    )


@login_required
def viewAssignments(request):

    if is_teacher(request.user):
        return HttpResponse(
            "Access Denied"
        )

    assignments = Assignment.objects.all().order_by('due_date')

    return render(
        request,
        'viewAssignments.html',
        {
            'assignments': assignments
        }
    )

@login_required
def viewAnnouncements(request):

    if is_teacher(request.user):
        return HttpResponse(
            "Access Denied"
        )

    announcements = Announcement.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'viewAnnouncements.html',
        {
            'announcements': announcements
        }
    )

@login_required
def reportCard(request):

    if is_teacher(request.user):
        return HttpResponse(
            "Access Denied"
        )

    student = Student.objects.get(
        user=request.user
    )

    mark = Mark.objects.filter(
        student=student
    ).first()

    present = Attendance.objects.filter(
        student=student,
        status='Present'
    ).count()

    absent = Attendance.objects.filter(
        student=student,
        status='Absent'
    ).count()

    total_days = present + absent

    attendance_percentage = 0

    if total_days > 0:

        attendance_percentage = round(
            (present / total_days) * 100,
            2
        )

    return render(
        request,
        'reportCard.html',
        {
            'student': student,
            'mark': mark,
            'attendance_percentage': attendance_percentage
        }
    )

def teacher_signup(request):

    form = TeacherSignupForm()

    if request.method == 'POST':

        form = TeacherSignupForm(request.POST)

        print("FORM VALID =", form.is_valid())

        if not form.is_valid():
            print(form.errors)

        if form.is_valid():

            user = form.save()

            print("USER SAVED =", user.username)

            login(request, user)

            return redirect('teacher_dashboard')

    return render(
        request, 
        'teacherSignup.html', 
        {'form': form}
    )


def teacher_login(request):

    print("LOGIN VIEW HIT")

    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        print("USERNAME =", repr(username))
        print("PASSWORD =", repr(password))

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("AUTH RESULT =", user)

        if user:
            login(request, user)
            return redirect('teacher_dashboard')

    return render(request, "teacher.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_student(request):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    message = ""

    form = StudentForm()

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()
            message = "Student added successfully!"
            form = StudentForm()
        
        else:

            message = "Error while saving student."

    return render(
        request,
        'addStudent.html',
        {'form': form,
         'message':message}
    )

@login_required
def viewStudents(request):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    students = Student.objects.all()

    return render(
        request,
        'viewStudents.html',
        {'students': students}
    )

@login_required
def edit_student(request, id):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    student = Student.objects.get(id=id)

    form = StudentForm(
        instance=student
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect(
                'view_students'
            )

    return render(
        request,
        'editStudent.html',
        {'form': form}
    )

@login_required
def delete_student(request, id):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    student = Student.objects.get(id=id)

    student.delete()

    return redirect(
        'view_students'
    )

@login_required
def edit_assignment(request, id):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    assignment = Assignment.objects.get(id=id)

    if request.method == "POST":
        assignment.title = request.POST.get("title")
        assignment.description = request.POST.get("description")
        assignment.due_date = request.POST.get("due_date")
        assignment.save()

        return redirect('assignments')

    return render(request, 'editAssignment.html', {
        'assignment': assignment
    })

@login_required
def delete_assignment(request, id):

    if is_student(request.user):
        return HttpResponse(
            "Access Denied"
        )

    assignment = Assignment.objects.get(id=id)
    assignment.delete()

    return redirect('assignments')

def student_signup(request):

    print("STUDENT SIGNUP VIEW HIT")

    form = StudentSignupForm()

    if request.method == "POST":

        form = StudentSignupForm(request.POST)

        print("FORM VALID =", form.is_valid())

        if not form.is_valid():
            print(form.errors)

        if form.is_valid():

            user = form.save()

            Student.objects.create(
                user=user,
                name=user.username,
                roll_no="TEMP",
                student_class="TEMP",
                email="temp@gmail.com",
                phone="0000000000"
            )

            print("USER SAVED =", user.username)

            login(request, user)

            return redirect('student_dashboard')

    return render(
        request,
        'studentSignup.html',
        {'form': form}
    )

def student_login(request):

    print("STUDENT LOGIN HIT")

    if request.method == "POST":

        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("AUTH RESULT =", user)

        if user:
            login(request, user)
            return redirect('student_dashboard')

    return render(request, 'student.html')
