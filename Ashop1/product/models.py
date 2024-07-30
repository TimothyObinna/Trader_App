from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.safestring import mark_safe
from authentication.models import Registration
from django.contrib.auth import get_user_model
from vendor.models import Vendor
from django.utils.translation import gettext as _


User = get_user_model()
# Create your models here.

class Category(models.Model):
    category_id = ShortUUIDField(unique=True, length=10, prefix="cat", max_length=30, alphabet="abdc30")
    # Incase I want just numbers and one alphabet on each ID generated ;
    # category_id = ShortUUIDField(unique=True, length=11, prefix="cat", max_length=30, alphabet="0123456789abcdefghijklmnopqrstuvwxyz")
    category_name = models.CharField( max_length=100)
    image = models.ImageField(upload_to="category")
    date =  models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
    
    def category_image(self):
        return mark_safe('<img src="%s" width="90" height="40" />' % (self.image.url))
    



order_status = (
    ('processing', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)    



status = [
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in review', 'In Review'),
    ('approved', 'Approved'),
]


class Product(models.Model):
    product_id = ShortUUIDField(unique=True, length=20, prefix="pro", max_length=30, alphabet="abdc30")
    product_name = models.CharField(max_length=100)
    # user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='vendors', limit_choices_to={'is_vendor': True, 'vendor_application_status': 'approved'})
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, related_name='product')
    image = models.ImageField(_(""), upload_to="product_image")
    description = models.TextField(_("Description"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='product')
    product_details = models.TextField(_("Product Details"))
    price = models.DecimalField(max_digits=20, decimal_places=2, default=00)
    old_price = models.DecimalField(max_digits=60, decimal_places=2)
    specification = models.TextField(_("Product Specification"))
    product_status = models.CharField(choices=status, max_length=50, default='in review')
    in_stock = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    my_stock = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    # sku = ShortUUIDField(unique=True, length=4, prefix="pro", max_length=10, alphabet="0123456789")
    # product_kind = models.CharField(max_length=100, null=True, blank=True, default='best selling')
    # status = models.BooleanField(default=True)
    # summary_product_info = RichTextUploadingField(null=True, blank=True)

    # COMMENTED on sku field due to migration warning, ask Skyline the approach he used ******


    class Meta:
        verbose_name_plural = 'products'
        ordering = ['-last_updated']

    def __str__(self):
        return self.product_name
    
    def product_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % (self.image.url))
    
    def product_percentage(self):
        if self.old_price:
            new_price = (self.price - self.old_price) / abs(self.old_price) * 100
        return new_price



RATING_CHOICES = [
    (1, '⭐️'), 
    (2, '⭐️⭐️'), 
    (3, '⭐️⭐️⭐️'), 
    (4, '⭐️⭐️⭐️⭐️'), 
    (5, '⭐️⭐️⭐️⭐️⭐️'),
]



class Productimage(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='product_names')
    images = models.ImageField(_(""), upload_to='product images', default='product.jpg')
    date = models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name_plural = 'Products images'

    def __str__(self):
        return self.product_name.product_name    



class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __str__(self):
        return self.review
    
    def get_rating(self):
        return self.rating
    
    class Meta:
        verbose_name_plural = 'Product Reviews'



class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    paid_status = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=60, decimal_places=2, default=70.90)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=order_status, max_length=200, default='processing')
    invoice_No = models.CharField(max_length=200, default='No2304')

    class Meta:
        verbose_name_plural = 'Cart orders'

    def __str__(self):
        return self.product_status    



class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=60, decimal_places=2, default=70.90)
    total = models.DecimalField(max_digits=60, decimal_places=2, default=70.90)
    qty = models.IntegerField(default=0)
    invoice_No = models.CharField(max_length=200, default='No2304')


    class Meta:
        verbose_name_plural = 'Cart orders'


    def __str__(self):
        return self.invoice_No


    def cartitem_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % (self.image.url))





class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product






class OrderAddress(models.Model):
    address = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(False)