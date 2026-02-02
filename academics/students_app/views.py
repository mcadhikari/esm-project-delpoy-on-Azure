from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

from academics.students_app.forms import NewStdRegForm,CreateStudentForm
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib import messages
from academics.students_app.models import CreateStudent
from academics.classes_app.models import CreateClassModel
from academics.subjects_app.models import CreateSubject
from django.http import JsonResponse


# student registeration view
def register_student(request):
    if request.method == 'POST':
        form = NewStdRegForm(request.POST)
        if form.is_valid():
            # Store form data in session for confirmation
            form_data = form.cleaned_data
            # Render the form with confirmation data using registrationstd.html
            return render(request, 'registrationstd.html', {
                'form': form,
                'form_data': form_data,
                
            })
    else:
        form = NewStdRegForm()

    return render(request, 'registrationstd.html', {'form': form})

#views to handle student add and manage from admin
def add_student(request):
    if request.method == "POST":
        form = CreateStudentForm(request.POST, request.FILES)  # include FILES
        if form.is_valid():
            form.save()   # direct save student data
            messages.success(request, "Student Added successfully!")
            return redirect('addstudent')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CreateStudentForm()

    return render(request, 'add_student.html', {'form': form})


 
# Manage and Delete student View
def manage_student_v(request):
    student_id=request.GET.get('delete')
    if student_id:
        student=get_object_or_404(CreateStudent,id=student_id)
        student.delete()
        messages.success(request,"student Deleted")
        return  redirect('managestudent')
    students=CreateStudent.objects.all()
    return render(request,'manage_student.html',{'students':students})

#edit student
def edit_student(request, student_id):
    # Get the student object to update
    student = get_object_or_404(CreateStudent, pk=student_id)
    
    if request.method == 'POST':
        # Bind POST data and files to the form with the instance
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()  # This updates the existing object
            messages.success(request, "Student updated successfully")
            return redirect('managestudent')
        else:
            messages.error(request, "Please fix the errors below")
            print(form.errors)  # Debug validation errors
    else:
        # On GET, populate the form with existing student data
        form = CreateStudentForm(instance=student)

    return render(request, 'editstudent.html', {'form': form})

#view student

def view_student(request,student_id):
    student=get_object_or_404(CreateStudent,pk=student_id)
    return render(request,'view_student.html',{'student':student})


def get_subjects(request):
    class_id = request.GET.get("class_id")
    subjects = CreateSubject.objects.filter(createsubject_fk_createclassmodel_id=class_id)
    data = {
              "subjects": 
            [
                {"id": s.id, "name": s.subject_name_model}
             for s in subjects]
            }
    return JsonResponse(data)