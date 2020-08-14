from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TicketItem, BookTicketItem


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


def book_ticket(request, ticket_id):
    #BookTicketItem(user_id=user_id, ticket_id=ticket_id)
    #return HttpResponseRedirect('/myTicket/')
    pass


def my_ticket_info(request, user_id):
    '''
    bookTicketItem = BookTicketItem.objects.get(user_id=user_id)
    bookTicketItem.ticketitem_set.all()
    all_ticket_items = TicketItem.objects.filter(id=ticket_id)
    return render(request, 'MyTicketInfo.html', {'all_items': all_ticket_items})
    '''
    pass
