from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.safestring import mark_safe
from authentication.models import Registration

# Create your models here.

class Vendor(models.Model):
    vendor_id = ShortUUIDField(unique=True, length=10, prefix="ven", max_length=30, alphabet="abdc30")
    name = models.CharField( max_length=50)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='vendor', limit_choices_to={'is_vendor': True, 'vendor_application_status': 'approved', 'vendor_id': False})
    ## TO AVOID CIRCULAR IMPORT USE  CODE BELOW;
    # user = models.ForeignKey('authentication.Registration', on_delete=models.CASCADE, related_name='vendors', limit_choices_to={'is_vendor': True, 'vendor_application_status': 'approved'})
    # user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="vendor")
    description = models.TextField(null=True, blank=True)
    address = models.CharField( max_length=500)
    mobile = models.CharField( max_length=500)
    shipping_rating =models.CharField( max_length=500)
    days_returns = models.CharField( max_length=500)
    warenty_period = models.CharField( max_length=500)
    authentic_rating = models.CharField( max_length=500)
    chat_res =  models.CharField( max_length=500)
    date =  models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.name
    
    def vendors_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % (self.image.url))