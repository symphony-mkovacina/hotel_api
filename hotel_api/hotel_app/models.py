from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models
from location_field.models.plain import PlainLocationField

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/no-img.jpg')
    stars = models.IntegerField()
    description = models.TextField(max_length=2000)
    price = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    user = models.ManyToManyField(User)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.name + ', ' + self.city + ' - ' + self.country


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    positive = models.BooleanField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.first_name + ' ' + self.author.last_name + ' - ' + str(self.created_at.date())


class Counter(models.Model):
    name = models.CharField(max_length=20)
    hit_count = models.IntegerField()


class Favorite(models.Model):
    hotel_id = models.IntegerField()
    is_favorite = models.BooleanField()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

