from django.db import models

# Create your models here.
class StudentUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password= models.CharField(max_length=10,default=True)
    confirm_password= models.CharField(max_length=10,default=True)

    def __str__(self):
        return self.name
    
class PDFFile(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdf_files/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class PersonalInformationQuestionResponse(models.Model):
    question_1 = models.TextField()
    question_2 = models.TextField()
    question_3 = models.TextField()
    question_4 = models.TextField()
    question_5 = models.TextField()
    
    def __str__(self):
            return self.question_1
        
        
class ProfessionalSummaryQuestionResponse(models.Model):
    question_6 = models.TextField()
    question_7 = models.TextField()
    question_8 = models.TextField()
    
    def __str__(self):
            return self.question_6
        
        
class WorkExperienceQuestionResponse(models.Model):
    question_9 = models.TextField()
    question_10 = models.TextField()
    question_11 = models.TextField()
    question_12 = models.TextField()
    question_13 = models.TextField()
    question_14 = models.TextField()
    
    def __str__(self):
            return self.question_9
        
class TechnicalSkillsQuestionResponse(models.Model):
    question_15 = models.TextField()
    question_16 = models.TextField()
    question_17 = models.TextField()
    
    
    def __str__(self):
        return self.question_15
    
class CertificationsQuestionsResponse(models.Model):
    question_18 = models.TextField()
    question_19 = models.TextField()
    
    def __str__(self):
        return self.question_18
    

class EducationQuestionResponse(models.Model):
    
    question_20 = models.TextField()
    question_21 = models.TextField()
    
    def __str__(self):
        return self.question_20
    
    