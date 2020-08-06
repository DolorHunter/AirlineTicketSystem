from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import UserItem


def user_info(request):
    all_userapp_items = UserItem.objects.all()
    return render(request, 'UserInfo.html', {'all_items': all_userapp_items})


def login(request):
    item = UserItem(request.POST or None)
    if item.username and item.password:
        user = authenticate(username=item.username, password=item.password)
        if user is not None:  # 登录成功
            login(request, user)
            context = {
                'username': request.user.username
            }
            return render(request, '../ticketCenter.html', context)
        else:  # 登录失败
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def register(request):
    item = UserItem(request.POST or None)
    if item.username and item.password and item.email:
        item.save()
        return render(request, 'login.html')  # 注册成功直接render result页面
    else:
        return render(request, 'register.html')
