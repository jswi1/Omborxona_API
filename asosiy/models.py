from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    dokon = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ism} ({self.dokon})'

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    miqdor = models.SmallIntegerField()
    brend = models.CharField(max_length=50)
    kelgan_narx = models.IntegerField()
    sotuv_narx = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} ({self.brend})'

class Stats(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    umumiy = models.IntegerField()
    tolandi = models.IntegerField()
    miqdor = models.IntegerField()
    nasiya = models.IntegerField()
    sana = models.DateTimeField()
    foyda = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)


class Ombor(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    dokon = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.ism} ({self.dokon})"
