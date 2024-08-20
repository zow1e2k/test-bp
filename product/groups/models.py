from django.db import models
from typing import Final
MAX_COURSE_GROUPS: Final = 10


class Group(models.Model):

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)
