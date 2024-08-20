from django.contrib.auth.models import AbstractUser
from groups.models import Group
from django.db import models


class CustomUser(AbstractUser):
	"""Кастомная модель пользователя - студента."""

	email = models.EmailField(
		verbose_name='Адрес электронной почты',
		max_length=250,
		unique=True
	)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = (
		'username',
		'first_name',
		'last_name',
		'password'
	)

	group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		ordering = ('-id',)

	def __str__(self):
		return self.get_full_name()
