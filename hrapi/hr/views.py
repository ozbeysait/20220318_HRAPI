from django.shortcuts import render
from hr.models import Employee
from hr.serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDetailAPIView(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

class EmployeeDeleteAPIView(DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()