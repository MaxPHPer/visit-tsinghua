from django.contrib import admin

# Register your models here.
from adminWeb import models

admin.site.register(models.SystemConfiguration)
admin.site.register(models.EveryDayBookingInfo)
admin.site.register(models.User)
admin.site.register(models.BookingRecord)
