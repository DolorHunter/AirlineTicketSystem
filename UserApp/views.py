from django.shortcuts import render
from .models import UserItem

def user_info(request):
    all_user_items = UserItem.objects.all()
    return render(request, 'UserInfo.html', {'all_items': all_user_items})
