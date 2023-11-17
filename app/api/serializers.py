from rest_framework import serializers
from webapp.models import FinancialOrganization




class FinancialOrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinancialOrganization
        fields = ('__all__')
