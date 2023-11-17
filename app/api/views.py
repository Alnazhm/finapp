from rest_framework import generics
from api.serializers import FinancialOrganizationSerializer
from webapp.models import FinancialOrganization


class FinancialOrganizationList(generics.ListCreateAPIView):
    serializer_class = FinancialOrganizationSerializer

    def get_queryset(self):
        queryset = FinancialOrganization.objects.all()
        return queryset

class FinancialOrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FinancialOrganizationSerializer
    queryset = FinancialOrganization.objects.all()







