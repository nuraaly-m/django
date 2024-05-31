from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(User):
    GENDER = (("Male", "Male"), ("Female", "Female"))
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=14, default="+996")
    age = models.PositiveIntegerField(
        default=18, validators=[MinValueValidator(5), MaxValueValidator(99)]
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    experience = models.PositiveIntegerField(default=0)
    telegram = models.CharField(max_length=100, blank=True)
    favorite_genre = models.CharField(max_length=100)
    club = models.CharField(max_length=100, default="новичок")
