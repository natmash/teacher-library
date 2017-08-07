from django.db import models
from django.contrib.auth.models import User
import uuid

class Student(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    total_checkouts = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    cover = models.ImageField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    times_checked_out = models.IntegerField(editable=False,default=0)
    available = models.BooleanField(editable=False,default=True)++
    # checkout_history =
    # owner = models.ForeignKey(User, editable=False)

    def __unicode__(self):
        return self.title

class Checkout(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now=True)
    end = models.DateTimeField(editable=False, null=True, blank=True)