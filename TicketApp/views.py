from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import TicketItem, BookTicketItem
from django.contrib import messages
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def ticket_info(request):
    all_ticket_items = TicketItem.objects.all()
    return render(request, 'TicketInfo.html', {'all_items': all_ticket_items})


def search_ticket(request):
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
    return render(request, 'TicketInfo.html', {'all_items': all_ticket_items})


@login_required(login_url='login')
def pre_book_ticket(request, ticket_id):
    ticket_item = TicketItem.objects.filter(id=ticket_id)
    if request.method == 'POST':
        return render(request, 'BookTicket.html', {'all_items': ticket_item})
    return HttpResponseRedirect('/ticketInfo/')


@login_required(login_url='login')
def book_ticket(request, ticket_id):
    ticket_item = TicketItem.objects.get(id=ticket_id)
    book_ticket_item = BookTicketItem.objects.filter(user_id=request.user.id, book_status='已订票')
    if ticket_item in book_ticket_item:
        messages.error(request, '已经订阅本航班')
    else:
        if request.method == 'POST':
            if ticket_item.flight_remained_seats > 0:
                ticket_item.flight_booked_seats += 1
                ticket_item.flight_remained_seats -= 1
                ticket_item.save()
                book_ticket_item = BookTicketItem(user_id=request.user.id, ticket_id=ticket_item,
                                                  book_status='已订票', seat_id=str(ticket_item.flight_booked_seats))
                book_ticket_item.save()
        return HttpResponseRedirect('/myTicketInfo/')


@login_required(login_url='login')
def checkin_ticket(request, ticket_id):
    ticket_item = TicketItem.objects.filter(id=ticket_id, checkinitem__ticket_id=ticket_id).values(
                                            'id', 'flight_name', 'flight_date', 'flight_capacity',
                                            'flight_booked_seats', 'flight_remained_seats',
                                            'flight_price', 'depart_city', 'arrive_city',
                                            'depart_airport', 'arrive_airport', 'depart_time',
                                            'arrive_time', 'checkinitem__checkin_windows',
                                            'checkinitem__boarding_port', 'bookticketitem__seat_id')
    if request.method == 'POST':
        return render(request, 'CheckinTicket.html', {'all_items': ticket_item})
    return HttpResponseRedirect('/myTicketInfo/')


@login_required(login_url='login')
def pre_pay_ticket(request, ticket_id):
    ticket_item = TicketItem.objects.filter(id=ticket_id)
    if request.method == 'POST':
        return render(request, 'PayTicket.html', {'all_items': ticket_item})
    return HttpResponseRedirect('/myTicketInfo/')


@login_required(login_url='login')
def pay_ticket(request, ticket_id):
    ticket_item = TicketItem.objects.get(id=ticket_id)
    if request.method == 'POST':
        book_ticket_item = BookTicketItem.objects.filter(user_id=request.user.id, ticket_id=ticket_item,
                                                         book_status='已订票').first()
        if book_ticket_item:
            book_ticket_item.book_status = '已付款'
            book_ticket_item.save()
    return HttpResponseRedirect('/myTicketInfo/')


@login_required(login_url='login')
def pre_cancel_ticket(request, ticket_id):
    ticket_item = TicketItem.objects.filter(id=ticket_id)
    if request.method == 'POST':
        return render(request, 'CancelTicket.html', {'all_items': ticket_item})
    return HttpResponseRedirect('/myTicketInfo/')


@login_required(login_url='login')
def cancel_ticket(request, ticket_id):
    ticket_item = TicketItem.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket_item.flight_booked_seats -= 1
        ticket_item.flight_remained_seats += 1
        ticket_item.save()
        book_ticket_item = BookTicketItem.objects.filter(Q(book_status='已订票') | Q(book_status='已付款'),
                                                         user_id=request.user.id, ticket_id=ticket_item,
                                                         ).first()
        book_ticket_item.book_status = '已取消'
        book_ticket_item.save()
    return HttpResponseRedirect('/myTicketInfo/')


@login_required(login_url='login')
def my_ticket_info(request):
    all_ticket_items = TicketItem.objects.filter(Q(bookticketitem__book_status='已订票') |
                                                 Q(bookticketitem__book_status='已付款'),
                                                 bookticketitem__user_id=request.user.id).values(
                                                    'id', 'flight_name', 'flight_date', 'flight_capacity',
                                                    'flight_booked_seats', 'flight_remained_seats',
                                                    'flight_price', 'depart_city', 'arrive_city',
                                                    'depart_airport', 'arrive_airport', 'depart_time',
                                                    'arrive_time', 'bookticketitem__book_status')
    return render(request, 'MyTicketInfo.html', {'all_items': all_ticket_items})


@login_required(login_url='login')
def search_my_ticket(request):
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
    book_status = request.POST['search_book_status']
    all_ticket_items = TicketItem.objects.filter(Q(bookticketitem__book_status='已订票') |
                                                 Q(bookticketitem__book_status='已付款'),
                                                 bookticketitem__user_id=request.user.id).values(
                                                    'id', 'flight_name', 'flight_date', 'flight_capacity',
                                                    'flight_booked_seats', 'flight_remained_seats',
                                                    'flight_price', 'depart_city', 'arrive_city',
                                                    'depart_airport', 'arrive_airport', 'depart_time',
                                                    'arrive_time', 'bookticketitem__book_status')
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
    if book_status:
        all_ticket_items = all_ticket_items.filter(bookticketitem__book_status=book_status)
    return render(request, 'MyTicketInfo.html', {'all_items': all_ticket_items})
