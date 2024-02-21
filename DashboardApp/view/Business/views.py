from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages


class ListBusiness(ListView):
    template_name = 'Dashboard/Business/List.html'
    model = BusinessModel

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['create'] = 'Dash:CreateBusiness'
        context['update'] = 'Dash:UpdateBusiness' 
        context['delete'] = 'Dash:DeleteBusiness' 
        return context 

class CreateBusiness(CreateView):
    template_name = 'Dashboard/Business/Create.html'
    model = BusinessModel
    form_class = BusinessForm
    success_url = reverse_lazy('Dash:ListBusiness')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Business'
        context['list'] = 'Dash:ListBusiness' 
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

class UpdateBusiness(UpdateView):
    template_name = 'Dashboard/Business/Update.html'    
    model = BusinessModel
    form_class = BusinessForm
    success_url = reverse_lazy('Dash:ListBusiness')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'EditBusiness'
        context['list'] = 'Dash:ListBusiness' 
        return context 
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha Actualizado con exito')
        return response

class DeleteBusiness(DeleteView):
    template_name = 'Dashboard/Business/Delete.html'
    model = BusinessModel
    success_url = reverse_lazy('Dash:ListBusiness') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Business'
        context['delete'] = 'Dash:DeleteBusiness' 
        return context
