from django.db import models

# Create your models here.


class Summarize(models.Model):

    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=50, verbose_name='Başlık')
    content = models.TextField(verbose_name='Metin')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Oluşturulan Tarih')


class Stemmer(models.Model):

    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    text = models.TextField(verbose_name='Metin')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Oluşturulan Tarih')


class Lemmatizer(models.Model):

    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    text = models.TextField(verbose_name='Metin')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Oluşturulan Tarih')


class StopWordRemove(models.Model):

    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    text = models.TextField(verbose_name='Metin')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Oluşturulan Tarih')
