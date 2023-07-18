from django.urls import path

from . import views

urlpatterns = [
    path("", views.flightlist, name="flightlist"),
    path("buy/<int:flight_id>", views.buy_ticket, name="buy_ticket"),
]