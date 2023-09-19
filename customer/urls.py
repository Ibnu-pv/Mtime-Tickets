from django.urls import path
from .views import *



urlpatterns = [
    path('cust',Custhome.as_view(),name="cust"),
    path('dtls/<int:id>',MovieDetail.as_view(),name="mvdt"),
    path('th/<int:id>',TheaterListView.as_view(),name="tl"),
    path('book',BookingsView.as_view(),name="book"),
    path('py/<int:id>/',PaymentView.as_view(),name="py"),
    path('cnc/<int:id>',cancelbooking,name="cncl")
    
    
    
    
    
]    