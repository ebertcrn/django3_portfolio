from django.urls import path
from . import views

app_name = 'pwgenerator'

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
    path('error/', views.password, name='passworderror')
]