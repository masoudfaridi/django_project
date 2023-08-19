from django.urls import path, include
from rest_framework.authtoken import views
from .views import CustomAuthtoken
urlpatterns = [


    # path('token/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/',views.obtain_auth_token),
    path('token_CustomAuthtoken/',CustomAuthtoken.as_view())
]
