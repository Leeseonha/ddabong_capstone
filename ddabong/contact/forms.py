from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = ['post_type', 'title', 'b_type', 'body', 'region']

        help_texts = {
            'post_type': None,
            'title': None,
            'b_type': None,
            'body': None,
            'region': None,
        }