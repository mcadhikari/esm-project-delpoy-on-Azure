"""
URL configuration for esm_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from academics.subjects_app.views import create_subject,manage_subject
from dashboard_layout_app.views import admin_dashboard_content_views,index
from academics.students_app.views import view_student,edit_student,manage_student_v,add_student,register_student,get_subjects
from academics.classes_app.views import edit_class,manage_class,create_class
from User_Creation_app.views import user_login
from academics.results_app.views import result, marksheet
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',index,name='index'), 
    path('nsr/',register_student,name='registration_std'),
    #admin
    path('login/',user_login,name='userlogin'),
  
   
    #class
    path('c_class/',create_class,name="createclass"),
    path('m_class/',manage_class,name='manageclass'),
    path('edit_class/<int:class_id>/',edit_class ,name='editclass'),
    #student
    path('a_student/',add_student,name='addstudent'),
    path('managestudent/',manage_student_v,name='managestudent'),
    path('e_student/<int:student_id>/',edit_student,name='editstudent'),
    path('v_student/<int:student_id>/',view_student,name='viewstudent'),
    
    # #subject
     path('createsubject/',create_subject,name='createsubject'),
     path('m_subject/',manage_subject,name='managesubject'),
    # path('edit_subject/<int:subject_id>/',edit_subject,name='editsubject'),
    
    # #notice
    # path('notice/',add_notice_views,name='addnotice'),
    # path('mnotice/',manage_notice_views,name='managenotice'),
    # path('noticeboard/',notice_board_views,name='noticeboard'),
    
    #t dashboard
    #path('t_dashboard/',teacher_dashboard_views,name='teacher_dashboard'),
     path('a_dashboard/',admin_dashboard_content_views,name='admin-dashboard-content'),
     path('get-subjects/', get_subjects, name='get_subjects'),
     # result
    path('std_result/',result,name='result'),
    path('marksheet/', marksheet, name='marksheet'),
   # path('save_marks/', save_marks, name='savemarks'),
    
]
