from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

