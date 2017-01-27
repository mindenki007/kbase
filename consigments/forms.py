from django import forms

from .models import Consigments, Areas

class ConsigmentForm(forms.ModelForm):
    class Meta:
        model = Consigments
        fields = (
            'letter_code',
            'letter_BG',
            'letter_SG',
            'letter_SE',
            'email_BG',
            'email_SE',
            'business_area',
            'application',
            'journey',
            'vi',
            'environment',
            'comments',
            )

class FilterAreaForm(forms.Form):
    areas = forms.ModelChoiceField(queryset=Areas.objects.all(), required=False)
