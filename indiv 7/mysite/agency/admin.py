from django.contrib import admin

from .models import Agency, Contract, Employer

admin.site.register(Agency)
admin.site.register(Employer)
admin.site.register(Contract)