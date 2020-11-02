from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from TicketApp.models import TicketItem
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


@login_required(login_url='login')
def is_superuser(user_id):
    user_item = User.objects.get(id=user_id)
    if not user_item.is_superuser:
        raise PermissionDenied


@login_required(login_url='login')
def admin_user_info(request):
    is_superuser(request.user.id)
    all_user_items = User.objects.all()
    return render(request, 'AdminUserInfo.html', {'all_items': all_user_items})


@login_required(login_url='login')
def admin_add_user(request):
    is_superuser(request.user.id)
    username = request.POST['add_username']
    password = request.POST['add_password']
    email = request.POST['add_email']
    item = User(username=username, password=password, email=email)
    item.save()
    return HttpResponseRedirect('/adminUserInfo/')


@login_required(login_url='login')
def admin_delete_user(request, user_id):
    is_superuser(request.user.id)
    item = User.objects.get(id=user_id)
    item.delete()
    return HttpResponseRedirect('/adminUserInfo/')


@login_required(login_url='login')
def admin_update_user(request, user_id):
    is_superuser(request.user.id)
    username = request.POST['update_username_'+str(user_id)]
    password = request.POST['update_password_'+str(user_id)]
    email = request.POST['update_email_'+str(user_id)]
    item = User(id=user_id, username=username, password=password, email=email)
    item.save()
    return HttpResponseRedirect('/adminUserInfo/')


@login_required(login_url='login')
def admin_search_user(request):
    is_superuser(request.user.id)
    username = request.POST['search_username']
    password = request.POST['search_password']
    email = request.POST['search_email']
    all_user_items = User.objects.all()
    if username:
        all_user_items = all_user_items.filter(username=username)
    if password:
        all_user_items = all_user_items.filter(password=password)
    if email:
        all_user_items = all_user_items.filter(email=email)
    return render(request, 'AdminUserInfo.html', {'all_items': all_user_items})


@login_required(login_url='login')
def admin_ticket_info(request):
    is_superuser(request.user.id)
    all_ticket_items = TicketItem.objects.all()
    return render(request, 'AdminTicketInfo.html', {'all_items': all_ticket_items})


@login_required(login_url='login')
def admin_search_ticket(request):
    is_superuser(request.user.id)
    flight_name = request.POST['search_flight_name']
    flight_date = request.POST['search_flight_date']
    flight_capacity = request.POST['search_flight_capacity']
    flight_booked_seats = request.POST['search_flight_booked_seats']
    flight_remained_seats = request.POST['search_flight_remained_seats']
    flight_price = request.POST['search_flight_price']
    depart_city = request.POST['search_depart_city']
    arrive_city = request.POST['search_arrive_city']
    depart_airport = request.POST['search_depart_airport']
    arrive_airport = request.POST['search_arrive_airport']
    depart_time = request.POST['search_depart_time']
    arrive_time = request.POST['search_arrive_time']
    all_ticket_items = TicketItem.objects.all()
    if flight_name:
        all_ticket_items = all_ticket_items.filter(flight_name=flight_name)
    if flight_date:
        all_ticket_items = all_ticket_items.filter(flight_date=flight_date)
    if flight_capacity:
        all_ticket_items = all_ticket_items.filter(flight_capacity=flight_capacity)
    if flight_booked_seats:
        all_ticket_items = all_ticket_items.filter(flight_booked_seats=flight_booked_seats)
    if flight_remained_seats:
        all_ticket_items = all_ticket_items.filter(flight_remained_seats=flight_remained_seats)
    if flight_price:
        all_ticket_items = all_ticket_items.filter(flight_price=flight_price)
    if depart_city:
        all_ticket_items = all_ticket_items.filter(depart_city=depart_city)
    if arrive_city:
        all_ticket_items = all_ticket_items.filter(arrive_city=arrive_city)
    if depart_airport:
        all_ticket_items = all_ticket_items.filter(depart_airport=depart_airport)
    if arrive_airport:
        all_ticket_items = all_ticket_items.filter(arrive_airport=arrive_airport)
    if depart_time:
        all_ticket_items = all_ticket_items.filter(depart_time=depart_time)
    if arrive_time:
        all_ticket_items = all_ticket_items.filter(arrive_time=arrive_time)
    return render(request, 'AdminTicketInfo.html', {'all_items': all_ticket_items})


@login_required(login_url='login')
def admin_add_ticket(request):
    is_superuser(request.user.id)
    flight_name = request.POST['add_flight_name']
    flight_date = request.POST['add_flight_date']
    flight_capacity = request.POST['add_flight_capacity']
    flight_booked_seats = request.POST['add_flight_booked_seats']
    flight_remained_seats = request.POST['add_flight_remained_seats']
    flight_price = request.POST['add_flight_price']
    depart_city = request.POST['add_depart_city']
    arrive_city = request.POST['add_arrive_city']
    depart_airport = request.POST['add_depart_airport']
    arrive_airport = request.POST['add_arrive_airport']
    depart_time = request.POST['add_depart_time']
    arrive_time = request.POST['add_arrive_time']
    item = TicketItem(flight_name=flight_name, flight_date=flight_date, flight_capacity=flight_capacity,
                      flight_booked_seats=flight_booked_seats, flight_remained_seats=flight_remained_seats,
                      flight_price=flight_price, depart_city=depart_city, arrive_city=arrive_city,
                      depart_airport=depart_airport, arrive_airport=arrive_airport, depart_time=depart_time,
                      arrive_time=arrive_time)
    item.save()
    return HttpResponseRedirect('/adminTicketInfo/')


@login_required(login_url='login')
def admin_update_ticket(request, ticket_id):
    is_superuser(request.user.id)
    flight_name = request.POST['add_flight_name'+str(ticket_id)]
    flight_date = request.POST['add_flight_date'+str(ticket_id)]
    flight_capacity = request.POST['add_flight_capacity'+str(ticket_id)]
    flight_booked_seats = request.POST['add_flight_booked_seats'+str(ticket_id)]
    flight_remained_seats = request.POST['add_flight_remained_seats'+str(ticket_id)]
    flight_price = request.POST['add_flight_price'+str(ticket_id)]
    depart_city = request.POST['add_depart_city'+str(ticket_id)]
    arrive_city = request.POST['add_arrive_city'+str(ticket_id)]
    depart_airport = request.POST['add_depart_airport'+str(ticket_id)]
    arrive_airport = request.POST['add_arrive_airport'+str(ticket_id)]
    depart_time = request.POST['add_depart_time'+str(ticket_id)]
    arrive_time = request.POST['add_arrive_time'+str(ticket_id)]
    item = TicketItem(id=ticket_id, flight_name=flight_name, flight_date=flight_date, flight_capacity=flight_capacity,
                      flight_booked_seats=flight_booked_seats, flight_remained_seats=flight_remained_seats,
                      flight_price=flight_price, depart_city=depart_city, arrive_city=arrive_city,
                      depart_airport=depart_airport, arrive_airport=arrive_airport, depart_time=depart_time,
                      arrive_time=arrive_time)
    item.save()
    return HttpResponseRedirect('/adminTicketInfo/')


@login_required(login_url='login')
def admin_delete_ticket(request, ticket_id):
    is_superuser(request.user.id)
    item = TicketItem.objects.get(id=ticket_id)
    item.delete()
    return HttpResponseRedirect('/adminTicketInfo/')
