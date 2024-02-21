from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from DashboardApp.models import *
from DashboardApp.forms import *
import json
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

class InicioView(TemplateView):
    template_name = 'Layouts/IndexDashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)         
        return context
  
  
@method_decorator(csrf_exempt)
def inicio_dashboard(request):
    
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
        else:                   
                data['error'] = 'No ha ingresado a ninguna opción'
     except Exception as e: 
        data['error'] = str(e)
     return JsonResponse(data, safe=False)
