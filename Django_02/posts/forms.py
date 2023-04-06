from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    category_choices = [('개발', '개발'), ('CS', 'CS'), ('신기술', '신기술'),]
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '제목을 입력해주세요.'
        }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': '내용을 입력해주세요.',
            'style': 'height: 10em;',
        }
        )
    )
    category = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=category_choices)
    )
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')