from django.urls import path 
from app2.views import *

app_name='mama'

urlpatterns=[
    path("kattappa/",kattappa,name='kattappa'),
]