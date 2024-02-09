from django import forms
from .models import Comment
from tinymce.widgets import TinyMCE

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': TinyMCE(),
        }