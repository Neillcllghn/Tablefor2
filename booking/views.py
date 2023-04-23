from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from datetime import datetime, timedelta
from .models import Booking

# this is to create an index/home page view


def index(request):
    return render(request, "index.html")


# This class view allows user to view their bookings in list format.


class BookingList(generic.ListView):
    model = Booking
    template_name = 'bookings.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
