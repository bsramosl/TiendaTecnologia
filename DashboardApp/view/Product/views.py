from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages


class ListProduct(ListView):
    template_name = 'Dashboard/Product/List.html'
    model = ProductModel

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['create'] = 'Dash:CreateProduct'
        context['update'] = 'Dash:UpdateProduct' 
        context['delete'] = 'Dash:DeleteProduct' 
        return context 

class CreateProduct(CreateView):
    template_name = 'Dashboard/Product/Create.html'
    model = ProductModel
    form_class = ProductForm
    success_url = reverse_lazy('Dash:ListProduct')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Product'
        context['list'] = 'Dash:ListProduct' 
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

class UpdateProduct(UpdateView):
    template_name = 'Dashboard/Product/Update.html'    
    model = ProductModel
    form_class = ProductForm
    success_url = reverse_lazy('Dash:ListProduct')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'EditProduct'
        context['list'] = 'Dash:ListProduct' 
        return context 
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha Actualizado con exito')
        return response

class DeleteProduct(DeleteView):
    template_name = 'Dashboard/Product/Delete.html'
    model = ProductModel
    success_url = reverse_lazy('Dash:ListProduct') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'Product'
        context['delete'] = 'Dash:DeleteProduct' 
        return context
