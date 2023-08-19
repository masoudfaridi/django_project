from rest_framework.throttling import UserRateThrottle

#https://www.django-rest-framework.org/api-guide/throttling/

class CustomUserRateThrottle(UserRateThrottle):
    rate= '3/day'




