from django.db import models
from django.utils.translation import ugettext_lazy as _
from  django.contrib.auth.models import AbstractUser

# Create your models here.

def random_code():
    # randompass = ''.join([choice('1234567890') for i in range(4)])
    randompass = 1234
    return randompass

STATUS = (('n', '  '),
              ("ACTIVE", "Active"),
              ("INACTIVE", "Inactive")
              )


class Temp(models.Model):
    username=models.CharField(max_length=250)
    mobilenumber=models.CharField(max_length=250)
    otp=models.CharField(verbose_name=_('OTP'), max_length=10,default="1234")
    expire_time=models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def get_expire_time(self, obj):
    #     obj.expire_time =

    def __str__(self):
        return str(self.username)

class Customer(AbstractUser):
    dob = models.DateField(verbose_name=_('Date of Birth'), blank=True, null=True)
    mobile = models.CharField(verbose_name=_('Mobile Number'), max_length=100, unique=True )
    status = models.CharField(max_length=100, choices=STATUS, null=True, default='n')
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return str(self.username)



class TradeType(models.Model):
    Type=models.CharField(verbose_name=_('Type'), max_length=100, )
    status = models.CharField(max_length=100, choices=STATUS, null=True, default='n')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.Type)


class Trademan(models.Model):
    name=models.CharField(verbose_name=_('Name'), max_length=100, null=True, blank=True)
    tradeType=models.ForeignKey('TradeType',on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, null=True, default='n')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)


order = (('n', '  '),
              ("PENDING", "PENDING"),
              ("BOOKED", "BOOKED"),
              ("CANCELED","CANCELED")

              )
class BookTradeMan(models.Model):
    image=models.ImageField(blank=True, null=True, upload_to='profiles', default='/static/dummy.png')
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE)
    trademan=models.ForeignKey('Trademan',on_delete=models.CASCADE)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    status = models.CharField(max_length=100, choices=order, null=True, default='n')

    def __str__(self):
        return str(self.customer.username)


class ImageUpload(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='')
    status = models.CharField(max_length=100, choices=STATUS, null=True, default='n')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer.username)


