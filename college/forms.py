from django import forms
from .models import Seminar, Subject, Lab, Document, Year
from .widgets import DateTimePickerInput, DatePickerInput


class SeminarForm(forms.Form):
    nr = forms.IntegerField(required=False, widget=forms.HiddenInput())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    week = forms.ChoiceField(choices=(('Odd', 'Odd weeks (1, 3, 5...'), ('Even', 'Even weeks(2, 4, 6...'),
                                      (3, 'Every week')))
    day = forms.ChoiceField(choices=(('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                     ('Thursday', 'Thursday'), ('Friday', 'Friday')))
    room = forms.CharField(max_length=10)
    professor = forms.CharField(max_length=150)
    points = forms.IntegerField()
    start_hour = forms.IntegerField()
    end_hour = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        modify_form = kwargs.get('modify_form', False)
        if 'modify_form' in kwargs:
            del kwargs['modify_form']
        super(SeminarForm, self).__init__(*args, **kwargs)
        if modify_form:
            del self.fields['subject']

class LabForm(forms.Form):
    nr = forms.IntegerField(required=False, widget=forms.HiddenInput())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    week = forms.ChoiceField(choices=(('Odd', 'Odd weeks (1, 3, 5...'), ('Even', 'Even weeks(2, 4, 6...'),
                                      (3, 'Every week')))
    day = forms.ChoiceField(choices=(('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                     ('Thursday', 'Thursday'), ('Friday', 'Friday')))
    room = forms.CharField(max_length=10)
    professor = forms.CharField(max_length=150)
    points = forms.IntegerField()
    start_hour = forms.IntegerField()
    end_hour = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        modify_form = kwargs.get('modify_form', False)
        if 'modify_form' in kwargs:
            del kwargs['modify_form']
        super(LabForm, self).__init__(*args, **kwargs)
        if modify_form:
            del self.fields['subject']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name',
                  'professor',
                  'credit_points',
                  ]

class CourseForm(forms.Form):
    nr = forms.IntegerField(required=False, widget=forms.HiddenInput())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    week = forms.ChoiceField(choices=(('Odd', 'Odd weeks (1, 3, 5...'), ('Even', 'Even weeks(2, 4, 6...'),
                                      (3, 'Every week')))
    day = forms.ChoiceField(choices=(('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                     ('Thursday', 'Thursday'), ('Friday', 'Friday')))
    room = forms.CharField(max_length=10)
    points = forms.IntegerField()
    start_hour = forms.IntegerField()
    end_hour = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        modify_form = kwargs.get('modify_form', False)
        if 'modify_form' in kwargs:
            del kwargs['modify_form']
        super(CourseForm, self).__init__(*args, **kwargs)
        if modify_form:
            del self.fields['subject']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name',
                  'document',
                  )

class ModifyCoursesForm(forms.Form):
    course1_week = forms.ChoiceField(choices=(('Odd', 'Odd weeks (1, 3, 5...'), ('Even', 'Even weeks(2, 4, 6...'),
                                      (3, 'Every week')))
    course1_day = forms.ChoiceField(choices=(('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                     ('Thursday', 'Thursday'), ('Friday', 'Friday')))
    course1_room = forms.CharField(max_length=10)
    course1_start_hour = forms.IntegerField()
    course1_end_hour = forms.IntegerField()
    course2_week = forms.ChoiceField(choices=(('Odd', 'Odd weeks (1, 3, 5...'), ('Even', 'Even weeks(2, 4, 6...'),
                                              (3, 'Every week')))
    course2_day = forms.ChoiceField(choices=(('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                             ('Thursday', 'Thursday'), ('Friday', 'Friday')))
    course2_room = forms.CharField(max_length=10)
    course2_start_hour = forms.IntegerField()
    course2_end_hour = forms.IntegerField()

class ExamForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    type = forms.ChoiceField(choices=(('Partial', 'Partial'),
                                      ('Final', 'Final'),
                                      ('Test', 'Test'),
                                      ('Colocviu', 'Colocviu'),
                                      )
                             )
    date = forms.DateField(widget=DatePickerInput())
    points = forms.IntegerField()

class YearForm(forms.ModelForm):
    class Meta:
        model = Year
        fields = ('number',
                  )
