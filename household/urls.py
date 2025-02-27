from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/services/", include("services.urls")),
    path("api/orders/", include("orders.urls")),  # Add this line
    path("api/cart/", include("cart.urls")),
]