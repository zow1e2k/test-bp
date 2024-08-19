from django.db import models
from users.models import CustomUser
from products.lessons.models import Lesson

class Product(models.Model):
	name = models.CharField(max_length=64)
	date_created = models.DateTimeField()
	price = models.IntegerField()
	creator = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=False)
	lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, null=False)

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
		ordering = ('-id',)

	def __str__(self):
		return self.name