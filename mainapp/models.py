#product
#category
#cartproduct
#cart
#order
#customer
#specification

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class Category(models.Model):
    """
    Model representing categories of products
    """

    name = models.CharField(max_length=255, verbose_name='Category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing products
    """

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Name of product')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Image of product')
    description = models.TextField(verbose_name='Product description', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.title


class NotebookProduct(Product):
    """
    Model representing class of product for Product class 
    """

    diagonal = models.CharField(max_length=255, verbose_name='Diagonal')
    dispaly_type = models.CharField(max_length=255, verbose_name='Display type')
    processor_frq = models.Charfield(max_length=255, verbose_name='Processor frequenci')
    ram = models.CharField(max_length=255, verbose_name='Random memory qty.')
    video = models.CharField(max_length=255, verbose_name='Video card type')
    time_withot_charge = models.CharField(max_length=255, verbose_name='Time to charge')

    def __str__(self):
        return "


class CartProduct(models.Model):
    """
    Model representing products in the particular cart of the customer
    """

    user = models.ForeignKey('Customer', verbose_name='Customer name', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Customer"s cart', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total sum')

    def __str__(self):
        return "Product {} (for cart)".format(self.product.title)

class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Cart owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Total sum')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Phone number')
    address = models.CharField(max_length=255, verbose_name='Address')

    def __str__(self):
        return "Bayer: {},{}".format(self.user.first_name, self.user.last_name)

