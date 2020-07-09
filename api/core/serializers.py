from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['ENTITY_ID', 'NAME', 'CATEGORY', 'ITEM_TYPE', 'DESCRIPTION', 'ATTRIBUTES',
                  'CONSUME_MP', 'CONSUME_HEART', 'STATISTICS_HP', 'STATISTICS_MP', 'STATISTICS_HEART',
                  'STATISTICS_STR', 'STATISTICS_ATT', 'STATISTICS_GOLD', 'STATISTICS_CON', 'STATISTICS_DEF',
                  'STATISTICS_MAX_HT', 'STATISTICS_INT', 'STATISTICS_LCK', 'STATISTICS_MAX_HP', 'SELL',
                  'FOUND_AT', 'DROPPED_BY', 'EFFECT', 'IMAGE', 'ANIMATION', 'SPECIAL_ANIMATION']
