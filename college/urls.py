from django.urls import path, include
from .views import index, subject_list, subject, seminar, lab, course, add_seminar, add_lab, add_subject, schedule, \
    add_course, delete_course, delete_lab, delete_subject, delete_seminar, modify_subject, modify_seminar, modify_lab, \
    upload_file, open_file, delete_file, modify_course, exams, add_exam, delete_exam, modify_exam, change_exam_state, \
    set_points, grades

app_name = 'college'

urlpatterns = [
    path('', index, name='index'),
    path('subject_list/', subject_list, name='subject_list'),
    path('subject/<int:pk>', subject, name='subject'),
    path('subject/<int:pk>/seminar', seminar, name='seminar'),
    path('subject/<int:pk>/lab', lab, name='lab'),
    path('subject/<int:pk>/course', course, name='course'),
    path('add_seminar/', add_seminar, name='add_seminar'),
    path('add_lab/', add_lab, name='add_lab'),
    path('add_subject/', add_subject, name='add_subject'),
    path('schedule', schedule, name='schedule'),
    path('add_course/', add_course, name='add_course'),
    path('subject/<int:pk>/delete_course/', delete_course, name='delete_course'),
    path('subject/<int:pk>/delete_seminar/', delete_seminar, name='delete_seminar'),
    path('subject/<int:pk>/delete_lab/', delete_lab, name='delete_lab'),
    path('subject/<int:pk>/delete_subject/', delete_subject, name='delete_subject'),
    path('subject/<int:pk>/modify_subject/', modify_subject, name='modify_subject'),
    path('subject/<int:pk>/modify_seminar/', modify_seminar, name='modify_seminar'),
    path('subject/<int:pk>/modify_lab/', modify_lab, name='modify_lab'),
    path('upload_file/<str:activity_name>/<int:pk>/', upload_file, name='upload_file'),
    path('open_file/<int:pk>/', open_file, name='open_file'),
    path('delete_file/<int:pk>/', delete_file, name='delete_file'),
    path('subject/<int:pk>/modify_course/', modify_course, name='modify_course'),
    path('exams/', exams, name='exams'),
    path('add_exam/', add_exam, name='add_exam'),
    path('delete_exam/<int:pk>/', delete_exam, name='delete_exam'),
    path('modify_exam/<int:pk>/', modify_exam, name='modify_exam'),
    path('change_exam_state/<int:pk>/', change_exam_state, name='change_exam_state'),
    path('<str:activity_name>/<int:pk>/set_points/', set_points, name='set_points'),
    path('grades/', grades, name='grades'),
    ]
