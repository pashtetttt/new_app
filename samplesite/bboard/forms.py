from django.forms import ModelForm

from .models import Bb


# Создание класса формы, в мета класс заноситься модель для формы!
# и поля, которые там будут
class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
