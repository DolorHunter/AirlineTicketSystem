from django.shortcuts import render
from .models import TicketAppItem


def ticket_info(request):
    all_ticketapp_items = TicketAppItem.objects.all()
    return render(request, 'TicketInfo.html', {'all_items': all_ticketapp_items})
