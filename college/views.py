import datetime

from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect
from .models import Subject, Course, Lab, Seminar, Activity, Document, Exam
from .forms import SeminarForm, LabForm, SubjectForm, CourseForm, DocumentForm, ModifyCoursesForm, ExamForm
from .serializers import SeminarSerializer, LabSerializer, SubjectSerializer, CourseSerializer
from django.urls import reverse


# Create your views here.

def create(body, type, subject=None):
    day = body['day']
    week = body['week']
    if (subject == None):
        subject = body['subject']

    if (week != '3'):
        activity = Activity.objects.create()
        activity.type = type
        activity.room = body['room']
        activity.start_hour = body['start_hour']
        activity.end_hour = body['end_hour']
        activity.subject = Subject.objects.get(pk=subject)
        activity.day = day
        activity.week = week
        activity = activity.save()
    else:
        activity_odd = Activity.objects.create()
        activity_odd.type = type
        activity_odd.room = body['room']
        activity_odd.start_hour = body['start_hour']
        activity_odd.end_hour = body['end_hour']
        activity_odd.subject = Subject.objects.get(pk=subject)
        activity_odd.day = day
        activity_odd.week = 'Odd'
        activity_odd = activity_odd.save()

        activity_even = Activity.objects.create()
        activity_even.type = type
        activity_even.room = body['room']
        activity_even.start_hour = body['start_hour']
        activity_even.end_hour = body['end_hour']
        activity_even.subject = Subject.objects.get(pk=subject)
        activity_even.day = day
        activity_even.week = 'Even'
        activity_even = activity_even.save()


def index(request):
    return render(request, 'college/index.html')


def subject_list(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, 'college/subject_list.html', context)


def subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    has_course = has_seminar = has_lab = 0
    if subject.labs.first():
        has_lab = 1
    if subject.courses.first():
        has_course = 1
    if subject.seminars.first():
        has_seminar = 1
    context = {
        'subject': subject,
        'has_course': has_course,
        'has_seminar': has_seminar,
        'has_lab': has_lab,
    }
    return render(request, 'college/subject.html', context)


def seminar(request, pk):
    subject = Subject.objects.get(pk=pk)
    seminars = subject.seminars.all()
    first_sem = subject.seminars.first()

    context = {
        'seminars': seminars,
        'subject': subject,
        'professor': first_sem.professor,
        'points': first_sem.points,
        'points_earned': first_sem.points_earned,
        'id': first_sem.id,
    }
    return render(request, 'college/seminar.html', context)


def lab(request, pk):
    subject = Subject.objects.get(pk=pk)
    labs = subject.labs.all()
    first_lab = subject.labs.first()
    context = {
        'labs': labs,
        'subject': subject,
        'professor': first_lab.professor,
        'points': first_lab.points,
        'points_earned': first_lab.points_earned,
        'id': first_lab.id,
    }
    return render(request, 'college/lab.html', context)


def course(request, pk):
    subject = Subject.objects.get(pk=pk)
    courses = subject.courses.all()
    first_course = subject.courses.first()
    if first_course.points:
        points = first_course.points
    else:
        points = 0
    context = {
        'courses': courses,
        'subject': subject,
        'professor': subject.professor,
        'points': points,
        'points_earned': first_course.points_earned,
        'id': first_course.id,
    }
    return render(request, 'college/course.html', context)


def add_seminar(request):
    if (request.method == 'GET'):
        return render(
            request, 'college/add_seminar.html',
            {'form': SeminarForm}
        )
    elif request.method == 'POST':
        body = request.POST

        create(body, 'seminar')

        seminar_data = {}
        seminar_data['room'] = body['room']
        seminar_data['professor'] = body['professor']
        seminar_data['points'] = body['points']
        seminar_data['subject'] = body['subject']
        if (body['week'] == '3'):
            sem_nr = 14
        else:
            sem_nr = 7
        for i in range(sem_nr):
            seminar_data['nr'] = i + 1
            seminar_serializer = SeminarSerializer(data=seminar_data)
            if (seminar_serializer.is_valid()):
                seminar = seminar_serializer.save()
        return HttpResponseRedirect(reverse('college:seminar', args=(seminar.subject.id,)))


