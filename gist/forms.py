from django import forms
from .models import Gist

class GistForm(forms.ModelForm):
    title = forms.CharField(
            label='',
            widget=forms.TextInput(attrs={'placeholder': 'Filename including extension...', 'class': 'filename'})
    )
    text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Paste code here...', 'class': 'gist_code'})
    )

    class Meta:
        model = Gist
        fields = ('title', 'text')
