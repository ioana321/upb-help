from django.contrib import admin
from .models import Subject, Seminar, Lab, Course, Activity, Exam, Document, Year, Semester
# Register your models here.
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Seminar)
admin.site.register(Lab)
admin.site.register(Activity)
admin.site.register(Exam)
admin.site.register(Document)
admin.site.register(Year)
admin.site.register(Semester)
