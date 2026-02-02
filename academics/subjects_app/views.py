from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from academics.subjects_app.models import CreateSubject,CreateClassModel


# Create Subject (Admin Dashboard)
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CreateClassModel, CreateSubject

def create_subject(request):
    classes = CreateClassModel.objects.all()
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name_form')
        subject_code = request.POST.get('subject_code_form')
        class_name = request.POST.get('student_class')

        if subject_name and subject_code and class_name:
            try:
                selected_class = CreateClassModel.objects.get(class_name_model=class_name)
                CreateSubject.objects.create(
                    createsubject_fk_createclassmodel=selected_class,
                    subject_name_model=subject_name,
                    subject_code_model=subject_code
                )
                messages.success(request, "✅ Subject created successfully.")
                return redirect('createsubject')
            except CreateClassModel.DoesNotExist:
             messages.error(request, "⚠️ Selected class does not exist.")
            except Exception as e:
                messages.error(request, f"⚠️ Something went wrong: {str(e)}")
        else:
            messages.warning(request, "⚠️ Please fill in all required fields.")

    return render(request, 'subject/createsubject.html', {'classes': classes})



#manage & delete subject for admindashbord
def manage_subject(request):
    classes=CreateSubject.objects.all()
    if request.GET.get('delete'):
        try:
            subject_id=request.GET.get('delete')
            subject_obj=get_object_or_404(CreateSubject,pk=subject_id)
            subject_obj.delete()
            return redirect('managesubject')
            messages.success(request,"Subject Deleted Successfully")
        except Exception as e:
                return redirect('managesubject')
    return render(request,'subject/managesubject.html',{'classes':classes})

# #edit class for admin from admindashboard
# def edit_subject(request,subject_id):
#     subject_edit=get_object_or_404(CreateSubject,pk=subject_id)
#     if request.method=='POST':
#           try:
#               subject_name=request.POST.get('editsubject_subject_name')
#               subject_code=request.POST.get('editsubject_subject_code')
             
#               subject_edit.subject_name=subject_name
#               subject_edit.subject_code=subject_code

#               subject_edit.save()
              
#               messages.success(request,"Contain Edited")
#               return redirect('editsubject')
          
#           except Exception:
#              messages.error(request,"Could Not edit try again")
#              return redirect('editsubject', subject_id=subject_id)
#     return render(request,'editsubject.html',{'subject_edit':subject_edit})
   
