from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


TIME_CHOICES = (
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30")
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=200, null=True)
    group_size = models.PositiveIntegerField(null=True, default=1)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES,
                            default="17:00")
    time_booked = models.TimeField(default=datetime.now, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on", "day", "time"]

    def __str__(self):
        return f'{self.user.username} | Email: {self.email} | '
        f'Group: {self.group_size} | day: {self.day} | time: {self.time}'
