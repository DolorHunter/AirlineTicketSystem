from django.db import models


class TicketItem(models.Model):
    flight_name = models.TextField()
    flight_date = models.TextField()
    flight_capacity = models.IntegerField()
    flight_booked_seats = models.IntegerField()
    flight_remained_seats = models.IntegerField()
    flight_price = models.TextField()
    depart_city = models.TextField()
    arrive_city = models.TextField()
    depart_airport = models.TextField()
    arrive_airport = models.TextField()
    depart_time = models.TextField()
    arrive_time = models.TextField()


class BookTicketItem(models.Model):
    user_id = models.IntegerField()
    ticket_id = models.ForeignKey(TicketItem, on_delete=models.CASCADE)
    book_status = models.TextField()
    seat_id = models.TextField()


class CheckinItem(models.Model):
    ticket_id = models.ForeignKey(TicketItem, on_delete=models.CASCADE)
    checkin_windows = models.TextField()
    boarding_port = models.TextField()
