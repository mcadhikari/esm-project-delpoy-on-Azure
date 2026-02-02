from django import forms
from academics.students_app.models import CreateStudent
#new student admission form
class NewStdRegForm(forms.Form):
      first_name=forms.CharField(max_length=50,label="First Name",widget=forms.TextInput(attrs={"placeholder":'First Name'}))
      middle_name=forms.CharField(max_length=50,label="Middle Name",widget=forms.TextInput(attrs={"placeholder":'Middle Name'}))
      sur_name=forms.CharField(max_length=50,label="Sur Name",widget=forms.TextInput(attrs={"placeholder":'Sur Name'}))
      father_name=forms.CharField(max_length=50,label="Father Name",widget=forms.TextInput(attrs={"placeholder":'Father Name'}))
      previous_school_name=forms.CharField(max_length=50,label="Previous School Name",widget=forms.TextInput(attrs={"placeholder":'Previous School Name'}))
      #date_of_birth_ad=forms.DateTimeField(label="DOB(AD)",required=False,widget=forms.DateInput(format='%Y-%m-%d', attrs={"placeholder":'yy-mm-dd',"type":"date"}))
      #date_of_birth_bs=forms.DateTimeField(label="DOB(B.S)",required=False,widget=forms.DateInput(format='%Y-%m-%d', attrs={"placeholder":'yy-mm-dd',"type":"date"}))
      address=forms.CharField(max_length=50,label="Address",widget=forms.TextInput(attrs={"placeholder":'Address'}))
      birth_citizen_no=forms.IntegerField(max_value=20,label="RegistrationNo",widget=forms.TextInput(attrs={"placeholder":'BirthCertificate/CitizenshipNO'}))
      
    # new form from model CreateStudent
class CreateStudentForm(forms.ModelForm):
    middle_name = forms.CharField(required=False)
    class Meta:
        model = CreateStudent
        fields =[
            'first_name','middle_name','last_name' ,
                 'dob', 'email', 'createstudent_fk_createclassmodel', 
                 'gender','photo','birth_certificate',
                 'parents_name','p_phone','address','createstudent_fk_createsubject'
                 ]
        widgets = {
            'dob': forms.DateInput(format='%Y-%M-%D', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set empty labels for dropdowns
        self.fields['createstudent_fk_createclassmodel'].empty_label = "Insert Class"
        self.fields['createstudent_fk_createsubject'].empty_label = "Insert Subject"