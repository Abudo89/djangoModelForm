from django import forms
from djangoModelForm.models import HpStudents


class WanafunziForm(forms.ModelForm):
    class Meta:
        model = HpStudents
        fields = '__all__'
