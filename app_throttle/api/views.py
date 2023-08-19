from django.http import HttpResponse
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from .throttling import CustomUserRateThrottle




class class_view_add_throttle_classes(APIView):
 throttle_classes = [UserRateThrottle,]
 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')


class class_view_add_throttle_CustomUserRateThrottle(APIView):
 throttle_classes = [CustomUserRateThrottle,]
 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')