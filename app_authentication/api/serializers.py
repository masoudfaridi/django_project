from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
class PasswordChangeUserSerializer(serializers.Serializer):
    username = serializers.CharField( label="user name")
    old_password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="old password")
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="new password")
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="repeat new password")

    def save(self):
        username = self.validated_data['username']
        old_password = self.validated_data['old_password']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error': 'username does not exists!'})
        else:
            account = User.objects.get(username=username)
            if account.check_password('{}'.format(old_password)):
                account.set_password(password)
                account.save()
            else:
                raise serializers.ValidationError({'error': 'password was not correct!'})
        return account





class CustomAuthtokenSerializer(serializers.Serializer):
    username = serializers.CharField(label="user name")
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label="password")

    # def validate_username(self, attrs):
    #     if not User.objects.filter(username=attrs).exists():
    #         raise serializers.ValidationError({'error': 'username does not exists!'})
    #     return attrs
    #
    # def validate(self, data):
    #     account = User.objects.get(username=data['username'])
    #     if not account.check_password('{}'.format(data['password'])):
    #         raise serializers.ValidationError({'error': 'username and password not matched!'})
    #     return data

    def save(self):
        username = self.validated_data['username']
        password = self.validated_data['password']
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error': 'username does not exists!'})
        else:
            account = User.objects.get(username=username)
            if not account.check_password('{}'.format(password)):
                raise serializers.ValidationError({'error': 'password was not correct!'})
        return account






