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










#
# class User_serializers(serializers.Serializer):
#     email=serializers.EmailField(required=True)
#     mobile=serializers.CharField()
#     country_code = serializers.CharField(required=True)
#     user_name = serializers.CharField(required=True)
#     confirm_password=serializers.CharField(required=True)
#     password=serializers.CharField(required=True)
#     device_type = serializers.CharField()
#     device_token = serializers.CharField()
#     fcm_token=serializers.CharField()
#     bio=serializers.CharField(required=False)
#     notification_status=serializers.BooleanField(required=False)
#
# class User_serializers1(serializers.ModelSerializer):
#     profile_image = serializers.SerializerMethodField()
#     mobile=serializers.SerializerMethodField()
#     #user_name=serializers.SerializerMethodField()
#
#     class Meta:
#         model = Customer
#         fields = ["id","last_login","profile_image","image_link","name","user_name","email","country_code","mobile","latitude","longitude","is_active","is_SocialLogin",'bio','notification_status']#"__all__"
#     profile_image = serializers.SerializerMethodField()
#     def get_profile_image(self, obj):
#
#         try:
#             # (base_url + obj.image.url)
#             x = (base_url + obj.profile_image.url)
#         except:
#             x = None
#         #print("bjd,bdvbjdvbdjvbdjvb 121  == ", x)
#         return x
#     def get_mobile(self, obj):
#         #print("===== 40 ",obj)
#         if obj.SocialLogin == True:
#             return ''
#         else:
#             return obj.mobile
#
#     '''
#      def get_user_name(self, obj):
#             if obj.SocialLogin == True:
#                 return ''
#             else:
#                 return obj.user_name
#                 '''
#
#
# class login_serializers(serializers.Serializer):
#     email=serializers.EmailField(required=False)
#     mobile = serializers.EmailField(required=False)
#     user_name = serializers.CharField(required=False)
#     fcm_token=serializers.CharField()
#     device_type = serializers.CharField()
#     device_token = serializers.CharField()
#     password=serializers.CharField(required=True)
#
# class Forgot_password(serializers.Serializer):
#     email=serializers.EmailField(required=True)
#
# class Forgot_password_reset_serializers(serializers.Serializer):
#     password = serializers.CharField(required=True)
#     confirm_password = serializers.CharField(required=True)
#
# class reset_password_serializers(serializers.Serializer):
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
#     confirm_password = serializers.CharField(required=True)
#
# class verify_mobile_serializers(serializers.Serializer):
#     enter_otp=serializers.CharField(required=True)
#     mobile_number = serializers.CharField(required=True)
#     country_code = serializers.CharField(required=True)
#
# class verify_email_serializers(serializers.Serializer):
#     enter_otp=serializers.CharField(required=True)
#     email= serializers.CharField(required=True)
#
# class resend_email_verification_link_serializers(serializers.Serializer):
#     email=serializers.EmailField(required=True)
#
# class resend_otp_serializers(serializers.Serializer):
#     country_code = serializers.CharField(required=True)
#     mobile=serializers.CharField(required=True)
#
# class social_login(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#     image_link=serializers.CharField(required=False)
#     name=serializers.CharField(required=False)
#     uid=serializers.CharField(required=False)
#     login_type=serializers.CharField(required=True)
#     mobile=serializers.CharField(required=False)
#     device_token=serializers.CharField(required=True)
#     profile_image=serializers.ImageField(required=False)
#     fcm_token=serializers.CharField(required=False)
#     device_type = serializers.CharField(required=True)
#
# '''
# class update_profile_serializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ["profile_image","user_name","country_code","mobile",]
#         '''
#
# class update_profile_serializer(serializers.Serializer):
#     profile_image=serializers.ImageField(required=False)
#     user_name=serializers.CharField(required=False)
#     mobile = serializers.CharField(required=True)
#     country_code = serializers.CharField(required=True)
#     bio=serializers.CharField(required=False)
#
# class mobile_serializers(serializers.Serializer):
#     user_name=serializers.CharField(required=False)
#     email=serializers.EmailField(required=False)
#     mobile = serializers.CharField(required=True)
#     country_code = serializers.CharField(required=True)
#
# class View_user_profile_seralizer(serializers.Serializer):
#     userid =serializers.CharField(required=True)
#     type=serializers.CharField(required=False)