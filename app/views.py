from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .serializers import *
from .models import *


def response_handler(data,message,status):
    dict={"status":status,"message":message,"data":data}
    return Response(dict)


class Sign_up(viewsets.ViewSet):
    permission_classes = [AllowAny]
    def create(self, request):
        serializer = User_reg_serializers(data=request.data)
        if serializer.is_valid():
            mobile = serializer.validated_data.get('mobile','')
            username=serializer.validated_data.get('username','')
            if mobile.isdigit() == True:
                mobile = mobile
            else:
                m = "Invalid mobile number"
                s = False
                d = {}
                return response_handler(message=m, status=s, data=d)
            #otp = random.randint()

            otp=1234
            user = Temp.objects.get_or_create(username=username,mobilenumber=mobile,otp=otp)
            m="Verification OTP Sent on the Mobile Number"
            s=1003
            d = {}
            return response_handler(message=m, status=s, data=d)
        else:
            m = serializer.errors  # "Error"
            s = False
            d = {}
            return response_handler(message=m, status=s, data=d)

class Validate_Otp(viewsets.ViewSet):
    permission_classes = [AllowAny]
    def create(self, request):
        serializer = User_reg_otp_serializers(data=request.data)
        if serializer.is_valid():
            mobile = serializer.validated_data.get('mobile','')
            otp = serializer.validated_data.get('otp','')

            if mobile.isdigit() == True:
                mobile = mobile

            else:
                m = "Invalid mobile number"
                s = False
                d = {}
                return response_handler(message=m, status=s, data=d)
            try:
                user = Temp.objects.get(mobilenumber=mobile)
                if Customer.objects.filter(mobile=mobile).first() and Temp.objects.filter(mobilenumber=mobile).first():
                    if user.otp==otp and user.otp:
                        new_user=Customer.objects.filter(mobile=mobile).first()
                        token = str(AccessToken.for_user(new_user))
                        serilizer=User_serializers(new_user)
                        m = ""
                        s = 1001
                        d = {'data':serilizer.data,'token':token}
                        return response_handler(message=m, status=s, data=d)
                    else:
                        m = "invalid Otp"
                        s = ''
                        d = {}
                        return response_handler(message=m, status=s, data=d)

                else:
                    if user.otp == otp:
                        new_user = Customer.objects.create(username=user.username, mobile=mobile,)
                        token = str(AccessToken.for_user(new_user))
                        print('+++++++++++++++++++++++++++++++++++++++++91')
                        serilizer = User_serializers(new_user)

                        m = ""
                        s = 100
                        d = {'data': serilizer.data, 'token': token}
                        return response_handler(message=m, status=s, data=d)

                    else:
                        m = "invalid Otp"
                        s = ''
                        d = {}
                        return response_handler(message=m, status=s, data=d)
            except Exception as e:
                m = str(e)
                s = ''
                d = {}
                return response_handler(message=m, status=s, data=d)
        else:
            m = serializer.errors  # "Error"
            s = False
            d = {}
            return response_handler(message=m, status=s, data=d)

class Profile(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self,request):
        user=request.user
        if user:
            serilizer = User_serializers(user)
            m = ""
            s = 100
            d = {'data': serilizer.data}
            return response_handler(message=m, status=s, data=d)
        else:
            m = "Invalid Token"
            s = 100
            d = {}
            return response_handler(message=m, status=s, data=d)

class Profile_Image_Upload(viewsets.ViewSet):
      permission_classes = [IsAuthenticated]
      def create(self,request):
        user=request.user
        serilizer=Profile_image(data=request.data)
        if serilizer.is_valid():
            image=request.FILES.get('image')
            if image:
                # image=serilizer.validated_data.get('image')
                img,created=ImageUpload.objects.get_or_create(customer=user)
                print(img,created,'++++++++++++++')
                img.image=image
                img.save()
                m = "Profile image Updated Successfully"
                s = 1005
                d = {}
                return response_handler(message=m, status=s, data=d)
        else:
            m = "Please upload image"
            s = 100
            d = {'error':serilizer.errors}
            return response_handler(message=m, status=s, data=d)


class BookTrademan(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self,request):
        def create(self, request):
            user = request.user
            serilizer = Profile_image(data=request.data)
            if serilizer.is_valid():
                image = request.FILES.get('image')
                if image:
                    # image=serilizer.validated_data.get('image')
                    img, created = ImageUpload.objects.get_or_create(customer=user)
                    print(img, created, '++++++++++++++')
                    img.image = image
                    img.save()
                    m = "Profile image Updated Successfully"
                    s = 1005
                    d = {}
                    return response_handler(message=m, status=s, data=d)
            else:
                m = "Please upload image"
                s = 100
                d = {'error': serilizer.errors}
                return response_handler(message=m, status=s, data=d)

class BookTrademan(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self,request):
        user=request.user
        serilizer=BookTradeManSerilizer(data=request.data)
        if serilizer.is_valid():
            trademanid=serilizer.validated_data.get('trademan')
            date=serilizer.validated_data.get('date')
            print(date)
            try:
                trademan=Trademan.objects.get(id=trademanid)
                print('+++++++++++++++++++',trademan.status)
                if trademan.status == 'ACTIVE':
                   book =BookTradeMan.objects.create(customer=user,trademan=trademan,date=date)
                   m = "Request Added Successfully"
                   s = 1004
                   d = {}
                   return response_handler(message=m, status=s, data=d)
                else :
                    print('-----------------------191')
                    m = "Trademan is not active"
                    s = 100
                    d = {}
                    return response_handler(message=m, status=s, data=d)

            except Exception as e:
                m = str(e)
                s = 100
                d = {}
                return response_handler(message=m, status=s, data=d)
        else:
            m = ""
            s = 100
            d = {'error':serilizer.errors}
            return response_handler(message=m, status=s, data=d)


