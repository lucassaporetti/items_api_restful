# Generated by Django 3.0.8 on 2020-07-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ENTITY_ID', models.CharField(max_length=36)),
                ('NAME', models.CharField(max_length=50)),
                ('CATEGORY', models.CharField(max_length=50)),
                ('ITEM_TYPE', models.CharField(max_length=50)),
                ('DESCRIPTION', models.CharField(max_length=1000)),
                ('ATTRIBUTES', models.CharField(max_length=50)),
                ('CONSUME_MP', models.IntegerField()),
                ('CONSUME_HEART', models.IntegerField()),
                ('STATISTICS_HP', models.IntegerField()),
                ('STATISTICS_MP', models.IntegerField()),
                ('STATISTICS_HEART', models.IntegerField()),
                ('STATISTICS_STR', models.IntegerField()),
                ('STATISTICS_ATT', models.IntegerField()),
                ('STATISTICS_GOLD', models.IntegerField()),
                ('STATISTICS_CON', models.IntegerField()),
                ('STATISTICS_DEF', models.IntegerField()),
                ('STATISTICS_MAX_HT', models.IntegerField()),
                ('STATISTICS_INT', models.IntegerField()),
                ('STATISTICS_LCK', models.IntegerField()),
                ('STATISTICS_MAX_HP', models.IntegerField()),
                ('SELL', models.IntegerField()),
                ('FOUND_AT', models.CharField(max_length=100)),
                ('DROPPED_BY', models.CharField(max_length=100)),
                ('EFFECT', models.CharField(max_length=1000)),
                ('IMAGE', models.CharField(max_length=1000)),
                ('ANIMATION', models.CharField(max_length=1000)),
                ('SPECIAL_ANIMATION', models.CharField(max_length=1000)),
            ],
        ),
    ]
