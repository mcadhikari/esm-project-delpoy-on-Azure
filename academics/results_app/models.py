from django.db import models
from academics.students_app.models import CreateStudent
from academics.subjects_app.models import CreateSubject

# Create your models here.
class AcademicYear(models.Model):
    years=models.CharField(max_length=20)
    
    def __str__(self):
        return self.year
    
class ExamType(models.Model):
    exam_type=models.CharField(max_length=30)
    def __str__(self):
        return self.exam_type
    
    
from django.db import models
from academics.students_app.models import CreateStudent
from academics.subjects_app.models import CreateSubject
from academics.results_app.models import AcademicYear, ExamType

class StudentMarks(models.Model):
    student = models.ForeignKey(CreateStudent, on_delete=models.CASCADE)
    #student_name = models.CharField(max_length=100, blank=True)

    subject = models.ForeignKey(CreateSubject, on_delete=models.CASCADE)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)

    max_marks = models.PositiveIntegerField(default=0)
    obtained_marks = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return f"{self.student.first_name} - {self.subject.subject} - {self.marks}"
