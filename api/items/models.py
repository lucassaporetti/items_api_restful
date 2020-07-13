import uuid
from django.db import models


# Create your models here.
class Item(models.Model):
    objects = None
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    name = models.CharField(max_length=50, default='Without Name')
    category = models.CharField(max_length=50, default='STANDARD')
    item_type = models.CharField(max_length=50, default='UNIQUE')
    description = models.CharField(max_length=1000, default='Without Description')
    attributes = models.CharField(max_length=50, default='NONE')
    consume_mp = models.IntegerField(default=0)
    consume_heart = models.IntegerField(default=0)
    statistics_hp = models.IntegerField(default=0)
    statistics_mp = models.IntegerField(default=0)
    statistics_heart = models.IntegerField(default=0)
    statistics_str = models.IntegerField(default=0)
    statistics_att = models.IntegerField(default=0)
    statistics_gold = models.IntegerField(default=0)
    statistics_con = models.IntegerField(default=0)
    statistics_def = models.IntegerField(default=0)
    statistics_max_ht = models.IntegerField(default=0)
    statistics_int = models.IntegerField(default=0)
    statistics_lck = models.IntegerField(default=0)
    statistics_max_hp = models.IntegerField(default=0)
    sell = models.FloatField(default=0.0)
    found_at = models.CharField(max_length=100, default='NONE')
    dropped_by = models.CharField(max_length=100, default='NONE')
    effect = models.CharField(max_length=1000, default='Without Effect')
    image = models.ImageField(default='Without Image')
    animation = models.ImageField(default='Without Animation')
    special_animation = models.ImageField(default='Without Special Animation')

    def __str__(self):
        return self.name
