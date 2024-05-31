from django.db import models

class Book(models.Model):

    GENRE_BOOKS = (
        ('Detective', 'Detective'),
        ('Horror', 'Horror'),
        ('Musical', 'Musical'),
        ('Fantasy', 'Fantasy')
    )

    title = models.CharField(max_length=100, verbose_name='enter the name of the book')
    author = models.CharField(max_length=100, verbose_name='enter the name of the author')
    genre = models.CharField(max_length=100, choices=GENRE_BOOKS, verbose_name='choose the genre of the book')
    image = models.ImageField(upload_to='images/', verbose_name='upload an image', blank=True)
    description = models.TextField(verbose_name='enter the description of the book')
    music = models.FileField(upload_to='audios/', verbose_name='upload an audio', blank=True)
    video = models.URLField(verbose_name='enter the url of the video', blank=True)
    price = models.PositiveIntegerField(verbose_name='enter the price of the book')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.created_at}'


