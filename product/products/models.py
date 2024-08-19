from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=64)
	date_created = models.DateTimeField()
	price = models.IntegerField()
	#creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
		ordering = ('-id',)

	def __str__(self):
		return self.name