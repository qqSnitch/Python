from django import forms
from .models import Agency, Employer, Contract

class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ['name','title','salary']

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'surname','email','phone']

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['employer', 'agency']