from webapp.views import IndexView, OrganizationCreateView, OrganizationDeleteView, OrganizationUpdateView,\
    OrganizationView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('organization/<int:pk>/', OrganizationView.as_view(), name='organization_detail'),
    path('organizations/add/', OrganizationCreateView.as_view(), name='organization_add'),
    path('organization/<int:pk>/delete', OrganizationDeleteView.as_view(), name="organization_delete"),
    path('organization/<int:pk>/edit', OrganizationUpdateView.as_view(), name="organization_edit"),
]