from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAppItem

def user_info(request):
    all_userapp_items = UserAppItem.objects.all()
    return render(request, 'UserInfo.html', {'all_items': all_userapp_items})
