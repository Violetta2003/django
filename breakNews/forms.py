from breakNews.models import News
from django.forms import ModelForm, TextInput, Textarea, DateInput, Select


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'news', 'imgURL', 'date', 'category', 'user']

        widgets = {
            "title": TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Заголовок'
            }),
            "news": Textarea(attrs={
                'class': 'input-field',
                'placeholder': 'Новость'
            }),
            "imgURL": TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'URL картинки'
            }),
            "date": DateInput(attrs={
                'class': 'input-field',
                'type': 'date'
            }),
            "category": Select(attrs={
                'class': 'input-field'
            }),
            "user": Select(attrs={
                'class': 'input-field'
            })
        }