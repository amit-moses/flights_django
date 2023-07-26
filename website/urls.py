from django.urls import path

from . import views

urlpatterns = [
    path("", views.flightlist, name="flightlist"),
    path("buy/<int:flight_id>", views.buy_ticket, name="buy_ticket"),
    path("change_img/<int:flight_id>", views.change_img, name="change_img"),
]