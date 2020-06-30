from django import forms 
from .models import Article,Comment

class AddArticle(forms.ModelForm):
    
    class Meta:
        model=Article
        fields=['title','content','article_image']


