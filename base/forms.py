from django import forms

class DonwloadForm(forms.Form):
    url = forms.URLField(label='YouTube Video URL', widget=forms.URLInput(attrs={
        'class': 'form-input mt-1 block w-full',
        'placeholder': 'Enter YouTube URL here...'
    }))
