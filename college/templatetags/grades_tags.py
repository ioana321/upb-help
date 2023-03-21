from django import template

register = template.Library()

@register.filter(name="total_points")
def total_points(subject):
    from college.models import Subject, Seminar, Lab, Course, Exam
    points = 0
    if subject.seminars.first():
        points += subject.seminars.first().points_earned
    if subject.labs.first():
        points += subject.labs.first().points_earned
    if subject.courses.first():
        points += subject.courses.first().points_earned
    exams = subject.exams.all()
    for exam in exams:
        if exam.points_earned > 0:
            points += exam.points_earned
    return points

@register.filter(name="has_course")
def has_course(subject):
    from college.models import Subject, Course
    course = subject.courses.first()
    return course

@register.filter(name="has_seminar")
def has_seminar(subject):
    from college.models import Subject, Seminar
    seminar = subject.seminars.first()
    return seminar

@register.filter(name="has_lab")
def has_lab(subject):
    from college.models import Subject, Lab
    lab = subject.labs.first()
    return lab
