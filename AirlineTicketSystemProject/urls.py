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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from UserApp.views import *
from TicketApp.views import *
from AdminApp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('adminUserInfo/', admin_user_info, name='adminUserInfo'),
    path('adminAddUser/', admin_add_user),
    path('adminDeleteUser/<int:user_id>', admin_delete_user),
    path('adminUpdateUser/<int:user_id>', admin_update_user),
    path('adminSearchUser/', admin_search_user),
    path('ticketInfo/', ticket_info, name='ticketInfo'),
    path('searchTicket/', search_ticket),
    path('preBookTicket/<int:ticket_id>', pre_book_ticket),
    path('bookTicket/<int:ticket_id>', book_ticket),
    path('checkinTicket/<int:ticket_id>', checkin_ticket),
    path('prePayTicket/<int:ticket_id>', pre_pay_ticket),
    path('payTicket/<int:ticket_id>', pay_ticket),
    path('preCancelTicket/<int:ticket_id>', pre_cancel_ticket),
    path('cancelTicket/<int:ticket_id>', cancel_ticket),
    path('myTicketInfo/', my_ticket_info, name='myTicketInfo'),
    path('searchMyTicket/', search_my_ticket),
    path('adminTicketInfo/', admin_ticket_info, name='adminTicketInfo'),
    path('adminAddTicket/', admin_add_ticket),
    path('adminDeleteTicket/<int:ticket_id>', admin_delete_ticket),
    path('adminUpdateTicket/<int:ticket_id>', admin_update_ticket),
    path('adminSearchTicket/', admin_search_ticket),
]

urlpatterns += staticfiles_urlpatterns()