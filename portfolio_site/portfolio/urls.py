from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('greet/<str:name>/', views.greet_by_name, name='greet')
]