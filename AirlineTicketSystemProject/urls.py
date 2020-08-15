"""AirlineTicketSystemProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UserApp.views import *
from TicketApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('userInfo/', user_info),
    path('addUser/', add_user),
    path('deleteUser/<int:user_id>', delete_user),
    path('updateUser/<int:user_id>', update_user),
    path('searchUser/', search_user),
    path('ticketInfo/', ticket_info, name='ticketInfo'),
    path('searchTicket/', search_ticket),
    path('bookTicket/<int:ticket_id>', book_ticket),
    path('myTicketInfo/', my_ticket_info, name='myTicketInfo'),
]
