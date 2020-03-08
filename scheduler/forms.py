from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from scheduler.models import *

class LoginForm(forms.Form):
    login = forms.CharField(label='login', max_length=64, required=False)
    password = forms.CharField(label='password', max_length=64,
                               widget=forms.PasswordInput)

class AddStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['staff_id']


class AddUnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'


class AddShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        exclude = ['shift_id']


class AddPartTimeForm(forms.ModelForm):
    class Meta:
        model = PartTime
        fields = '__all__'


class AddBaseTimeForm(forms.ModelForm):
    class Meta:
        model = BaseTime
        fields = '__all__'

class AddYearScheduleForm(forms.ModelForm):
    class Meta:
        model = YearSchedule
        exclude = ['yearschedule_id']

class FillScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
