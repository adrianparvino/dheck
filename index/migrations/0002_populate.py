# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from index.models import Card, Expansion
import json

def populate_cards(apps, schema_editor):
    cards = {}
    with open('cards.json') as cards_json:
        cards = json.load(cards_json)["data"]["cards"]

    for card in cards:
        Card(card_id=card["card_id"],
                clan=card["clan"],
                card_name=card["card_name"],
                rarity=card["rarity"],
                card_set_id=card["card_set_id"]
                ).save()

class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_cards),
    ]
