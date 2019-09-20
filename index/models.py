from django.db import models

# Create your models here.

class Card(models.Model):
    # Card ID
    card_id = models.IntegerField(primary_key=True)
    # Class
    clan = models.IntegerField()
    # Name
    card_name = models.CharField(max_length=64)
    # Rarity
    rarity = models.IntegerField()
    # Expansion
    card_set_id = models.IntegerField()

class Expansion(models.Model):
    # Expansion
    card_set_id = models.IntegerField()
    # Expansion Name
    expac_name = models.CharField(max_length=64)
