from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploader = models.ForeignKey(User, related_name = "uploaded_books")
class Likes(models.Model):
    user = models.ForeignKey(User, related_name = "liked_books")
    book = models.ForeignKey(Book, related_name = "liked_users")

#Book.objects.first().uploader - this should return the user who uploaded the book
#User.objects.first().uploaded_books - this should return all the books that are uploaded by the first user
#Book.objects.first().liked_users - this should return all the users who liked the first book
#User.objects.first().liked_books - this should return all the books that were liked by the first user