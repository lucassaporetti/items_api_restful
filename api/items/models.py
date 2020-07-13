import uuid
from django.db import models


# Create your models here.
from django.forms import forms


class Item(models.Model):
    objects = None
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default='Without Name', blank=True)
    category = models.CharField(max_length=50, default='STANDARD', blank=True)
    item_type = models.CharField(max_length=50, default='UNIQUE', blank=True)
    description = models.CharField(max_length=1000, default='Without Description', blank=True)
    attributes = models.CharField(max_length=50, default='NONE', blank=True)
    consume_mp = models.IntegerField(default=0, null=True)
    consume_heart = models.IntegerField(default=0, null=True)
    statistics_hp = models.IntegerField(default=0, null=True)
    statistics_mp = models.IntegerField(default=0, null=True)
    statistics_heart = models.IntegerField(default=0, null=True)
    statistics_str = models.IntegerField(default=0, null=True)
    statistics_att = models.IntegerField(default=0, null=True)
    statistics_gold = models.IntegerField(default=0, null=True)
    statistics_con = models.IntegerField(default=0, null=True)
    statistics_def = models.IntegerField(default=0, null=True)
    statistics_max_ht = models.IntegerField(default=0, null=True)
    statistics_int = models.IntegerField(default=0, null=True)
    statistics_lck = models.IntegerField(default=0, null=True)
    statistics_max_hp = models.IntegerField(default=0, null=True)
    sell = models.FloatField(default=0.0, null=True)
    found_at = models.CharField(max_length=100, default='NONE', blank=True)
    dropped_by = models.CharField(max_length=100, default='NONE', blank=True)
    effect = models.CharField(max_length=1000, default='Without Effect', blank=True)
    image = models.ImageField(default='Without Image', null=True)
    animation = models.ImageField(default='Without Animation', null=True)
    special_animation = models.ImageField(default='Without Special Animation', null=True)

    def __str__(self):
        return self.name
