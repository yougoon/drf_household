# users/urls.py
from django.urls import path
from .views import register, login, register_admin, promote_to_admin

urlpatterns = [
    path("register/", register),
    path("login/", login),
    path("register-admin/", register_admin, name="register-admin"),
    path("promote-admin/<int:user_id>/", promote_to_admin, name="promote-admin"),
]