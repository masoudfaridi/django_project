from django.urls import path, include
from .views import class_view_add_throttle_classes, class_view_add_throttle_CustomUserRateThrottle

urlpatterns = [
    path("class_view_add_throttle_classes/", class_view_add_throttle_classes.as_view()),
    path("class_view_add_throttle_CustomUserRateThrottle/", class_view_add_throttle_CustomUserRateThrottle.as_view()),
]
