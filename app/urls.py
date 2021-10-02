from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'sign_up',Sign_up,basename='sign_up')
router.register(r'validateotp',Validate_Otp,basename='validate_Otp')
router.register(r'profile',Profile,basename='Profile')
router.register(r'imageupload',Profile_Image_Upload,basename='imageupload')
router.register(r'booktrademan',BookTrademan,basename='booktrademan')
urlpatterns = [
    path('',include(router.urls))
]
