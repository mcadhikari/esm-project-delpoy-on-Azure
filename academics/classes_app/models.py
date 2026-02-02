from django.db import models
# model for create class
class CreateClassModel(models.Model):
	class_name_model = models.CharField(max_length=50, null=False)
	class_numeric_model = models.IntegerField()
	class_section_model = models.CharField(max_length=20)
	creation_date_model = models.DateTimeField(auto_now_add=True)
	update_date_model = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.class_name_model}"