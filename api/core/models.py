from django.db import models

# Create your models here.


class Item(models.Model):
    ENTITY_ID = models.CharField(max_length=36)
    NAME = models.CharField(max_length=50)
    CATEGORY = models.CharField(max_length=50)
    ITEM_TYPE = models.CharField(max_length=50)
    DESCRIPTION = models.CharField(max_length=1000)
    ATTRIBUTES = models.CharField(max_length=50)
    CONSUME_MP = models.IntegerField()
    CONSUME_HEART = models.IntegerField()
    STATISTICS_HP = models.IntegerField()
    STATISTICS_MP = models.IntegerField()
    STATISTICS_HEART = models.IntegerField()
    STATISTICS_STR = models.IntegerField()
    STATISTICS_ATT = models.IntegerField()
    STATISTICS_GOLD = models.IntegerField()
    STATISTICS_CON = models.IntegerField()
    STATISTICS_DEF = models.IntegerField()
    STATISTICS_MAX_HT = models.IntegerField()
    STATISTICS_INT = models.IntegerField()
    STATISTICS_LCK = models.IntegerField()
    STATISTICS_MAX_HP = models.IntegerField()
    SELL = models.IntegerField()
    FOUND_AT = models.CharField(max_length=100)
    DROPPED_BY = models.CharField(max_length=100)
    EFFECT = models.CharField(max_length=1000)
    IMAGE = models.CharField(max_length=1000)
    ANIMATION = models.CharField(max_length=1000)
    SPECIAL_ANIMATION = models.CharField(max_length=1000)

    def __str__(self):
        return self.NAME
