from django import forms
from .models import Apply, Job


class ApplyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        self.fields['website'].label = "LinkedIn"
        
    class Meta:
        model = Apply
        fields = ['first_name', 'email', 'website', 'cv', 'cover_letter']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug', 'owner')
