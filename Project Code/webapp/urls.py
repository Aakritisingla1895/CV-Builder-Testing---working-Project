from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.login_screen),
    path('signup',views.signup,name='signup'),
    path('userlogin',views.userlogin, name='userlogin'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('home',views.home,name='home'),
    path('uploadPdf', views.uploadPdf, name='uploadPdf'),
    path('processing_cv', views.processingCV, name='processingCV'),
    path('about_us', views.about_us, name='about_us'),
    path('question_form', views.question_form, name='question_form'),
    path('professional_experience_form', views.professional_experience_form, name='professional_experience_form'),
    path('work_experience_form', views.work_experience_form, name='work_experience_form'),
    path('technical_skills_form', views.technical_skills_form, name='technical_skills_form'),
    path('certifications_form', views.certifications_form, name='certifications_form'),
    path('education_form', views.education_form, name='education_form'),
    path('chatgptBackend', views.chatgptBackend, name='chatgptBackend'),
    path('generate_word_template',views.generate_word_template, name='generate_word_template'),
    path('test_front', views.test_front, name='test_front'),
    path('test_buildCV', views.test_buildCV, name='test_buildCV'),
    
    
   
    

    
]