from django.forms import (ModelForm, CharField, DateField, IntegerField)
from viewer.models import Advertisement
from accounts.models import CustomUser

from datetime import datetime

class AdForm(ModelForm):

    class Meta:
        model = Advertisement
        fields = '__all__'


    #user_id = IntegerField(initial=CustomUser.id)
    age = IntegerField(min_value=1, max_value=120)
    experience = IntegerField(min_value=0, max_value=50)
    pub_date = DateField(initial=datetime.today())
