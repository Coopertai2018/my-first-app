from django import forms

from .models import Comments
from .models import Articles

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ( 'text',)

class ArticlesForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = ('title', 'text', 'type_of_article')
