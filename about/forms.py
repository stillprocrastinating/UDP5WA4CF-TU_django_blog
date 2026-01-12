from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    '''
    Docstring for CollaborateForm
    '''

    class Meta:
        '''
        Docstring for Meta
        '''
        
        model = CollaborateRequest
        fields = ('name', 'email', 'message',)
