from .models import Fast
from django.forms import ModelForm, TextInput, DateInput, Textarea

class FastForm(ModelForm):
    class Meta:
        model = Fast
        fields = [
            'title',
            'anons',
            'text',
            'date',
            'buttonText',


        ]
        widgets = {
            'title': TextInput(attrs={
                'id' : 'form-title',
                'class': 'form-control',
                'placeholder': 'Название блога'
            }),
            'anons': TextInput(attrs={
                'id' : 'form-anons',
                'class': 'form-control',
                'placeholder': 'Анонс блога'
            }),
            'text': Textarea(attrs={
                'id' : 'form-text',

                'class': 'form-control',
                'placeholder': 'Текст блога'
            }),
            'date': DateInput(attrs={
                'id' : 'form-text',

                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),


        }