from django.urls import path
from .views import *

urlpatterns = [
    path('Data/', DealView.as_view(), name='Data'),
    path('Result/', DealList.as_view(), name='Result')
]