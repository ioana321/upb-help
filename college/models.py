from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Year(models.Model):
    number = models.PositiveSmallIntegerField()
    def __str__(self):
        return 'Year ' + str(self.number)


class Semester(models.Model):
    count = models.PositiveSmallIntegerField(null=True)
    year = models.ForeignKey(Year,
                             related_name='semesters',
                             default=0,
                             on_delete=models.CASCADE
                             )
    def __str__(self):
        return 'Year ' + str(self.year.number) + ' Sem ' + str(self.count)

class Subject(models.Model):
    name = models.CharField(max_length=150)
    professor = models.CharField(max_length=150)
    credit_points = models.PositiveSmallIntegerField()
    points_earned = models.IntegerField(default=0)
    # semester = models.ForeignKey(Semester,
    #                              related_name='subjects',
    #                              blank=True,
    #                              on_delete=models.CASCADE
    #                              )
    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=50)
    document = models.FileField(upload_to='documents/',
                                validators=[FileExtensionValidator(['pdf'],
                                                                   'Please upload a .pdf file!'
                                                                   )]
                                )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return self.name

class Seminar(models.Model):
    room = models.CharField(max_length=10)
    professor = models.CharField(max_length=150)
    points = models.PositiveSmallIntegerField()
    nr = models.IntegerField()
    subject = models.ForeignKey(Subject,
                                   related_name='seminars',
                                   blank=True,
                                   on_delete=models.CASCADE
                                   )
    documents = GenericRelation(Document, related_query_name='seminar')
    points_earned = models.IntegerField(default=0)
    def __str__(self):
        name = 'Seminar ' + self.subject.name# + ' ' + str(self.nr)
        return name

class Lab(models.Model):
    room = models.CharField(max_length=10)
    professor = models.CharField(max_length=150)
    points = models.PositiveSmallIntegerField()
    nr = models.IntegerField()
    subject = models.ForeignKey(Subject,
                                   related_name='labs',
                                   blank=True,
                                   on_delete=models.CASCADE
                                   )
    documents = GenericRelation(Document, related_query_name='lab')
    points_earned = models.IntegerField(default=0)
    def __str__(self):
        name = 'Lab ' + self.subject.name + ' ' + str(self.nr)
        return name

class Course(models.Model):
    room = models.CharField(max_length=10)
    points = models.PositiveSmallIntegerField(blank=True)
    nr = models.IntegerField()
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                blank=True,
                                on_delete=models.CASCADE,
                                )
    documents = GenericRelation(Document, related_query_name='course')
    points_earned = models.IntegerField(default=0)
    def __str__(self):
        return self.subject.name

class Activity(models.Model):
    type = models.CharField(max_length=10, null=True)
    room = models.CharField(max_length=10)
    start_hour = models.IntegerField(null=True)
    end_hour = models.IntegerField(null=True)
    day = models.CharField(max_length=10, null=True)
    week = models.CharField(max_length=10, null=True)
    subject = models.ForeignKey(Subject,
                                related_name='activities',
                                blank=True,
                                on_delete=models.CASCADE,
                                null=True
                                )
    def __str__(self):
        return self.subject.name + ' ' + self.type + ' ' + self.week

class Exam(models.Model):
    subject = models.ForeignKey(Subject,
                                related_name='exams',
                                blank=True,
                                on_delete=models.CASCADE,
                                null=True
                                )
    type = models.CharField(max_length=15)
    date = models.DateField()
    points = models.PositiveSmallIntegerField(default=1)
    done = models.BooleanField(default=False)
    points_earned = models.IntegerField(default=0)
    def __str__(self):
        if self.type == 'Partial' or self.type == 'Final':
            return self.subject.name + ' ' + self.type + ' Exam'
        else:
            return self.subject.name + ' ' + self.type
