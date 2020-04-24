from django.db import models


# Create your models here.

class Fruit(models.Model):
    barcode = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=100, default='')
    variety = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.name}-{self.variety}'


class Country(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return f'{self.name}'


class Fabric(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    site = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.name}-{self.country}'


class FabricProduct(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = (('fruit', 'fabric'),)

    def __str__(self):
        return f'{self.fruit}-{self.fabric}'


class Diler(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=100)
    site = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class PriceList(models.Model):
    diler = models.ForeignKey(Diler, on_delete=models.CASCADE)
    fabric_product = models.ForeignKey(FabricProduct, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()

    class Meta:
        unique_together = (('diler', 'fabric_product'),)

    def __str__(self):
        return f'{self.price}-{self.diler}-{self.fabric_product}'
