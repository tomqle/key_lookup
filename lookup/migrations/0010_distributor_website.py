# Generated by Django 3.2.6 on 2022-01-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0009_auto_20211216_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='website',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
