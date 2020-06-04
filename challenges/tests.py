from datetime import date, timedelta

from django.test import TestCase
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

from faker import Factory


faker = Factory.create()

class ChallengeTests(TestCase):

    def setUp(self):
        pass


        