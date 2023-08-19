import rest_framework.permissions
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import permissions
from rest_framework.views import APIView



class add(APIView):
 permission_classes = [AllowAny]

 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')


class class_view_add(APIView):

 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')


class class_view_add_TokenAuthentication(APIView):
 #authentication_classes = [TokenAuthentication]
 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')

class class_view_add_IsAdminUser(APIView):
 #authentication_classes = [TokenAuthentication]
 #permission_classes = [IsAdminUser]

 def get(self, request, format=None):

  a = request.GET.get("a") or 1
  b = request.GET.get("b") or 1
  return HttpResponse(f'{a} + {b} = {int(a) + int(b)} ')
