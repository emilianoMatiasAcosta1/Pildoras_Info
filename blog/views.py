from django.shortcuts import render
from blog.models import Blog

def blog(request):
    posteos = Blog.objects.all()
    context = {'posteos' : posteos }
    return render(request , 'blog/blog.html', context )

    
