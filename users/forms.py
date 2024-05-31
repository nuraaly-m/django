from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models

GENDER = (("Male", "Male"), ("Female", "Female"))


class CustomRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    city = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    experience = forms.IntegerField(required=True)
    telegram = forms.CharField(required=True)
    favorite_genre = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "name",
            "surname",
            "city",
            "gender",
            "phone_number",
            "age",
            "experience",
            "telegram",
            "favorite_genre",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
