from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from users.user_subscriptions.models import UserSubscription


@receiver(post_save, sender=UserSubscription)
def post_save_subscription(sender, instance: UserSubscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.

    """

    if created:
        pass
        # TODO
