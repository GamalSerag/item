from django.db import models

class MenuItemExtra(models.Model):
    title = models.CharField(max_length=100)

class MenuItemExtraItem(models.Model):
    extra = models.ForeignKey(MenuItemExtra, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Item(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    extras = models.ManyToManyField(MenuItemExtra, blank=True)

    def __str__(self):
        return self.name