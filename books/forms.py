from django import forms
from . import models


class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = [
            "title",
            "author",
            "image",
            "description",
            "genre",
            "price",
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["book", "stars", "text"]