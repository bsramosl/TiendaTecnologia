from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from PrincipalApp.forms import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import transaction
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
import json
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView
from PrincipalApp.Carrito import Carrito 


@method_decorator(csrf_exempt)
def modales(request): 
     data = {}
     try: 
        action = request.POST['action']
        if action == 'view':
            data = []
            view = ProductModel.objects.filter( id = request.POST['id'])
            for i in view:
                    item = i.toJSON()
                    data.append(item)     
        else:                   
                data['error'] = 'No ha ingresado a ninguna opción'
     except Exception as e: 
        data['error'] = str(e)
     return JsonResponse(data,safe=False)


@method_decorator(csrf_exempt)
def inicio_major(request):
    
     data = {}
     try: 
        action = request.POST['action']
        if action == 'cargar':
            data = []
            prods = BusinessModel.objects.all()
            for i in prods:
                    item = i.toJSON()
                    item['value']= i.name
                    data.append(item)    
            cat = CategoryModel.objects.all()
            for j in cat:
                    cate = j.toJSON() 
                    data.append(cate)                 
        else:                   
                data['error'] = 'No ha ingresado a ninguna opción'
     except Exception as e: 
        data['error'] = str(e)
     return JsonResponse(data,safe=False)

@method_decorator(csrf_exempt)
def cart(request):
    data = {}
    try:
        action = request.POST['action']
        if action == 'add':
            carrito = Carrito(request)
            producto = ProductModel.objects.get(id=request.POST['id'])
            carrito.agregar(producto)  
            data['success'] = 'registrado'
        else:
            if action == 'delete':
                  carrito = Carrito(request)
                  producto = ProductModel.objects.get(id=request.POST['id'])
                  carrito.eliminar(producto)
            else:
                if action == 'restar':
                  carrito = Carrito(request)
                  producto = ProductModel.objects.get(id=request.POST['id'])
                  carrito.restar(producto)
                else:
                    data['error'] = 'No ha ingresado a ninguna opción'
    except Exception as e: 
        data['error'] = str(e)
    return JsonResponse(data,safe=False) 

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")


@method_decorator(csrf_exempt)
def refresh_cart(request):
    data = {}
    try:
        data = []
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                item = value 
                data.append(item) 
        else:                   
            data['error'] = 'No ha ingresado a ninguna opción'
    except Exception as e:  
        data['error'] = str(e)
    return JsonResponse(data, safe=False)

 

class InicioView(TemplateView):
    template_name = 'Major/Index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['recently'] = ProductModel.objects.order_by('-date_creation')[:6]
        context['price'] = ProductModel.objects.order_by('-price')[:5]
        return context


class ProductDetail(DetailView):
    model = ProductModel
    template_name = 'Major/DetailProduct.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['recently'] = ProductModel.objects.order_by('-date_creation')[:5]           
        return context

class RegisterUser(CreateView):
    template_name = 'Major/RegisterUser.html'
    form_class = UsuarioForm    
    success_url = reverse_lazy('Store:Inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Usuario'
        return context

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response

class Login(FormView):
    template_name = 'Major/Login.html'
    form_class = LoginForm
    success_url = reverse_lazy('Store:Inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'Bienvenido')
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))


class Logout(RedirectView):
    pattern_name = 'Store:Inicio'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    

class MyAccount(TemplateView):
    template_name = 'Major/MyAccount.html'

    
 
class ShoppingCart(TemplateView):
    template_name = 'Major/ShoppingCart.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self , request, *args,**kwargs):
        data = {}
        try: 
            action = request.POST['action']
            data = []
            if action == 'cargar':
                if "carrito" in request.session.keys():
                     for key, value in request.session["carrito"].items():
                         item = value 
                         data.append(item) 
            else:                   
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:             
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class ContactUs(TemplateView):
     template_name = 'Major/ContactUs.html'

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business'] = BusinessModel.objects.all()
        return context
     
class Shop(TemplateView):
    template_name = 'Major/Shop.html' 

    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

    def post(self , request, *args,**kwargs):
        data = {}        
        try:
            action = request.POST['action']           
            if action == 'cargar':
                data = []
                for i in ProductModel.objects.all():
                    item = i.toJSON()
                    data.append(item)                    
            else:               
                if action == 'filter': 
                    data = []
                    category = request.POST.getlist("category[]")
                    search = request.POST.get("search") 
                    if category and search:
                        for i in ProductModel.objects.filter(category__in = category).filter(name__contains = search):
                            item = i.toJSON()
                            data.append(item)
                    else: 
                        if category:
                            for i in ProductModel.objects.filter(category__in = category):
                                item = i.toJSON()
                                data.append(item)    
                        else:
                            if search: 
                                for i in ProductModel.objects.filter(name__contains = search):
                                    item = i.toJSON()
                                    data.append(item)            
                else:
                    data['error'] = 'Ha ocurrido un error'              
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()
        return context
    

@method_decorator(csrf_exempt)
def Search(request):
    search = request.POST['searching']
    item = ProductModel.objects.filter(name__contains = search)
    if item:
        return render(request, 'Major/Search.html',{'search':search,'item': item})
    else:
        return redirect( 'Store:Inicio')
      

    
    
    