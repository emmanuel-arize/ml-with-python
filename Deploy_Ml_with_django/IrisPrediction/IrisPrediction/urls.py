"""
Definition of urls for IrisPrediction.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin

from app import  views


urlpatterns = [
    path('', views.home, name='home'),
    path('SpeciesPrediction',views.SpeciesPrediction,name='SpeciesPrediction'),
   
    path('admin/', admin.site.urls),
]
