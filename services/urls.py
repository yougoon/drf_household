from django.urls import path
from .views import ServiceListView, ReviewCreateView, ServiceReviewListView

urlpatterns = [
    path("services/", ServiceListView.as_view(), name="service-list"),
    path("leave-review/", ReviewCreateView.as_view(), name="leave-review"),
    path("reviews/<int:service_id>/", ServiceReviewListView.as_view(), name="service-reviews"),
]