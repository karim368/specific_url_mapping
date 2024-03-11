from django.urls import path
from rcb.views import *

app_name = 'anything'

urlpatterns = [
    path('kohli/',kohli,name='kohli'),
    path('abd/',abd,name='abd'),
]