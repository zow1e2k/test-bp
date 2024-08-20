
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from products.models import Product
from products.lessons.models import Lesson
from django.test import Client
from users.user_products.models import UserProducts


class ProductAPITests(APITestCase):
	def setUp(self):
		self.user = CustomUser.objects.create_user(
			username="genius",
			email="genius@gmail.com",
			password="777555",
			first_name="Genius",
			last_name="Geniously"
		)
		print(self.user)
		print(self.user.is_active)
		self.client = Client()

		self.user_products = UserProducts.objects.create(
			user=self.user,
		)

		self.lessons = []
		self.lessons.append(Lesson.objects.create(
			name='Тестовый урок 1',
			video_url ='https://github.com/zow1e2k'
		))
		self.lessons.append(Lesson.objects.create(
			name='Тестовый урок 2',
			video_url='https://github.com/zow1e2k'
		))

		self.products = []
		self.products.append(Product.objects.create(
			name='Тестовый продукт 1',
			date_created=timezone.now(),
			price=1000,
			creator=self.user,
			lesson=self.lessons[0]
		))

		self.products.append(Product.objects.create(
			name='Тестовый продукт 2',
			date_created=timezone.now(),
			price=1000,
			creator=self.user,
			lesson=self.lessons[1]
		))

		for product in self.products:
			if product.name == "Тестовый продукт 2":
				continue

			self.user_products.products.add(product)

	def test_available_products(self):
		self.client = Client()
		self.client.force_login(self.user)
		response = self.client.get(reverse('available-products-list'))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn('Тестовый продукт', str(response.content.decode('utf-8')))
		print(str(response.content.decode('utf-8')))