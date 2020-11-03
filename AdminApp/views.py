from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from TicketApp.models import TicketItem, CheckinItem
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


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
    superuser = request.POST['add_superuser']
    staff = request.POST['add_staff']
    active = request.POST['add_active']
    item = User(username=username, password=password, email=email, is_superuser=superuser,
                is_staff=staff, is_active=active)
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
    superuser = request.POST['update_superuser_'+str(user_id)]
    staff = request.POST['update_staff_'+str(user_id)]
    active = request.POST['update_active_'+str(user_id)]
    item = User(id=user_id, username=username, password=password, email=email, is_superuser=superuser,
                is_staff=staff, is_active=active)
    item.save()
    return HttpResponseRedirect('/adminUserInfo/')


@login_required(login_url='login')
def admin_search_user(request):
    is_superuser(request.user.id)
    username = request.POST['search_username']
    password = request.POST['search_password']
    email = request.POST['search_email']
    superuser = request.POST['search_superuser']
    staff = request.POST['search_staff']
    active = request.POST['search_active']
    all_user_items = User.objects.all()
    if username:
        all_user_items = all_user_items.filter(username=username)
    if password:
        all_user_items = all_user_items.filter(password=password)
    if email:
        all_user_items = all_user_items.filter(email=email)
    if superuser:
        all_user_items = all_user_items.filter(is_superuser=superuser)
    if staff:
        all_user_items = all_user_items.filter(is_staff=staff)
    if active:
        all_user_items = all_user_items.filter(is_active=active)
    return render(request, 'AdminUserInfo.html', {'all_items': all_user_items})


@login_required(login_url='login')
def admin_ticket_info(request):
    is_superuser(request.user.id)
    all_ticket_items = TicketItem.objects.all().values('id', 'flight_name', 'flight_date', 'flight_capacity',
                                                       'flight_booked_seats', 'flight_remained_seats',
                                                       'flight_price', 'depart_city', 'arrive_city',
                                                       'depart_airport', 'arrive_airport', 'depart_time',
                                                       'arrive_time', 'checkinitem__checkin_windows',
                                                       'checkinitem__boarding_port')
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
    checkin_windows = request.POST['search_checkin_windows']
    boarding_port = request.POST['search_boarding_port']
    all_ticket_items = TicketItem.objects.all().values('flight_name', 'flight_date', 'flight_capacity',
                                                       'flight_booked_seats', 'flight_remained_seats',
                                                       'flight_price', 'depart_city', 'arrive_city',
                                                       'depart_airport', 'arrive_airport', 'depart_time',
                                                       'arrive_time', 'checkinitem__checkin_windows',
                                                       'checkinitem__boarding_port')
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
    if checkin_windows:
        all_ticket_items = all_ticket_items.filter(checkinitem__checkin_windows=checkin_windows)
    if boarding_port:
        all_ticket_items = all_ticket_items.filter(checkinitem__boarding_port=boarding_port)
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
    checkin_windows = request.POST['add_checkin_windows']
    boarding_port = request.POST['add_boarding_port']
    ticket_item = TicketItem(flight_name=flight_name, flight_date=flight_date, flight_capacity=flight_capacity,
                             flight_booked_seats=flight_booked_seats, flight_remained_seats=flight_remained_seats,
                             flight_price=flight_price, depart_city=depart_city, arrive_city=arrive_city,
                             depart_airport=depart_airport, arrive_airport=arrive_airport, depart_time=depart_time,
                             arrive_time=arrive_time)
    ticket_item.save()
    checkin_item = CheckinItem(ticket_id=ticket_item, checkin_windows=checkin_windows, boarding_port=boarding_port)
    checkin_item.save()
    return HttpResponseRedirect('/adminTicketInfo/')


@login_required(login_url='login')
def admin_update_ticket(request, ticket_id):
    is_superuser(request.user.id)
    flight_name = request.POST['update_flight_name_'+str(ticket_id)]
    flight_date = request.POST['update_flight_date_'+str(ticket_id)]
    flight_capacity = request.POST['update_flight_capacity_'+str(ticket_id)]
    flight_booked_seats = request.POST['update_flight_booked_seats_'+str(ticket_id)]
    flight_remained_seats = request.POST['update_flight_remained_seats_'+str(ticket_id)]
    flight_price = request.POST['update_flight_price_'+str(ticket_id)]
    depart_city = request.POST['update_depart_city_'+str(ticket_id)]
    arrive_city = request.POST['update_arrive_city_'+str(ticket_id)]
    depart_airport = request.POST['update_depart_airport_'+str(ticket_id)]
    arrive_airport = request.POST['update_arrive_airport_'+str(ticket_id)]
    depart_time = request.POST['update_depart_time_'+str(ticket_id)]
    arrive_time = request.POST['update_arrive_time_'+str(ticket_id)]
    checkin_windows = request.POST['update_checkin_windows_'+str(ticket_id)]
    boarding_port = request.POST['update_boarding_port_'+str(ticket_id)]
    ticket_item = TicketItem(id=ticket_id, flight_name=flight_name, flight_date=flight_date, flight_capacity=flight_capacity,
                             flight_booked_seats=flight_booked_seats, flight_remained_seats=flight_remained_seats,
                             flight_price=flight_price, depart_city=depart_city, arrive_city=arrive_city,
                             depart_airport=depart_airport, arrive_airport=arrive_airport, depart_time=depart_time,
                             arrive_time=arrive_time)
    ticket_item.save()
    checkin_item = CheckinItem.objects.get(ticket_id=ticket_item)
    checkin_item = CheckinItem(id=checkin_item.id, ticket_id=ticket_item, checkin_windows=checkin_windows, boarding_port=boarding_port)
    checkin_item.save()
    return HttpResponseRedirect('/adminTicketInfo/')


@login_required(login_url='login')
def admin_delete_ticket(request, ticket_id):
    is_superuser(request.user.id)
    item = TicketItem.objects.get(id=ticket_id)
    item.delete()
    return HttpResponseRedirect('/adminTicketInfo/')
