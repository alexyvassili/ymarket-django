from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='products_images/', blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "{} {}".format(self.name, self.price)
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='products_images/')
#     is_main = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     def __str__(self):
#         return "{}.".format(self.id)
#     class Meta:
#         verbose_name = "Фотография"
#         verbose_name_plural = "Фотографии"