from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LineItem(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )