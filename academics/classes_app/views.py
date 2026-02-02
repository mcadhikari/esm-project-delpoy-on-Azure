from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CreateClassModel

# Create class from Admin dashboard
def create_class(request):
    if request.method == 'POST':
        try:
            class_name = request.POST.get('class_name_form')
            class_numeric = int(request.POST.get('class_numeric_form'))  # Cast to integer
            class_section = request.POST.get('class_section_form')

            CreateClassModel.objects.create(
                class_name_model=class_name,
                class_numeric_model=class_numeric,
                class_section_model=class_section
            )
            messages.success(request, "Class Created Successfully")
            return redirect('createclass')
        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect('createclass')

    return render(request, 'createclass.html')


# Manage & delete class for Admin dashboard
def manage_class(request):
    classes = CreateClassModel.objects.all()
    if request.GET.get('delete'):
        try:
            class_id = request.GET.get('delete')
            class_obj = get_object_or_404(CreateClassModel, pk=class_id)
            class_obj.delete()
            messages.success(request, "Class Deleted Successfully")  # Before redirect
            return redirect('manageclass')
        except Exception as e:
            messages.error(request, f"Could not delete: {str(e)}")
            return redirect('manageclass')

    return render(request, 'manageclass.html', {'classes': classes})


# Edit class for Admin dashboard
def edit_class(request, class_id):
    class_edit = get_object_or_404(CreateClassModel, pk=class_id)

    if request.method == 'POST':
        try:
            class_name = request.POST.get('editclass_class_name')
            class_numeric = int(request.POST.get('editclass_class_numeric'))  # Cast to integer
            class_section = request.POST.get('editclass_class_section')

            class_edit.class_name_model = class_name
            class_edit.class_numeric_model = class_numeric
            class_edit.class_section_model = class_section  # Correct field name
            class_edit.save()

            messages.success(request, "Class Edited Successfully")
            return redirect('manageclass')
        except Exception as e:
            messages.error(request, f"Could not edit class: {str(e)}")
            return redirect('editclass', class_id=class_id)

    return render(request, 'editclass.html', {'class_edit': class_edit})
