from django.db import models
from django.db import models
from products.models import Product
from users.models import CustomUser

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    transaction_value = models.IntegerField()
