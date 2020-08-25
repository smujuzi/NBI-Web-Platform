from django.forms import ModelForm
from .models import NBI


class NBIForm(ModelForm):
    class Meta:
        model = NBI
        fields = '__all__'

