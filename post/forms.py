from django import forms
from .models import postmodel ,Comment

class postmodelform(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = postmodel
        fields = ('title','content')
        
class postupdateform(forms.ModelForm):
    class Meta:
        model = postmodel
        fields = ('title','content')
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'laceholder': 'Add comment here....'}))

    class Meta:
        model = Comment
        fields = ('content',)