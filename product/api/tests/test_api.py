
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from products.models import Product
from products.lessons.models import Lesson
from django.test import Client


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

		self.lesson = Lesson.objects.create(
			name='Тестовый урок',
			video_url ='https://github.com/zow1e2k'
		)

		self.product = Product.objects.create(
			name='Тестовый продукт',
			date_created=timezone.now(),
			price=1000,
			creator=self.user,
			lesson=self.lesson
		)

	def test_available_products(self):
		self.client = Client()
		self.client.force_login(self.user)
		response = self.client.get(reverse('available-products-list'))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn('Тестовый продукт', str(response.content.decode('utf-8')))
		print(str(response.content.decode('utf-8')))