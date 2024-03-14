from rest_framework import serializers
from django.contrib.auth import  get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError



class UserLoginSerializer(serializers.Serializer):
    email=serializers.CharField(
        label=_('Email'),
        write_only=True,
    )
    password=serializers.CharField(
        label=_('Password'),
        write_only=True,
        style={'input_type':'password'}
    )
   

    def validate(self,data):
        request=self.context.get('request')
        email=data.get('email')
        password=data.get('password')
        get_user=authenticate(request,email=email,password=password)
        if email and password:
            if get_user is not None:
                data['user']=get_user  
                return data  
            raise serializers.ValidationError('email or password is wrong',code='user_not_exists')    
        else:
            raise serializers.ValidationError('required email and password',code='required_email_pass')    



