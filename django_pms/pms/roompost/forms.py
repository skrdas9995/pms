from django import forms
from roompost.models import DoctorDetails

class DoctorDetailsForm(forms.ModelForm):

    class Meta:
        model = DoctorDetails
        fields = ('__all__')
