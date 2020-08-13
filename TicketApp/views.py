from django.shortcuts import render
from .models import TicketItem


def ticket_info(request):
    all_ticket_items = TicketItem.objects.all()
    return render(request, 'TicketInfo.html', {'all_items': all_ticket_items})
