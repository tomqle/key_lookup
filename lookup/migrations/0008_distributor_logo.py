# Generated by Django 3.2.6 on 2021-12-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0007_alter_distributorkey_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/distributor_logos/'),
        ),
    ]