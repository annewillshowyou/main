from django.forms import ModelForm

from .models import Bb

class BbForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rubric'].empty_label = "Категория не выбрана"
        
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')