def add_lab(request):
    if (request.method == 'GET'):
        return render(
            request, 'college/add_lab.html',
            {'form': LabForm}
        )
    elif request.method == 'POST':
        body = request.POST

        create(body, 'lab')

        lab_data = {}
        lab_data['room'] = body['room']
        lab_data['professor'] = body['professor']
        lab_data['points'] = body['points']
        lab_data['subject'] = body['subject']
        if (body['week'] == '3'):
            lab_nr = 14
        else:
            lab_nr = 7
        for i in range(lab_nr):
            lab_data['nr'] = i + 1
            lab_serializer = LabSerializer(data=lab_data)
            if (lab_serializer.is_valid()):
                lab = lab_serializer.save()
        return HttpResponseRedirect(reverse('college:lab', args=(lab.subject.id,)))


def add_subject(request):
    if (request.method == 'GET'):
        return render(
            request, 'college/add_subject.html',
            {'form': SubjectForm}
        )
    elif request.method == 'POST':
        body = request.POST
        subject_data = {}
        subject_data['name'] = body['name']
        subject_data['professor'] = body['professor']
        subject_data['credit_points'] = body['credit_points']
        subject_serializer = SubjectSerializer(data=subject_data)
        if subject_serializer.is_valid():
            subject = subject_serializer.save()
        return HttpResponseRedirect(reverse('college:subject', args=(subject.id,)))


def add_course(request):
    if (request.method == 'GET'):
        return render(
            request, 'college/add_course.html',
            {'form': CourseForm}
        )
    elif request.method == 'POST':
        body = request.POST

        create(body, 'course')

        course_data = {}
        course_data['room'] = body['room']
        course_data['points'] = body['points']
        course_data['subject'] = body['subject']
        subject = Subject.objects.get(pk=body['subject'])
        if (subject.courses.first()):
            if body['week'] == '3':
                c_nr = 14
            else:
                c_nr = 7
            for i in range(c_nr):
                course_data['nr'] = i + 1
                course_serializer = CourseSerializer(data=course_data)
                if course_serializer.is_valid():
                    course = course_serializer.save()
            i = 1
            for course in subject.courses.all():
                course.nr = i
                course.save()
                i += 1
        else:
            if body['week'] == '3':
                c_nr = 14
            else:
                c_nr = 7
            for i in range(c_nr):
                course_data['nr'] = i + 1
                course_serializer = CourseSerializer(data=course_data)
                if course_serializer.is_valid():
                    course = course_serializer.save()

        return HttpResponseRedirect(reverse('college:course', args=(subject.id,)))


def schedule(request):
    context = {
        'week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        'hours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                  18, 19, 20, 21],
    }
    return render(request, 'college/schedule.html', context)


def delete_course(request, pk):
    subject = Subject.objects.get(pk=pk)
    courses = subject.courses.all()
    for course in courses:
        course.delete()
    activities = subject.activities.filter(type='course')
    for activity in activities:
        activity.delete()
    return HttpResponseRedirect(reverse('college:subject', args=(subject.id,)))


def delete_seminar(request, pk):
    subject = Subject.objects.get(pk=pk)
    seminars = subject.seminars.all()
    for seminar in seminars:
        seminar.delete()
    activities = subject.activities.filter(type='seminar')
    for activity in activities:
        activity.delete()
    return HttpResponseRedirect(reverse('college:subject', args=(subject.id,)))


def delete_lab(request, pk):
    subject = Subject.objects.get(pk=pk)
    labs = subject.labs.all()
    for lab in labs:
        lab.delete()
    activities = subject.activities.filter(type='lab')
    for activity in activities:
        activity.delete()
    return HttpResponseRedirect(reverse('college:subject', args=(subject.id,)))


def delete_subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    subject.delete()
    return HttpResponseRedirect(reverse('college:subject_list'))


def modify_subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    if request.method == 'POST':
        body = request.POST
        subject.name = body['name']
        subject.professor = body['professor']
        subject.credit_points = body['credit_points']
        subject.save()
        return HttpResponseRedirect(reverse('college:subject', args=(subject.id,)))
    else:
        form = SubjectForm(initial={'name': subject.name,
                                    'professor': subject.professor,
                                    'credit_points': subject.credit_points,
                                    })
        return render(
            request, 'college/modify_subject.html',
            {'form': form}
        )


