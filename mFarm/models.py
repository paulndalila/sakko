from django.db import models


# Create your models here.
class Sacco(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    # TODO("email & phone validation")

    def __str__(self):
        return self.name


class Farmer(models.Model):
    # TODO("farmer to be user)
    name = models.CharField(max_length=50)
    sacco = models.ForeignKey(Sacco, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)

    # TODO("email & phone validation)
    def __str__(self):
        return self.name


class MilkStatus(models.Model):
    FRESH = "fresh"
    SPOILT = "spoilt"
    MILK_STATUS_CHOICES = [
        (FRESH, 'Fresh'),
        (SPOILT, 'Spoilt'),

    ]

    status = models.CharField(
        max_length=7,
        choices=MILK_STATUS_CHOICES,
        default=FRESH
    )

    # spoilt = models.BooleanField(default=False)

    def __str__(self):
        return self.status


class Milk(models.Model):
    status = models.ForeignKey(MilkStatus, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    quantity = models.FloatField()

    # date = models.DateField()
    # price

    def __str__(self):
        return "{} litres of {} milk from {}".format(self.quantity, self.status, self.farmer)


class MilkCollection(models.Model):
    dateCollected = models.DateTimeField(auto_now_add=True)
    milk_collected = models.ForeignKey(Milk, on_delete=models.SET_NULL, null=True)
    # quantityCollected = models.DecimalField(max_digits=5, decimal_places=2)
    # saccoCollected = models.ForeignKey(Sacco, on_delete=models.CASCADE)
    farmerCollected = models.ForeignKey(Farmer, on_delete=models.CASCADE)


def __str__(self):
    return self.dateCollected
