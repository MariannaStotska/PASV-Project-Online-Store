from django.db import models


class Cart(models.Model):
    class Meta:
        db_table = 'cart'
        verbose_name ='Cart'
        verbose_name_plural = 'Carts'

    quantity = models.IntegerField(blank=False, null=False, max_length=200, verbose_name='Quantity')


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    order_date = models.DateTimeField(blank=False, null=False, verbose_name='Order date')
    order_status = models.CharField(blank=False, null=False, max_length=200, verbose_name='Order status')
    comments = models.CharField(blank=False, null=False, max_length=200, verbose_name='Comment')


class Payment(models.Model):
    class Meta:
        db_table = 'payments'
        verbose_name ='Payment'
        verbose_name_plural = 'Payments'

    payment_name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Payment name')


class Shipper(models.Model):
    class Meta:
        db_table = 'shippers'
        verbose_name = 'Shipper'
        verbose_name_plural = 'Shippers'

    shipper_name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Shipper name')
    shipped_date = models.DateTimeField(blank=False, null=False, verbose_name='Shipped date')


#class ProductCategory(models.Model):
 #   class Meta:
  #      db_table = 'products_categories'
   #     verbose_name ='Product Category'
    #    verbose_name_plural = 'Products Categories'


    #product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Good', on_delete=models.CASCADE)
    #category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)
