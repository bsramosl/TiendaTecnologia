from django.db import models
from Store.settings import MEDIA_URL,STATIC_URL
from datetime import datetime    
from django.forms import model_to_dict 
from django.contrib.auth.models import User


class BusinessModel(models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombre',unique=True)
    phone = models.IntegerField(verbose_name='Celular',null=True,blank=True)
    email = models.EmailField(verbose_name='Correo Electronico',null=True,blank=True)
    logo = models.ImageField(upload_to='logo/%Y/%m/%d',blank=True,null=True)
    address = models.CharField(max_length=100,verbose_name='Direccion')
    
    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self) 
        item['logo'] = self.get_logo()
        return item

    def get_logo(self):
        if self.logo:
             return '{}{}'.format(MEDIA_URL,self.logo)
        return '{}{}'.format (MEDIA_URL,'CAM.PNG')

    class Meta:
        verbose_name = 'Business'
        verbose_name_plural = 'Business'
        ordering = ['id']


class CategoryModel(models.Model):
    name = models.CharField(max_length=50,verbose_name='Nombre')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)       
        return item    

    class Meta:
        verbose_name ='Category'
        verbose_name_plural = 'Categorys'
        ordering = ['id']


class ProductModel(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,verbose_name='Categoria')
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(verbose_name='Precio')
    image = models.ImageField('Imagen1',upload_to='img/',blank=True, null=True)
    image2 = models.ImageField('Imagen2',upload_to='img/',blank=True, null=True)
    image3 = models.ImageField('Imagen3',upload_to='img/',blank=True, null=True)
    stock = models.IntegerField(verbose_name=('Stock'))
    discount = models.IntegerField(verbose_name=('Offer'),blank=True, null=True)
    date_creation = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering =['name']
    
    def __str__(self):
        return self.name
        

    def toJSON(self):
        item = model_to_dict(self) 
        item['category'] = self.category.toJSON()
        item['image'] = self.get_image()
        item['image2'] = self.get_image2()
        item['image3'] = self.get_image3()
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL,self.image)
        return '{}{}'.format (MEDIA_URL,'CAM.PNG')

    def get_image2(self):
        if self.image2:
            return '{}{}'.format(MEDIA_URL,self.image2)
        return '{}{}'.format (MEDIA_URL,'CAM.PNG')

    def get_image3(self):
        if self.image3:
            return '{}{}'.format(MEDIA_URL,self.image3)
        return '{}{}'.format (MEDIA_URL,'CAM.PNG')


class CartModel(models.Model):   
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,verbose_name = ('Producto'))
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = ('Usuario'))
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,verbose_name = ('Precio'))
    cant = models.IntegerField(default=0,verbose_name = ('Cantidad'))
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,verbose_name = ('Subtotal'))

    def __str__(self):
        return self.product.name
    
    def toJSON(self):
        item = model_to_dict(self) 
        item['product'] = self.product.toJSON()
        return item

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['id']

