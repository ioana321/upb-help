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


@register.filter(name="average")
def average(subjects):
    from college.models import Subject, Seminar, Lab, Course, Exam
    avg = 0
    subj_nr = 0
    for subj in subjects:
        subj_nr += 1
        temp = total_points(subj)
        if temp % 10 >= 5:
            avg += int((temp/10) + 1)  # 87/10 = 8.... 8+1 = 9
        else:
            avg += int(temp/10)

    return avg/subj_nr

