from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
class Category(models.Model):
    title = models.CharField('Title', max_length = 255)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField('Title', max_length = 255)
    news = models.TextField('News')
    imgURL = models.CharField('URL', max_length = 255)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, related_name = "categoty", on_delete = models.SET_NULL, default = None, null = True, blank = True)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Title', max_length = 255, null = True)
    @receiver(post_save, sender = User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender = User)
    def save_user(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user = instance)

    