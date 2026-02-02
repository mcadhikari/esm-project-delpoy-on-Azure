from django.shortcuts import render, get_object_or_404
from django.db import transaction, IntegrityError
from django.contrib import messages
from academics.students_app.models import CreateClassModel, CreateStudent
from academics.subjects_app.models import CreateSubject
from academics.results_app.models import AcademicYear, ExamType, StudentMarks

def result(request):
    """Render selection form for class, year, exam."""
    classes = CreateClassModel.objects.all()
    years = AcademicYear.objects.all()
    exams = ExamType.objects.all()
    return render(request, 'add_result.html', {
        'classes': classes,
        'year': years,
        'exam_type': exams
    })



def marksheet(request):
   
    classes = CreateClassModel.objects.all()
    years = AcademicYear.objects.all()
    exams = ExamType.objects.all()

    if request.method == "POST":

        # Determine source of POST: marksheet submission or selection form
        class_id =  request.POST.get('class_field')
        year_id =  request.POST.get('academic_year')
        exam_id =  request.POST.get('exam_type')

        # Validate IDs
        if not class_id or not year_id or not exam_id:
            messages.error(request, "Please select class, year, and exam.")
            return render(request, "marksheet.html", {
                "classes": classes,
                "year": years,
                "exam_type": exams,
                "show_marks_table": False,
            })

        # Fetch objects safely
        class_obj = get_object_or_404(CreateClassModel, id=class_id)
        academic_year = get_object_or_404(AcademicYear, id=year_id)
        exam_type = get_object_or_404(ExamType, id=exam_id)

        # CASE 1: Saving marks (marksheet submission has 'class_id' from hidden input)
        if 'class_id' in request.POST:
            students = CreateStudent.objects.filter(createstudent_fk_createclassmodel=class_obj)
            subjects = CreateSubject.objects.filter(createsubject_fk_createclassmodel=class_obj)

            edited_list = []
            new_marks_saved = False

            for student in students:
                for subject in subjects:
                    field_name = f"marks_{student.id}_{subject.id}"
                    value = request.POST.get(field_name)
                    if value:
                        StudentMarks.objects.update_or_create(
                            student=student,
                            subject=subject,
                            exam_type=exam_type,
                            academic_year=academic_year,
                            defaults={'obtained_marks': int(value)}
                        )
            messages.success(request, "Marks saved successfully!")

        # CASE 2: Display marksheet table (after selection form submission)
        students = CreateStudent.objects.filter(createstudent_fk_createclassmodel=class_obj)
        subjects = CreateSubject.objects.filter(createsubject_fk_createclassmodel=class_obj)

        # Build data for template
        students_data = []
        for student in students:
            marks_list, total = [], 0
            for subject in subjects:
                mark_obj = StudentMarks.objects.filter(
                    student=student,
                    subject=subject,
                    exam_type=exam_type,
                    academic_year=academic_year
                ).first()
                if mark_obj:
                    mark_value = mark_obj.obtained_marks
                    disabled = True
                else:
                    mark_value = ""
                    disabled = False

                marks_list.append({
                    "value": mark_value,
                    "disabled": disabled,
                    "subject": subject
                })
                total += mark_value if mark_value else 0

            percent = round(total / (len(subjects) * 100) * 100, 2) if subjects else 0
            students_data.append({
                "obj": student,
                "marks_list": marks_list,
                "total": total,
                "percent": percent,
            })

        return render(request, "marksheet.html", {
            "class_obj": class_obj,
            "academic_year": academic_year,
            "exam_type": exam_type,
            "students_data": students_data,
            "subjects": subjects,
            "show_marks_table": True,
        })

    # GET request → show selection form
    return render(request, "marksheet.html", {
        "classes": classes,
        "year": years,
        "exam_type": exams,
        "show_marks_table": False,
    })