def modify_seminar(request, pk):
    subject = Subject.objects.get(pk=pk)
    seminars = subject.seminars.all()
    activities = subject.activities.filter(type='seminar')
    if request.method == 'POST':
        body = request.POST
        if seminars.last().nr == 7 and body['week'] == '3':
            for i in range(7):
                new_seminar = SeminarSerializer(data={'room': body['room'],
                                                      'professor': body['professor'],
                                                      'points': body['points'],
                                                      'subject': subject.id,
                                                      'nr': i + 8,
                                                      })
                if new_seminar.is_valid():
                    final_new_sem = new_seminar.save()
        elif seminars.last().nr == 14 and body['week'] != '3':
            for i in range(8, 15):
                deleted_seminar = seminars.get(nr=i)
                deleted_seminar.delete()

        for seminar in seminars:
            seminar.room = body['room']
            seminar.professor = body['professor']
            if seminar.points != body['points']:
                seminar.points = body['points']
                seminar.points_earned = 0
            seminar.save()
        for activity in activities:
            activity.delete()
        create(body, 'seminar', subject.id)
        return HttpResponseRedirect(reverse('college:seminar', args=(subject.id,)))
    else:
        if activities.first() != activities.last():
            week = '3'
        else:
            week = activities.first().week
        form_init = {'week': week,
                     'day': activities.first().day,
                     'room': seminars.first().room,
                     'professor': seminars.first().professor,
                     'points': seminars.first().points,
                     'start_hour': activities.first().start_hour,
                     'end_hour': activities.first().end_hour,
                     }
        form = SeminarForm(initial=form_init, modify_form=True)
        return render(
            request, 'college/modify_seminar.html',
            {'form': form}
        )


def modify_lab(request, pk):
    subject = Subject.objects.get(pk=pk)
    labs = subject.labs.all()
    activities = subject.activities.filter(type='lab')
    if request.method == 'POST':
        body = request.POST
        if labs.last().nr == 7 and body['week'] == '3':
            for i in range(7):
                new_lab = LabSerializer(data={'room': body['room'],
                                              'professor': body['professor'],
                                              'points': body['points'],
                                              'subject': subject.id,
                                              'nr': i + 8,
                                              })
                if new_lab.is_valid():
                    final_new_lab = new_lab.save()
        elif labs.last().nr == 14 and body['week'] != '3':
            for i in range(8, 15):
                deleted_lab = labs.get(nr=i)
                deleted_lab.delete()

        for lab in labs:
            lab.room = body['room']
            lab.professor = body['professor']
            if lab.points != body['points']:
                lab.points = body['points']
                lab.points_earned = 0
            lab.save()
        for activity in activities:
            activity.delete()
        create(body, 'lab', subject.id)
        return HttpResponseRedirect(reverse('college:lab', args=(subject.id,)))
    else:
        if activities.first() != activities.last():
            week = '3'
        else:
            week = activities.first().week
        form_init = {'week': week,
                     'day': activities.first().day,
                     'room': labs.first().room,
                     'professor': labs.first().professor,
                     'points': labs.first().points,
                     'start_hour': activities.first().start_hour,
                     'end_hour': activities.first().end_hour,
                     }
        form = LabForm(initial=form_init, modify_form=True)
        return render(
            request, 'college/modify_lab.html',
            {'form': form}
        )


def modify_course(request, pk):
    subject = Subject.objects.get(pk=pk)
    courses = subject.courses.all()
    activities = subject.activities.filter(type='course')
    if courses.last().nr <= 14:
        if request.method == 'POST':
            body = request.POST
            if courses.last().nr == 7 and body['week'] == '3':
                for i in range(7):
                    new_course = CourseSerializer(data={'room': body['room'],
                                                        'points': body['points'],
                                                        'subject': subject.id,
                                                        'nr': i + 8,
                                                        })
                    if new_course.is_valid():
                        final_new_course = new_course.save()
            elif courses.last().nr == 14 and body['week'] != '3':
                for i in range(8, 15):
                    deleted_course = courses.get(nr=i)
                    deleted_course.delete()
            for course in courses:
                course.room = body['room']
                course.points = body['points']
                course.save()
            for activity in activities:
                activity.delete()
            create(body, 'course', subject.id)
            return HttpResponseRedirect(reverse('college:course', args=(subject.id,)))
        else:
            if activities.first() != activities.last():
                week = '3'
            else:
                week = activities.first().week
            form_init = {'week': week,
                         'day': activities.first().day,
                         'room': courses.first().room,
                         'points': courses.first().points,
                         'start_hour': activities.first().start_hour,
                         'end_hour': activities.first().end_hour,
                         }
            form = CourseForm(initial=form_init, modify_form=True)
            return render(
                request, 'college/modify_course.html',
                {'form': form}
            )


def upload_file(request, activity_name, pk):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if (activity_name == 'seminar'):
            activity = Seminar.objects.get(pk=pk)
        elif activity_name == 'lab':
            activity = Lab.objects.get(pk=pk)
        elif activity_name == 'course':
            activity = Course.objects.get(pk=pk)
        if form.is_valid():
            document = activity.documents.create(document=form.cleaned_data.get('document'),
                                                 name=form.cleaned_data.get('name'))
            if activity_name == 'seminar':
                return HttpResponseRedirect(reverse('college:seminar', args=(activity.subject.id,)))
            elif activity_name == 'lab':
                return HttpResponseRedirect(reverse('college:lab', args=(activity.subject.id,)))
            else:
                return HttpResponseRedirect(reverse('college:course', args=(activity.subject.id,)))
    else:
        form = DocumentForm()
    return render(request, 'college/upload_file.html', {'form': form})


