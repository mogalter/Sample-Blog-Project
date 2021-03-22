from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # defines a one to one relationship
    # to cascade means if the user is deleted, delete the profile
    # aka if the model this is linked to is deleted, delete this instance
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # specifies where we update the images and default picture

    def __str__(self):
        return self.user.username + "'s Profile"

    def save(self):
        # save override
        # run after model is saved
        super().save()  # execute parent save first to save data
        img = Image.open(self.image.path)  # opens image of current instance
        if img.height > 300 or img.width > 300: # resize procedure
            print("Resizing")
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)