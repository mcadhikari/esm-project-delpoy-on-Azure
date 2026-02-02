from django.contrib import admin

# Register your models here.
from .models import AcademicYear,ExamType,StudentMarks

admin.site.register(AcademicYear)
admin.site.register(ExamType)
admin.site.register(StudentMarks)