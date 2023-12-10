from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    student_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                               'class': 'form-control',
                                                               }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['student_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    email = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class PDFUploadForm(forms.Form):
    title = forms.CharField(max_length=255)
    pdf_file = forms.FileField()

class PersonalInformationQuestionForm(forms.Form):
    question_1 = forms.CharField(
        label='1. Full Name : ',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_2 = forms.CharField(
        label='2. Contact Information (Phone number, Email):',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_3 = forms.CharField(
        label='3. LinkedIn Profile URL',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    question_4 = forms.CharField(
        label='4. Availability: i.e. immediately, 2 weeks notice etc.',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    question_5 = forms.CharField(
        label='5. Location Preference: Nationwide',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    
class ProfessionalSummaryQuestionForm(forms.Form):
    question_6 = forms.CharField(
        label='1. How would you describe your professional background in one or two sentences, stating how many years’ experiences you have, the type of high-level tasks you have completed and which industries you have worked in ? ',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_7 = forms.CharField(
        label='2. What tools have you used which are related to business analysis?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_8 = forms.CharField(
        label='3. What tangible achievement have you achieved. i.e. how have you helped a company make money, save money or save time?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    
class WorkExperienceQuestionForm(forms.Form):
    question_9 = forms.CharField(
        label='1. What is your current or most recent job title? ',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_10 = forms.CharField(
        label='2. Can you list your previous job titles and the companies you worked for?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_11 = forms.CharField(
        label='3. Describe any projects where you used analytical or problem-solving skills.',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    question_12 = forms.CharField(
        label='4. Have you ever been in a role that required data analysis or interpretation?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    question_13 = forms.CharField(
        label='5. Can you provide examples of when you had to analyze a process and make recommendations for improvements?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    question_14 = forms.CharField(
        label='6. Have you been a part of any major changes in your previous work place?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    
class TechnicalSkillsQuestionForm(forms.Form):
    question_15 = forms.CharField(
        label='1. Are you familiar with any business analysis tools (e.g., Excel, SQL, Jira, confluence, basecamp, Visio, draw.io, balsamiq cloud)? ',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_16 = forms.CharField(
        label='2. Have you used any project management tools (e.g., JIRA, Trello, Asana)?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_17 = forms.CharField(
        label='3. Do you have experience with any business intelligence software (e.g., Tableau, Power BI)?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )
    
    
class CertificationsQuestionForm(forms.Form):
    question_18 = forms.CharField(
        label='1. Do you hold any certifications that are relevant to business analysis? ',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_19 = forms.CharField(
        label='2. Have you attended any workshops, seminars, or other training sessions related to business or analysis?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )


class EducationQuestionForm(forms.Form):
    question_20 = forms.CharField(
        label='1. What is your highest level of education? ',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    question_21 = forms.CharField(
        label='2. What were your major areas of study?',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True,
    )

    