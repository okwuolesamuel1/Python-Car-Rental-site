from django.contrib import admin
from .models import Car
from .models import Booking
from .models import Contact
from .models import Review


admin.site.register(Car)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Review)
