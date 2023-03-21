from .models import Seminar, Lab, Subject, Activity, Course
from rest_framework import serializers

class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields =('room',
                 'professor',
                 'points',
                 'subject',
                 'nr',
                 )

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields =('room',
                 'professor',
                 'points',
                 'subject',
                 'nr',
                 )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =('room',
                 'points',
                 'subject',
                 'nr',
                 )

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',
                  'professor',
                  'credit_points',
                  )
