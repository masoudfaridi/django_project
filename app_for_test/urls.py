from django.urls import path
from .views import (class_view_add_TokenAuthentication,class_view_add_TokenAuthentication_admin,
                    class_view_add_JWTAuthentication,  add,class_view_add_JWTAuthentication_admin)

urlpatterns = [
    path("add/", add.as_view()),
    path("class_view_add_TokenAuthentication/", class_view_add_TokenAuthentication.as_view()),
    path("class_view_add_TokenAuthentication_admin/", class_view_add_TokenAuthentication_admin.as_view()),
    path("class_view_add_JWTAuthentication/", class_view_add_JWTAuthentication.as_view()),
    path("class_view_add_JWTAuthentication_admin/", class_view_add_JWTAuthentication_admin.as_view()),

]