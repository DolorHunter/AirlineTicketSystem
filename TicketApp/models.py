from django.db import models


class TicketAppItem(models.Model):
    flight_name = models.TextField()
    flight_date = models.TextField()
    flight_capacity = models.TextField()
    flight_booked_seats = models.TextField()
    flight_remained_seats = models.TextField()
    flight_price = models.TextField()
    flight_income = models.TextField()
    depart_city = models.TextField()
    arrive_city = models.TextField()
    depart_airport = models.TextField()
    arrive_airport = models.TextField()
    depart_time = models.TextField()
    arrive_time = models.TextField()
