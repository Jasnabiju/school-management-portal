from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.teacher_login, name='login'),
    path(
    'student-login/',
    views.student_login,
    name='student_login'
),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('logout/', views.logout_view, name='logout'),

    path('teacher-dashboard/',
         views.teacher_dashboard,
         name='teacher_dashboard'),

    path('student-dashboard/',
         views.student_dashboard,
         name='student_dashboard'),

    path(
        'attendance/', 
        views.attendance,
        name='attendance'),
    
    path(
    'view-marks/',
    views.view_marks,
    name='view_marks'
),

    path('marks/',
         views.marks,
         name='marks'),

    path(
    'assignments/',
    views.assignments,
    name='assignments'
),

path(
    'announcements/',
    views.announcements,
    name='announcements'
),

path(
    'profile/',
    views.profile,
    name='profile'
),

path(
    'calendar/',
    views.calendar,
    name='calendar'
),
    path('allAttendance/', views.allAttendance, name='all_attendance'),

path(
    'studentViewAttendance/',
    views.studentViewAttendance,
    name='student_view_attendance'
),

path(
    'studentViewMarks/',
    views.studentViewMarks,
    name='student_view_marks'
),

path(
    'viewAssignments/',
    views.viewAssignments,
    name='view_assignments'
),

path(
    'viewAnnouncements/',
    views.viewAnnouncements,
    name='view_announcements'
),

path(
    'reportCard/',
    views.reportCard,
    name='report_card'
),

path(
    'viewCalendar/',
    views.viewCalendar,
    name='view_calendar'
),
    path(
        'teacherSignup/',
        views.teacher_signup,
        name='teacher_signup'
    ),    

    path(
    'studentSignup/',
    views.student_signup,
    name='student_signup'
),

    path(
        'addStudent/',
        views.add_student,
        name='add_student'
    ),
    
    path(
        'viewStudents/',
        views.viewStudents,
        name='view_students'
    ),
    
    path(
        'editStudent/<int:id>/',
        views.edit_student,
        name='edit_student'
    ),
    
    path(
        'deleteStudent/<int:id>/',
        views.delete_student,
        name='delete_student'
    ),

    path('edit-assignment/<int:id>/', views.edit_assignment, name='edit_assignment'),
    path('delete-assignment/<int:id>/', views.delete_assignment, name='delete_assignment'),


]