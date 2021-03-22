from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
# this is a signal fire after object is saved
# user will be sending the signal
# receiver will be a function that gets the signal and starts a task

# in this example, post_save is going to be run whenever something is saved
# as the sender is defined as User, whenever User is saved, we'll execute post_save


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # in this case we pass in the User as instance
    # receiver is a decorator we add to our instance
    # in this case, the signal is the receiver and this function is the task
    if created:
        Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # save the profile when user gets saved

