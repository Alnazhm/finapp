from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import FinancialOrganization


class IndexView(ListView):
    template_name = 'index.html'
    model = FinancialOrganization
    context_object_name = 'organizations'
