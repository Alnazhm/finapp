from django.urls import path, include
from .views import FinancialOrganizationList, FinancialOrganizationDetail



urlpatterns = [
    path('organization/', FinancialOrganizationList.as_view()),
    path('organization/<int:pk>/', FinancialOrganizationDetail.as_view()),
    
]






