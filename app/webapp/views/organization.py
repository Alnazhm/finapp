from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import FinancialOrganization
from webapp.forms import OrganizationForm



class IndexView(ListView):
    template_name = 'index.html'
    model = FinancialOrganization
    context_object_name = 'organizations'
    ordering = '-created_at'


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add_organization.html'
    form_class = OrganizationForm
    model = FinancialOrganization



    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.responsible = self.request.user
            form.save()
            print("AUTHOR ",form.instance.responsible)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy('index')


class OrganizationView(DetailView):
    template_name = 'organization_detail.html'
    model = FinancialOrganization
    context_object_name = 'organization'
    
    def get(self, request, *args, **kwargs):
        # You can add custom logic here if needed
        return super().get(request, *args, **kwargs)

    


class OrganizationUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'organization_edit.html'
    form_class = OrganizationForm
    model = FinancialOrganization
    context_object_name = 'organization'
    permission_required = 'webapp.change_financialorganization'

    def has_permission(self) -> bool:
        return super().has_permission() or self.get_object().responsible == self.request.user or self.get_object().responsible.role == 2

    
    def get_success_url(self):
        return reverse('organization_detail', kwargs={'pk': self.object.pk})


class OrganizationDeleteView(PermissionRequiredMixin, DeleteView):
    model = FinancialOrganization
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_financialorganization'

    def has_permission(self) -> bool:
        return super().has_permission() or self.get_object().responsible.role == 2






