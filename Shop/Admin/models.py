from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=60)
    categorys = [
        ["mb", "Мебель"],
        ["dr", "Одежда"],
        ["el", "Электроника"],
        ["ot", "Другое"]
    ]
    Category = models.CharField(max_length=50, choices=categorys)
    Price = models.PositiveIntegerField()
    status = [
        ["false", "Куплено"],
        ["true", "Не куплено"]
    ]
    Status = models.CharField(max_length=50, choices=status)
    Date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.Name}"

    def get_absolute_url(self):
        return reverse("product_name", args=self.pk)
