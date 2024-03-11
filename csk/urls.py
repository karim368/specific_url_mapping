from django.urls import path
from csk.views import *

app_name = 'anything'

urlpatterns =[
    path('msd/',msd,name='msd'),
    path('raina/',raina,name='raina'),
    path('rahane/',rahane,name='rahane'),
]