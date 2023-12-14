from django import forms
from .models import PersonalInformationQuestionResponse, ProfessionalSummaryQuestionResponse, WorkExperienceQuestionResponse, TechnicalSkillsQuestionResponse, CertificationsQuestionsResponse, EducationQuestionResponse

class PDFUploadForm(forms.Form):
    title = forms.CharField(max_length=255)
    pdf_file = forms.FileField()

class Page1Form(forms.ModelForm):
    class Meta:
        model = PersonalInformationQuestionResponse
        fields = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5']
        widgets = {
            'question_1': forms.Textarea(attrs={'rows': 4}),
            'question_2': forms.Textarea(attrs={'rows': 4}),
            'question_3': forms.Textarea(attrs={'rows': 4}),
            'question_4': forms.Textarea(attrs={'rows': 4}),
            'question_5': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(Page1Form, self).__init__(*args, **kwargs)
        self.fields['question_1'].label = '1. Full Name :'
        self.fields['question_2'].label = '2. Contact Information (Phone number, Email):'
        self.fields['question_3'].label = '3. LinkedIn Profile URL'
        self.fields['question_4'].label = '4. Availability: i.e. immediately, 2 weeks notice etc.'
        self.fields['question_5'].label = '5. Location Preference: Nationwide'

class Page2Form(forms.ModelForm):
    class Meta:
        model = ProfessionalSummaryQuestionResponse
        fields = ['question_6', 'question_7', 'question_8']
        widgets = {
            'question_6': forms.Textarea(attrs={'rows': 4}),
            'question_7': forms.Textarea(attrs={'rows': 4}),
            'question_8': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(Page2Form, self).__init__(*args, **kwargs)
        self.fields['question_6'].label = '1. How would you describe your professional background in one or two sentences, stating how many years’ experiences you have, the type of high-level tasks you have completed and which industries you have worked in ?'
        self.fields['question_7'].label = '2. What tools have you used which are related to business analysis?'
        self.fields['question_8'].label = '3. What tangible achievement have you achieved. i.e. how have you helped a company make money, save money or save time?'


class Page3Form(forms.ModelForm):
    class Meta:
        model = WorkExperienceQuestionResponse
        fields = ['question_9', 'question_10', 'question_11', 'question_12', 'question_13', 'question_14']
        widgets = {
            'question_9': forms.Textarea(attrs={'rows': 4}),
            'question_10': forms.Textarea(attrs={'rows': 4}),
            'question_11': forms.Textarea(attrs={'rows': 4}),
            'question_12': forms.Textarea(attrs={'rows': 4}),
            'question_13': forms.Textarea(attrs={'rows': 4}),
            'question_14': forms.Textarea(attrs={'rows': 4}),
            
        }

    def __init__(self, *args, **kwargs):
        super(Page3Form, self).__init__(*args, **kwargs)
        self.fields['question_9'].label = '1. What is your current or most recent job title?'
        self.fields['question_10'].label = '2. Can you list your previous job titles and the companies you worked for?'
        self.fields['question_11'].label = '3. Describe any projects where you used analytical or problem-solving skills.'
        self.fields['question_12'].label = '4. Have you ever been in a role that required data analysis or interpretation?'
        self.fields['question_13'].label = '5. Can you provide examples of when you had to analyze a process and make recommendations for improvements?'
        self.fields['question_14'].label = '6. Have you been a part of any major changes in your previous work place?'
        
        
class Page4Form(forms.ModelForm):
    class Meta:
        model = TechnicalSkillsQuestionResponse
        fields = ['question_15', 'question_16', 'question_17']
        widgets = {
            'question_15': forms.Textarea(attrs={'rows': 4}),
            'question_16': forms.Textarea(attrs={'rows': 4}),
            'question_17': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(Page4Form, self).__init__(*args, **kwargs)
        self.fields['question_15'].label = '1. Are you familiar with any business analysis tools (e.g., Excel, SQL, Jira, confluence, basecamp, Visio, draw.io, balsamiq cloud)?'
        self.fields['question_16'].label = '2. Have you used any project management tools (e.g., JIRA, Trello, Asana)?'
        self.fields['question_17'].label = '3. Do you have experience with any business intelligence software (e.g., Tableau, Power BI)?'


class Page5Form(forms.ModelForm):
    class Meta:
        model = CertificationsQuestionsResponse
        fields = ['question_18', 'question_19']
        widgets = {
            'question_18': forms.Textarea(attrs={'rows': 4}),
            'question_19': forms.Textarea(attrs={'rows': 4}),

        }

    def __init__(self, *args, **kwargs):
        super(Page5Form, self).__init__(*args, **kwargs)
        self.fields['question_18'].label = '1. Do you hold any certifications that are relevant to business analysis?'
        self.fields['question_19'].label = '2. Have you attended any workshops, seminars, or other training sessions related to business or analysis?'
        


class Page6Form(forms.ModelForm):
    class Meta:
        model = EducationQuestionResponse
        fields = ['question_20', 'question_21']
        widgets = {
            'question_20': forms.Textarea(attrs={'rows': 4}),
            'question_21': forms.Textarea(attrs={'rows': 4}),

        }

    def __init__(self, *args, **kwargs):
        super(Page6Form, self).__init__(*args, **kwargs)
        self.fields['question_20'].label = '1. What is your highest level of education?'
        self.fields['question_21'].label = '2. What were your major areas of study?'
        


