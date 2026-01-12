from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''
    Docstring for CommentForm
    '''

    class Meta:
        '''
        Docstring for Meta
        '''
        
        model = Comment
        fields = ('body',)
