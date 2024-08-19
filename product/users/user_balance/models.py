from django.core.validators import MinValueValidator
from django.db import models
from users.models import CustomUser


class UserBalance(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	value = models.IntegerField(default=1000, validators=[MinValueValidator(0)])

	class Meta:
		verbose_name = 'Баланс пользователя'
		ordering = ('-id',)

	def __str__(self):
		return self.name

	@property
	def value(self):
		return self.value

	@value.setter
	def value(self, new_value):
		if new_value < 0:
			raise ValueError("[UserProducts] def value(self, new_value): new_value имеет отрицательное значение.")
		self._value = new_value
