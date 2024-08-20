from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.user_subscriptions.models import UserSubscription
from groups.models import Group
#from groups.models import MAX_COURSE_GROUPS


@receiver(post_save, sender=UserSubscription)
def post_save_subscription(sender, instance: UserSubscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.
    """
    user = instance.user

    group_with_min_users = (
        Group.objects.annotate(user_count=Count('customuser'))
        .order_by('user_count')
        .first()
    )
    print(f"group_with_min_users: {group_with_min_users}")

    if group_with_min_users is not None:
        user.group = group_with_min_users
        user.save()
