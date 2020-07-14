# Generated by Django 3.0.8 on 2020-07-14 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20200714_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='animation',
            field=models.CharField(default='Without Animation', max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(default='Without Image', max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='special_animation',
            field=models.CharField(default='Without Special Animation', max_length=50000, null=True),
        ),
    ]