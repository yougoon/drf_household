from django.urls import path
from .views import ClientOrderHistoryView

urlpatterns = [
    path("order-history/", ClientOrderHistoryView.as_view(), name="order-history"),
]