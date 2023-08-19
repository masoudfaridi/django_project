from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,
                                            TokenVerifyView   )
from .views import registration_view, change_password_view, Update_User_view
urlpatterns = [
    path('register/', registration_view.as_view(), name='register'),
    path('change_password_view/', change_password_view.as_view(), name='change_password_view'),
    path('Update_User_view/', Update_User_view.as_view(), name='Update_User_view'),

    # path('token/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
