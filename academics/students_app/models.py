from django.db import models

# Create your models here.
from django.db import models
from academics.classes_app.models import CreateClassModel
from django.conf import settings
from academics.subjects_app.models import CreateSubject


# New Student Registration model

class NewStdRegModel(models.Model):
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50, blank=True, null=True)
	sur_name = models.CharField(max_length=50)
	father_name = models.CharField(max_length=100)
	previous_school = models.CharField(max_length=100, blank=True, null=True)
	# date_of_birth_ad = models.DateField(null=True, blank=True)
	# date_of_birth_bs = models.DateField(null=True, blank=True)
	address = models.TextField()
	birth_citizen_no = models.CharField(max_length=20)
	registration_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.sur_name}"


# Model for create student
class CreateStudent(models.Model):
    gender_choices = (
        ('','Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('others','others')
    )
    #Relation
    createstudent_fk_createclassmodel = models.ForeignKey(CreateClassModel, on_delete=models.SET_NULL, null=True)
    createstudent_fk_createsubject=models.ForeignKey(CreateSubject,on_delete=models.SET_NULL,null=True)
    #personal_info
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    #Documents
    birth_certificate = models.ImageField(upload_to='documents/birth_certificate/', null=True, blank=True)
    photo = models.ImageField(upload_to='documents/photos', null=True, blank=True)
    #parents info
    parents_name = models.CharField(max_length=50)
    p_phone = models.CharField(max_length=15)  # changed from IntegerField
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

