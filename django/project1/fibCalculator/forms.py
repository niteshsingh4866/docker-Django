from django import forms
from .models import Post


class FibForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('number', 'result')
