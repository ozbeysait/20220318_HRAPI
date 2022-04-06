from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    preferred_first_name = models.CharField(max_length=50, blank=True, null=True)
    preferred_last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    title_code = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    position_code = models.CharField(max_length=10, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    department_code = models.CharField(max_length=10, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    location_code = models.CharField(max_length=10, blank=True, null=True)
    work_type = models.CharField(max_length=50, blank=True, null=True)
    work_type_code = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True, default="Active")
    employee_type = models.CharField(max_length=50, blank=True, null=True)
    employee_type_code = models.CharField(max_length=10, blank=True, null=True)
    manager_id = models.CharField(max_length=50, blank=True, null=True)
    entitlements = models.ManyToManyField('Entitlement', blank=True)

    def __str__(self):
        return str(self.employee_id) + " - " + self.first_name + " " + self.last_name


class Entitlement(models.Model):
    entitlement_id = models.AutoField(primary_key=True)
    entitlement_name = models.CharField(max_length=50, blank=True, null=True)
    entitlement_description = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.entitlement_id) + " - " + self.entitlement_name