from django.shortcuts import render, render_to_response
from blogs.models import BlogsPost

# Create your views here.

def blog_index(request):
    blog_list = BlogsPost.objects.all()
    return render(request, 'blog_index.html', {'blog_list':blog_list})

def default_index(request):
    return render(request, "index.html")

def charts_index(request):
    return render(request, template_name="charts.html")

def tables_index(request):
    return render(request, template_name="tables.html")

def login(request):
    return render(request, template_name="login.html")

def register(request):
    return render(request, template_name="register.html")

def blank(request):
    return render(request, template_name="blank.html")

def cards(request):
    return render(request, template_name="cards.html")

def forgot_password(request):
    return render(request, template_name="forgot-password.html")

def navbar(request):
    return render(request, template_name="navbar.html")
