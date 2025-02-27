from rest_framework import generics
from .models import Service, Review
from .serializers import ServiceSerializer, ReviewSerializer

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ServiceReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        service_id = self.kwargs["service_id"]
        return Review.objects.filter(service_id=service_id)