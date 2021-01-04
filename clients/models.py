from django.db import models


class Client(models.Model):
    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    first_name = models.CharField(blank=False, null=False, max_length=200, verbose_name='First name')
    last_name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Last name')
    birthday = models.DateTimeField(blank=False, null=False, verbose_name='Birthday')
    address = models.CharField(blank=False, null=False, max_length=200, verbose_name='Address')
    state = models.CharField(blank=False, null=False, max_length=200, verbose_name='State')
    city = models.CharField(blank=False, null=False, max_length=200, verbose_name='City')
    phone = models.IntegerField(blank=False, null=False, verbose_name='Phone number')




