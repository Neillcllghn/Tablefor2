from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from datetime import datetime, timedelta
from .models import Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView
from .forms import BookingForm

# this is to create an index/home page view


def index(request):
    return render(request, "index.html")


# This class view allows user to view their bookings in list format.


class BookingList(generic.ListView):
    model = Booking
    template_name = 'bookings.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# View to create a booking.


class BookingCreate(CreateView):
    model = Booking
    template_name = 'create_bookings.html'
    form_class = BookingForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.INFO,
                             'Booking was made successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Ups.....Something went wrong')
        return super().form_invalid(form)
