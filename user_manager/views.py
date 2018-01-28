from django.shortcuts import render
from user_manager.models import MenuParam

# Create your views here.

def user_getall(request):
    user_list = MenuParam.objects.all()
    return render(request, "menu_tables.html", {"user_list":user_list})
