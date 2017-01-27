from django.contrib import admin
from .models import Consigments, Applications, Journeys, Areas
# Register your models here.

admin.site.register(Consigments)
admin.site.register(Applications)
admin.site.register(Journeys)
admin.site.register(Areas)
