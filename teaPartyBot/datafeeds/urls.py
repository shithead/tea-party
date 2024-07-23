from django.urls import path

from . import views


urlpatterns = [
    path("tradingview/", views.tradingview.index, name="index"),
    path("tradingview/history/<slug:exchange>/<slug:symbol>/", views.tradingview.history, name="history"),
]
