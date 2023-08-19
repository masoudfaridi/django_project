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


class UpdateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField( label="Fisrt name")
    last_name = serializers.CharField(label="Last name")
    username = serializers.CharField( label="user name")
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Enter a password'}, write_only=True, label="password")
    email = serializers.EmailField( label="email")
    # is_active = serializers.BooleanField(default=False ,label = "Active the account")
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        #is_active = self.validated_data['is_active']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']

        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error': 'username does not exists!'})
        else:
            account = User.objects.get(username=username)
            if account.check_password('{}'.format(password)):
                if User.objects.filter(email=self.validated_data['email']).exists():
                    raise serializers.ValidationError({'error': 'Email already exists!'})

                account.first_name = first_name
                account.last_name = last_name
                account.email = email
                #account.first_name = first_name or account.first_name
                account.save()
            else:
                raise serializers.ValidationError({'error': 'password was not correct!'})
        return account

class RegistrationUserSerializer(serializers.Serializer):
    first_name = serializers.CharField( label="Fisrt name")
    last_name = serializers.CharField(label="Last name")
    username = serializers.CharField( label="user name")
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Enter a password'}, write_only=True, label="password")
    password2 = serializers.CharField(style={'input_type': 'password', 'placeholder': 'repeat the password'}, write_only=True, label="password")
    email = serializers.EmailField( label="email")
    is_active = serializers.BooleanField(default=False ,label = "Active the account")
    def save(self):
        # username = self.validated_data['username']
        # email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        is_active = self.validated_data['is_active']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']

        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error': 'username is not available!'})
        account = User(email=self.validated_data['email'], username=self.validated_data['username']
                       ,first_name=first_name,last_name=last_name)
        account.is_active = False #is_active
        account.set_password(password)
        account.save()
        return account

