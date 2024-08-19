from django.db import models

class Lesson(models.Model):
	name = models.CharField(max_length=64, verbose_name='Название урока')
	video_url = models.URLField(verbose_name='Ссылка на обучающее видео')

	class Meta:
		verbose_name = 'Урок'
		verbose_name_plural = 'Уроки'
		ordering = ('-id',)

	def __str__(self):
		return self.name