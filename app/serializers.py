from rest_framework import serializers
from .models import *
from rest_framework import filters


class User_serializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['first_name','last_name','username','email','mobile','password']

class User_reg_serializers(serializers.Serializer):
    mobile=serializers.CharField(max_length=10)
    username=serializers.CharField(max_length=10)


class User_reg_otp_serializers(serializers.Serializer):
    mobile=serializers.CharField(max_length=10)
    otp=serializers.CharField(max_length=4)

class Profile_image(serializers.Serializer):
    image=serializers.ImageField()


class BookTradeManSerilizer(serializers.Serializer):
    trademan=serializers.CharField()
    date=serializers.DateField(format="%Y-%m-%d")


