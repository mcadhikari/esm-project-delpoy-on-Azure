from django.db import models

# Create your models here.
from django.db import models
from academics.classes_app.models import CreateClassModel
#from academics.model.admin_model.subject_model import CreateSubject
# model for create subject

class CreateSubject(models.Model):
    
    subject_name_model = models.CharField(max_length=50)
    subject_code_model = models.CharField(max_length=10)
    Subject_max_marks_model=models.PositiveIntegerField(default=100)
    
    #relationship
    createsubject_fk_createclassmodel= models.ForeignKey(CreateClassModel, on_delete=models.SET_NULL, null=True)
    # creation_date_model = models.DateTimeField(auto_now_add=True)
    # update_date_model = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.subject_name_model}-{self.subject_code_model}"

# # Models for subjectCombination
# class SubjectCombination(models.Model):
# 	student_class = models.ForeignKey(CreateClassModel, on_delete=models.SET_NULL, null=True)
# 	subject = models.ForeignKey(CreateSubject, on_delete=models.SET_NULL, null=True)
# 	creation_date = models.DateTimeField(auto_now_add=True)
# 	update_date = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return f"{self.student_Class}-{CreateSubject}"