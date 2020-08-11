from django.urls import path, include, re_path
from . import views


urlpatterns = [

    path('', views.index, name="index"),
    
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
    path('search/?q=marble/', views.filter, name='filter'),
    path('search/?q=plants/', views.filter2, name='filter2'),
    path('search/?q=geometric/', views.filter3, name='filter3'),
    path('product/', views.product, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/',views.updateItem, name='update_item'),
    path('process_order/',views.processOrder, name='process_order'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('product/<slug:slug>/', views.single, name='single'),
    path('register/', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),

]