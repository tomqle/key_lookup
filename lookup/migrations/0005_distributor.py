# Generated by Django 3.2.6 on 2021-12-16 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0004_remote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=16, null=True)),
            ],
        ),
    ]