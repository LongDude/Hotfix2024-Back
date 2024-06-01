from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('', views.Tickets.as_view(), name='tickets'),
    path('flights/',views.TicketsApiView.as_view())
]