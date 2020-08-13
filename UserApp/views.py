from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UserItem


def user_info(request):
    all_user_items = UserItem.objects.all()
    return render(request, 'UserInfo.html', {'all_items': all_user_items})


def add_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    item = UserItem(username=username, password=password, email=email)
    item.save()
    return HttpResponseRedirect('/userInfo/')


def delete_user(request, user_id):
    item = UserItem.objects.get(id=user_id)
    item.delete()
    return HttpResponseRedirect('/userInfo/')
