from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    posts = Post.objects.all()
    context ={
        
        'posts': posts}
    
        
    return render(request, 'index.html', context)

def gallerey(request):
    return render(request, 'pages/gallerey.html')