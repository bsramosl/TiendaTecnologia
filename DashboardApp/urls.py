from django.urls import path
from DashboardApp import views 
from django.contrib.auth.decorators import login_required
from DashboardApp.view.Product.views import *
from DashboardApp.view.Category.views import *
from DashboardApp.view.User.views import *
from DashboardApp.view.Business.views import *

 


app_name = 'Dash'
urlpatterns = [

    path('inicio_dashboard/',views.inicio_dashboard,name='inicio_dashboard'), 

    path('Dashboard/',views.InicioView.as_view(),name='Dashboard'),    
    path('ListProduct/',ListProduct.as_view(),name='ListProduct'),
    path('CreateProduct/',CreateProduct.as_view(),name='CreateProduct'),
    path('UpdateProduct/<int:pk>/',UpdateProduct.as_view(),name='UpdateProduct'),
    path('DeleteProduct/<int:pk>/',DeleteProduct.as_view(),name='DeleteProduct'), 

    path('ListCategory/',ListCategory.as_view(),name='ListCategory'),
    path('CreateCategory/',CreateCategory.as_view(),name='CreateCategory'),
    path('UpdateCategory/<int:pk>/',UpdateCategory.as_view(),name='UpdateCategory'),
    path('DeleteCategory/<int:pk>/',DeleteCategory.as_view(),name='DeleteCategory'), 

    path('ListUser/',ListUser.as_view(),name='ListUser'),
    path('CreateUser/',CreateUser.as_view(),name='CreateUser'),
    path('UpdateUser/<int:pk>/',UpdateUser.as_view(),name='UpdateUser'),
    path('DeleteUser/<int:pk>/',DeleteUser.as_view(),name='DeleteUser'), 

    path('ListBusiness/',ListBusiness.as_view(),name='ListBusiness'),
    path('CreateBusiness/',CreateBusiness.as_view(),name='CreateBusiness'),
    path('UpdateBusiness/<int:pk>/',UpdateBusiness.as_view(),name='UpdateBusiness'),
    path('DeleteBusiness/<int:pk>/',DeleteBusiness.as_view(),name='DeleteBusiness'), 

    

    
    
]