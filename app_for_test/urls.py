from django.urls import path
from .views import (class_view_add,  class_view_add_IsAdminUser, class_view_add_TokenAuthentication, add)

urlpatterns = [
    path("add/", add.as_view()),
    path("class_view_add/", class_view_add.as_view()),
    path("class_view_add_IsAdminUser/", class_view_add_IsAdminUser.as_view()),
    path("class_view_add_TokenAuthentication/", class_view_add_TokenAuthentication.as_view()),
]