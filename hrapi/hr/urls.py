
from django.urls import path, include
from hr.views import EmployeeListAPIView, EmployeeDetailAPIView, EmployeeCreateAPIView, EmployeeDeleteAPIView

urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='list'),
    path('employees/<pk>', EmployeeDetailAPIView.as_view(), name='employee'),
    path('create/', EmployeeCreateAPIView.as_view(), name='create'),
    path('delete/<pk>', EmployeeDeleteAPIView.as_view(), name='delete'),
]
