from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserItem
from .forms import CreateUserForm


@login_required(login_url='login')
def user_info(request):
    all_user_items = UserItem.objects.all()
    return render(request, 'UserInfo.html', {'all_items': all_user_items})


@login_required(login_url='login')
def add_user(request):
    username = request.POST['add_username']
    password = request.POST['add_password']
    email = request.POST['add_email']
    item = UserItem(username=username, password=password, email=email)
    item.save()
    return HttpResponseRedirect('/userInfo/')


@login_required(login_url='login')
def delete_user(request, user_id):
    item = UserItem.objects.get(id=user_id)
    item.delete()
    return HttpResponseRedirect('/userInfo/')


@login_required(login_url='login')
def update_user(request, user_id):
    username = request.POST['update_username_'+str(user_id)]
    password = request.POST['update_password_'+str(user_id)]
    email = request.POST['update_email_'+str(user_id)]
    item = UserItem(id=user_id, username=username, password=password, email=email)
    item.save()
    return HttpResponseRedirect('/userInfo/')


@login_required(login_url='login')
def search_user(request):
    username = request.POST['search_username']
    password = request.POST['search_password']
    email = request.POST['search_email']
    all_user_items = UserItem.objects.all()
    if username:
        all_user_items = all_user_items.filter(username=username)
    if password:
        all_user_items = all_user_items.filter(password=password)
    if email:
        all_user_items = all_user_items.filter(email=email)
    return render(request, 'UserInfo.html', {'all_items': all_user_items})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ticketInfo')
        else:
            messages.info(request, 'Username or password is incorrect')
            context = {}
            return render(request, 'login.html', context)
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
