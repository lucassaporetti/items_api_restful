from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['entity_id', 'name', 'category', 'item_type', 'description', 'attributes',
                  'consume_mp', 'consume_heart', 'statistics_hp', 'statistics_mp', 'statistics_heart',
                  'statistics_str', 'statistics_att', 'statistics_gold', 'statistics_con', 'statistics_def',
                  'statistics_max_ht', 'statistics_int', 'statistics_lck', 'statistics_max_hp', 'sell',
                  'found_at', 'dropped_by', 'effect', 'image', 'animation', 'special_animation']
