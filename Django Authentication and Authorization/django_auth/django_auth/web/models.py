from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()


# class Profile(models.Model):
#     first_name = models.CharField(
#         max_length=30,
#     )
#
#     # ...
#
#     user = models.OneToOneField(
#         UserModel,
#     )


class Article(models.Model):

    title = models.CharField(
        max_length=30,
    )
