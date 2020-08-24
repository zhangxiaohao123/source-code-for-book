from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    # widgets = {
    #     "name": forms.widgets.TextInput(attrs={'class': 'form-control'}),
    #     "email":forms.widgets.EmailInput(attrs={'class': 'form-control'}),
    #     "url": forms.widgets.URLInput(attrs={'class': 'form-control'}),
    #     "text":forms.widgets.Textarea(attrs={'class': 'form-control'})
    # }

