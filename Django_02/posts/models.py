from django.db import models
from django.forms import ModelForm


class Post(models.Model):
    category_choices = [('개발', '개발'), ('CS', 'CS'), ('신기술', '신기술'),]
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
    category = models.CharField(max_length=3, choices=category_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
