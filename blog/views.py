from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
#posts=[{'author':'aman','title':'Gla University','content':'Mathura','date_posted':'12-12-2015'},{'author':'aditya','title':'Gla University','content':'Delhi','date_posted':'12-11-2015'}]

# Create your views here.
def home(request):
    context={'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})


#blog ->templates