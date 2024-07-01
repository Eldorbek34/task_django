from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator,MaxLengthValidator

class Book(models.Model):
    title = models.CharField("Nom", max_length=255)
    isbn = models.PositiveIntegerField(verbose_name="ISBN kodi")
    qty = models.PositiveIntegerField(verbose_name="Bazadagi soni", default=0)
    price = models.IntegerField(verbose_name="Narxi", default=0)
    image = models.ImageField(upload_to="book_images", null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        print(vars(self))
        self.title = self.title.upper
        return super().save(*args, *kwargs)




class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="sales")
    qty = models.PositiveIntegerField("Sotilgan soni", default=0)
    price = models.IntegerField(verbose_name="Sotilgan narxi", default=0)
    total_price = models.IntegerField(verbose_name="Umumiy savdo", default=0)
    image = models.ImageField(upload_to="book_image", null=True, blank=True)


    created_at = models.DateTimeField("Savdo sanasi", auto_now=True)

    def clean(self) -> None:
        book = self.book
        if book.qty < self.qty:
            raise ValidationError(
                {
                    "qty": "Yetarli kitob mavjud emas"
                }
            )

        return super().clean()

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            qty = self.qty
            book = self.book

            self.price = book.price
            self.total_price = book.price * qty

            book.qty = book.qty - qty
            book.save()

        return super().save(*args, *kwargs)



