from django.db import models

# Create your models here.


class Item(models.Model):
    entity_id = models.CharField(max_length=36)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    item_type = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    attributes = models.CharField(max_length=50)
    consume_mp = models.IntegerField()
    consume_heart = models.IntegerField()
    statistics_hp = models.IntegerField()
    statistics_mp = models.IntegerField()
    statistics_heart = models.IntegerField()
    statistics_str = models.IntegerField()
    statistics_att = models.IntegerField()
    statistics_gold = models.IntegerField()
    statistics_con = models.IntegerField()
    statistics_def = models.IntegerField()
    statistics_max_ht = models.IntegerField()
    statistics_int = models.IntegerField()
    statistics_lck = models.IntegerField()
    statistics_max_hp = models.IntegerField()
    sell = models.IntegerField()
    found_at = models.CharField(max_length=100)
    dropped_by = models.CharField(max_length=100)
    effect = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    animation = models.CharField(max_length=1000)
    special_animation = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
