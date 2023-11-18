from .models import Post
from django.shortcuts import render
def index(request):
    posts = Post.objects.all()

    return render(request, 'index/index.html', {'posts':posts})