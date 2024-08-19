from django.db import models
from users.models import CustomUser
from products.models import Product


class UserProducts(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)

	class Meta:
		verbose_name = 'Продукты пользователя'
		ordering = ('-id',)

	def __str__(self):
		return self.name