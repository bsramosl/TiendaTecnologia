from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from PrincipalApp.forms import *



class ListUser(ListView):
    template_name = 'Dashboard/User/List.html'
    model = User

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['create'] = 'Dash:CreateUser'
        context['update'] = 'Dash:UpdateUser' 
        context['delete'] = 'Dash:DeleteUser' 
        return context 

class CreateUser(CreateView):
    template_name = 'Dashboard/User/Create.html'
    model = User
    form_class = UsuarioForm
    success_url = reverse_lazy('Dash:ListUser')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'User'
        context['list'] = 'Dash:ListUser' 
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

class UpdateUser(UpdateView):
    template_name = 'Dashboard/User/Update.html'    
    model = User
    form_class = UsuarioForm
    success_url = reverse_lazy('Dash:ListUser')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'EditUser'
        context['list'] = 'Dash:ListUser' 
        return context 
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha Actualizado con exito')
        return response

class DeleteUser(DeleteView):
    template_name = 'Dashboard/User/Delete.html'
    model = User
    success_url = reverse_lazy('Dash:ListUser') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtitle'] = 'User'
        context['delete'] = 'Dash:DeleteUser' 
        return context
