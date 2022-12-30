from django.urls import path 
from app1.views import *

app_name='prabhas'

urlpatterns=[
    path('bahubali/',bahubali,name='bahubali'),
]