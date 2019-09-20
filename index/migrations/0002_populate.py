# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from index.models import Card, Expansion
import json

def populate_expansions(apps, schema_editor):
    expansions = {}
    with open('expansions.json') as expansions_json:
        expansions = json.load(expansions_json)

    for name, card_set_id in expansions.items():
        Expansion(
            card_set_id=card_set_id,
            name=name
        ).save()

def populate_cards(apps, schema_editor):
    cards = {}
    with open('cards.json') as cards_json:
        cards = json.load(cards_json)["data"]["cards"]

    for card in cards:
        if 70000 <= card['card_set_id'] < 80000:
            card['card_set_id'] = 70000

        Card(
            card_id=card["card_id"],
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
        migrations.RunPython(populate_expansions),
        migrations.RunPython(populate_cards)
    ]
