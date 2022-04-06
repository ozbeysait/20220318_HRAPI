from django.contrib import admin
from hr.models import Employee, Entitlement

# Register your models here.
admin.site.register(Employee)
admin.site.register(Entitlement)