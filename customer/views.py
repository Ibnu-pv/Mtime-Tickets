from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,ListView,FormView,CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# Create your views here.

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please Login first!!")
            return redirect("h")
    return inner  
desc=[never_cache,signin_required] 

@method_decorator(desc,name='dispatch')

class Custhome(ListView):
    template_name="Chome.html"
    queryset=Movies.objects.all()
    context_object_name="Movies"
    
    
@method_decorator(desc,name='dispatch')
    
class MovieDetail(DetailView):
    template_name="moviedetail.html"
    pk_url_kwarg="id"    
    queryset=Movies.objects.all()
    context_object_name="details"  
 
 
@method_decorator(desc,name='dispatch')
    
class TheaterListView(ListView):
    template_name="theaters.html" 
    queryset=Theaters.objects.all()
    context_object_name="Theaters"
    
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        mov = Movies.objects.get(id=id)
        user = request.user
        theater = Theaters.objects.create(movie=mov, user=user) 
        theater.save()
        return redirect('tl')
    

@method_decorator(desc,name='dispatch')

class PaymentView(TemplateView):
    template_name = "payment.html"

    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        id = kwargs.get("id")
        movie= Movies.objects.get(id=id)
        theater = Theaters.objects.get(id=id)
        user = request.user
        phone = request.POST.get("phn")
        show = request.POST.get("stm")
        seat = request.POST.get("st")
        date = request.POST.get("dt")
       

        Books.objects.create(theater=theater,user=user,phone=phone,show=show,movie=movie,seat=seat,date=date)
        movie.save()
        theater.save()
        messages.success(request,"Booking successful ")
        

        return redirect("book")
    

@method_decorator(desc,name='dispatch')
    
class BookingsView(ListView):
    template_name="bookings.html"
    queryset=Books.objects.all()
    context_object_name="book"
    
    def get_queryset(self):
        return Books.objects.filter(user=self.request.user)
    
    
desc    
def cancelbooking(request,*args,**kwargs):
    oid=kwargs.get("id")
    book=Books.objects.get(id=oid)
    book.status='Cancelled'
    book.save()
    messages.success(request,"Booking cancelled")    
    return redirect('book')
      
         
        
    
       
    

