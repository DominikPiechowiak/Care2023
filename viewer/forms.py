from django.forms import (ModelForm, CharField, IntegerField)
from viewer.models import Advertisement

class AdForm(ModelForm):

    class Meta:
        model = Advertisement
        fields = '__all__'

    user = CharField(empty_value="Zalogowany użytkownik")
    age = IntegerField(min_value=1, max_value=120)
    experience = IntegerField(min_value=0, max_value=50)
