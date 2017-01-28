from django import forms

from .models import Changes, CIR

class ChangeForm(forms.ModelForm):
    class Meta:
        model = Changes
        fields = (
            'name_of_change',
            'BRS_num',
            'author',
            'author_email_address',
            'contact',
            'summary',
            'delivery_date',
            'channels',
            'brands',
            'business_area',
            'allocated',
            'point',
            'status',
        )

class CirForm(forms.ModelForm):
    class Meta:
        model = CIR
        fields = (
            'name_of_change',
            'author',
            'author_email_address',
            'contact',
            'summary',
            'delivery_date',
            'channels',
            'brands',
            'business_area',
            'allocated_to',
            'allocated',
            'point',
        )
