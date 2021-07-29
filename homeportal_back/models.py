from django.db import models
from django.utils import timezone

from enum import Enum


# General TODO:
# Validators (https://docs.djangoproject.com/en/dev/ref/validators/)
# Authentication fields for user
# S3 image storage
# Field type for user avatar


class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateTimeField()
    avatar_uuid = models.UUIDField(blank=True)

    def __str__(self):
        return f'Username: {self.username}, email: {self.email}'


class Role(models.Model):
    class RoleNames(Enum):
        USER = 'usr'
        ADMIN = 'adm'
        MODERATOR = 'mod'

    users = models.ManyToManyField(User)
    name = models.CharField(max_length=16, default=RoleNames.USER)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Invitation(models.Model):
    token = models.CharField(max_length=64)
    expiration_date = models.DateTimeField()


class Post(models.Model):
    # User deletion is restricted so the post remain linked to their authors
    publisher = models.ForeignKey(User, on_delete=models.RESTRICT)
    creation_date = models.DateTimeField()
    text = models.TextField(blank=True)

    def __str__(self):
        return f'Post from {self.publisher} on {self.creation_date}'


class Video(models.Model):
    link = models.URLField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.link


class Image(models.Model):
    # TODO: decide what field type S3 path will have
    s3_path = models.FileField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.s3_path
