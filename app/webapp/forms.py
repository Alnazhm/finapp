from django import forms
from webapp.models import FinancialOrganization



class OrganizationForm(forms.ModelForm):
    class Meta:
        model = FinancialOrganization
        fields = ('organization', 'bin', 'org_logo')