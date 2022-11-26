from django.db import models



class Shop(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Ürün Adı", help_text="Ürün adını giriniz")
    price = models.CharField(max_length=10, verbose_name="Fiyat")
    image = models.ImageField(null=True, blank=True, upload_to="shop", verbose_name="Resim")

    def __str__(self):
        return self.name