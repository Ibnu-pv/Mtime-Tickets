from django.urls import path
from .views import *

urlpatterns = [
    path('re',Regview.as_view(),name="reg"),
    path('lg',Logout.as_view(),name="log")
    
    
    
]    