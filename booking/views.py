from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from datetime import datetime, timedelta
from .models import Booking
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import BookingForm

# this is to create an index/home page view


def index(request):
    return render(request, "index.html")


# This class view allows user to view their bookings in list format.

class BookingList(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = 'bookings.html'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# View to create a booking.


class BookingCreate(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'create_bookings.html'
    form_class = BookingForm
    success_url = reverse_lazy('bookings')

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

# to update a booking


class BookingUpdate(LoginRequiredMixin, UpdateView):
    model = Booking
    template_name = 'update_bookings.html'
    form_class = BookingForm
    success_url = reverse_lazy('bookings')

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.INFO,
                             'Booking was updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Ups.....Something went wrong')
        return super().form_invalid(form)

    def get_object(self, queryset=None):
        booking_id = self.kwargs.get('booking_id')
        return get_object_or_404(Booking, id=booking_id)

# delete a booking


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('bookings')
