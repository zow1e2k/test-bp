from django.core.validators import MinValueValidator
from django.db import models
from users.models import CustomUser



class UserBalance(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	balance_value = models.IntegerField(default=1000, validators=[MinValueValidator(0)])

	class Meta:
		verbose_name = 'Баланс пользователя'
		ordering = ('-id',)

	def __str__(self):
		print(f'UserBalance __str__ called for value: {self.balance_value}')
		return str(self.balance_value)

	@property
	def value(self):
		return self.balance_value

	@value.setter
	def value(self, new_value):
		if new_value < 0:
			raise ValueError("[UserProducts] def value(self, new_value): new_value имеет отрицательное значение.")
		self.balance_value = new_value

def create_user_balance(user: CustomUser):
	result = UserBalance.objects.create(user=user)
	return result
