
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationUserSerializer, PasswordChangeUserSerializer, UpdateUserSerializer
#from django.contrib.auth import login, logout
from rest_framework.response import Response



class registration_view(APIView):
    serializer_class = RegistrationUserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data,partial=True)#RegistrationUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email
            #token = Token.objects.get(user=account).key
            #data['token'] = token

            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token),
            # }
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)



class Update_User_view(APIView):
    serializer_class = UpdateUserSerializer
    def put(self, request, *arg, **kwargs):
        serializer = self.serializer_class(data=request.data)#PasswordChangeUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            # account = serializer.save()
            # data['response'] = "Registration Successful!"
            # data['username'] = account.username
            # data['email'] = account.email
            #token = Token.objects.get(user=account).key
            #data['token'] = token
            #refresh = RefreshToken.for_user(account)
            #data['token'] = {
            #    'refresh': str(refresh),
            #    'access': str(refresh.access_token),
            #}
        else:
            #data = serializer.errors
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class change_password_view(APIView):
    serializer_class = PasswordChangeUserSerializer
    def post(self, request, *arg, **kwargs):
        serializer = self.serializer_class(data=request.data)#PasswordChangeUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            # account = serializer.save()
            # data['response'] = "Registration Successful!"
            # data['username'] = account.username
            # data['email'] = account.email
            #token = Token.objects.get(user=account).key
            #data['token'] = token
            #refresh = RefreshToken.for_user(account)
            #data['token'] = {
            #    'refresh': str(refresh),
            #    'access': str(refresh.access_token),
            #}
        else:
            #data = serializer.errors
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST',])
# def registration_view(request):
#
#     if request.method == 'POST':
#         serializer = RegistrationUserSerializer(data=request.data)
#
#         data = {}
#
#         if serializer.is_valid():
#             account = serializer.save()
#
#             data['response'] = "Registration Successful!"
#             data['username'] = account.username
#             data['email'] = account.email
#
#             token = Token.objects.get(user=account).key
#             data['token'] = token
#
#             refresh = RefreshToken.for_user(account)
#             data['token'] = {
#                                 'refresh': str(refresh),
#                                 'access': str(refresh.access_token),
#                             }
#
#         else:
#             data = serializer.errors
#
#         return Response(data, status=status.HTTP_201_CREATED)
