from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profilemodel
from django import forms 

class signupform(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(signupform, self).__init__(*args, **kwargs)
        
        for fieldname in ['username' , 'email' , 'password1', 'password2']:
            self.fields[fieldname].help_text=None


class userupdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'email' ]
        
    def __init__(self, *args, **kwargs):
        super(userupdateform, self).__init__(*args, **kwargs)
        
        for fieldname in ['username' , 'email']:
            self.fields[fieldname].help_text=None
        
class profileupdateform(forms.ModelForm):
    class Meta:
        model = profilemodel
        fields = ['image']