def open_file(request, pk):
    document = Document.objects.get(pk=pk)
    return FileResponse(document.document.open())


def delete_file(request, pk):
    document = Document.objects.get(pk=pk)
    activity = document.content_object
    document.delete()
    if activity.__class__.__name__ == 'Seminar':
        return HttpResponseRedirect(reverse('college:seminar', args=(activity.subject.id,)))
    elif activity.__class__.__name__ == 'Lab':
        return HttpResponseRedirect(reverse('college:lab', args=(activity.subject.id,)))
    else:
        return HttpResponseRedirect(reverse('college:course', args=(activity.subject.id,)))


def exams(request):
    exams = Exam.objects.filter(done=False).order_by('date')
    past_exams = Exam.objects.filter(done=True).order_by('date')
    return render(request,
                  'college/exams.html',
                  {'exams': exams,
                   'past_exams': past_exams,
                   }
                  )


def add_exam(request):
    if (request.method == 'GET'):
        return render(request,
                      'college/add_exam.html',
                      {'form': ExamForm()},
                      )
    elif (request.method == 'POST'):
        form = ExamForm(request.POST)
        if (form.is_valid()):
            exam = Exam(subject=form.cleaned_data['subject'],
                        type=form.cleaned_data['type'],
                        date=form.cleaned_data['date'],
                        points=form.cleaned_data['points']
                        )
            if exam.date.strftime("%Y%m%d") < datetime.datetime.now().strftime("%Y%m%d"):
                exam.done = True
            exam.save()
            return HttpResponseRedirect(reverse('college:exams'))


def delete_exam(request, pk):
    exam = Exam.objects.get(pk=pk)
    exam.delete()
    return HttpResponseRedirect(reverse('college:exams'))


def modify_exam(request, pk):
    exam = Exam.objects.get(pk=pk)
    if (request.method == 'GET'):
        form_init = {'subject': exam.subject,
                     'type': exam.type,
                     'date': exam.date,
                     'points': exam.points,
                     }
        form = ExamForm(initial=form_init)
        return render(request,
                      'college/modify_exam.html',
                      {'form': form},
                      )
    elif request.method == 'POST':
        body = request.POST
        exam.subject = Subject.objects.get(pk=body['subject'])
        exam.type = body['type']
        exam.date = body['date']
        exam.points = body['points']
        exam.save()
        return HttpResponseRedirect(reverse('college:exams'))


def change_exam_state(request, pk):
    exam = Exam.objects.get(pk=pk)
    if exam.done == False:
        exam.done = True
    else:
        exam.points_earned = 0
        exam.done = False
    exam.save()
    return HttpResponseRedirect(reverse('college:exams'))


# def set_points(request, pk):
#     exam = Exam.objects.get(pk=pk)
#     if request.method == 'GET':
#         return render(request, 'college/set_points.html', {'exam': exam})
#     elif request.method == 'POST':
#         data = request.POST
#         exam.points_earned = data.get('points', False)
#         exam.save()
#         return HttpResponseRedirect(reverse('college:exams'))


def grades(request):
    return render(request, 'college/grades.html', {'subjects': Subject.objects.all()})

def set_points(request, activity_name, pk):
    if activity_name == 'seminar':
        activity = Seminar.objects.get(pk=pk)
    elif activity_name == 'lab':
        activity = Lab.objects.get(pk=pk)
    elif activity_name == 'exam':
        activity = Exam.objects.get(pk=pk)
    else:
        activity = Course.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'college/set_points.html', {'activity': activity})
    elif request.method == 'POST':
        data = request.POST
        activity.points_earned = data.get('points', False)
        activity.save()
        if activity_name == 'seminar':
            return HttpResponseRedirect(reverse('college:seminar', args=(activity.subject.id,)))
        elif activity_name == 'lab':
            return HttpResponseRedirect(reverse('college:lab', args=(activity.subject.id,)))
        elif activity_name == 'exam':
            return HttpResponseRedirect(reverse('college:exams'))
        else:
            return HttpResponseRedirect(reverse('college:course', args=(activity.subject.id,)))


# de terminat cu punctajele, inca nu apare lista cu pct pt act, + media sem.