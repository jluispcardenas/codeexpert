from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.name

class Challenge(models.Model):

    title = models.CharField(max_length=256, null=False)
    description = models.TextField(null=False)
    slug = models.SlugField(max_length=200,unique=True, null=True, blank=True)
    template = models.TextField(null=False)
    difficult = models.CharField(max_length=10, default="easy")
    submissions = models.IntegerField(null=True, default=0)
    accepted = models.IntegerField(null=True, default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    answers = models.ManyToManyField(
        User,
        through='Answer',
        related_name='challenges_answers'
    )

    def __str__(self):
        return '{}'.format(self.title)
  

class Answer(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)
    code = models.TextField(null=True)
    status = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
