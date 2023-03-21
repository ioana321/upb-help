from django import forms

class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'

class DatePickerInput(forms.DateInput):
    input_type = 'date'
