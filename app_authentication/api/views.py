


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from app_authentication.api.serializers import CustomAuthtokenSerializer
from rest_framework import status

class CustomAuthtoken(APIView):
    serializer_class = CustomAuthtokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           partial=True)  # RegistrationUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successful!"
            data['username'] = account.username
            data['email'] = account.email
            token, created = Token.objects.get_or_create(user=account)
            print("==============token=========")
            print(token)
            print("==============created=========")
            print(created)
            data['token'] = token.key

        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)





# class CustomAuthtoken(ObtainAuthToken):
#     serializer_class = ObtainAuthToken.serializer_class
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request':request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#
#         })



# from rest_framework.decorators import api_view
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
#
# from rest_framework import status, permissions
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import PasswordChangeUserSerializer
# #from django.contrib.auth import login, logout
# from rest_framework.response import Response
#
#
# class change_password_view(APIView):
#     serializer_class = PasswordChangeUserSerializer
#     def post(self, request, *arg, **kwargs):
#         serializer = self.serializer_class(data=request.data)#PasswordChangeUserSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             # account = serializer.save()
#             # data['response'] = "Registration Successful!"
#             # data['username'] = account.username
#             # data['email'] = account.email
#             #token = Token.objects.get(user=account).key
#             #data['token'] = token
#             #refresh = RefreshToken.for_user(account)
#             #data['token'] = {
#             #    'refresh': str(refresh),
#             #    'access': str(refresh.access_token),
#             #}
#         else:
#             #data = serializer.errors
#             return Response(serializer.errors, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#

