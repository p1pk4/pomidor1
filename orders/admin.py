from django.contrib import admin
from .models import SalesOrder, DateOrder, FamilyProfiles

admin.site.register(SalesOrder)
admin.site.register(DateOrder)
admin.site.register(FamilyProfiles)