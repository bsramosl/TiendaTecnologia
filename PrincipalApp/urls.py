from django.urls import path
from PrincipalApp import views 
from django.contrib.auth.decorators import login_required 


app_name = 'Store'
urlpatterns = [
    
    path('modales/',views.modales,name='modales'), 

    path('inicio_major/',views.inicio_major,name='inicio_major'),  
    path('refresh_cart/',views.refresh_cart,name='refresh_cart'),
   

    path('cart/', views.cart, name='cart'), 
  
    path('limpiar/', views.limpiar_carrito, name="CLS"),

    path('',views.InicioView.as_view(),name='Inicio'),   
    path('ProductDetail/<int:pk>/',views.ProductDetail.as_view(),name='ProductDetail'),   
    path('RegisterUser/',views.RegisterUser.as_view(),name='RegisterUser'),   
    path('Login/',views.Login.as_view(),name='Login'),   
    path('Logout/',views.Logout.as_view(),name='Logout'),  
    path('MyAccount/',views.MyAccount.as_view(),name='MyAccount'),   
 
    path('ShoppingCart/',views.ShoppingCart.as_view(),name='ShoppingCart'),      

    path('ContactUs/',views.ContactUs.as_view(),name='ContactUs'), 

    path('Shop/',views.Shop.as_view(),name='Shop'), 

    path('Search/',views.Search,name='Search'),    
]