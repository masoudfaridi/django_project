import rest_framework.permissions
import rest_framework_simplejwt.authentication
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

class add(APIView):
 permission_classes = [AllowAny,]
 def get(self, request, format=None):
  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')


class class_view_add_TokenAuthentication(APIView):
 authentication_classes = [TokenAuthentication,]
 permission_classes = [IsAuthenticated,]
 def get(self, request, format=None):
  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')


class class_view_add_TokenAuthentication_admin(APIView):
 authentication_classes = [TokenAuthentication]
 permission_classes = [IsAdminUser,]
 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')

class class_view_add_JWTAuthentication(APIView):
 authentication_classes = [JWTAuthentication]
 permission_classes = [IsAuthenticated, ]
 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')



class class_view_add_JWTAuthentication_admin(APIView):
 authentication_classes = [JWTAuthentication]
 permission_classes = [IsAdminUser, ]
 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')




class class_view_add_throttle_classes(APIView):
 throttle_classes = [UserRateThrottle]
 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')