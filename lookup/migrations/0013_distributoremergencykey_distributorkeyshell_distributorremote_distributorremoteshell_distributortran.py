# Generated by Django 3.2.7 on 2023-01-24 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0012_transponderkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributorTransponderKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, max_length=1024)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.distributor')),
                ('transponder_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.transponderkey')),
            ],
            options={
                'unique_together': {('distributor', 'transponder_key')},
            },
        ),
        migrations.CreateModel(
            name='DistributorRemoteShell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, max_length=1024)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.distributor')),
                ('remote_shell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.remoteshell')),
            ],
            options={
                'unique_together': {('distributor', 'remote_shell')},
            },
        ),
        migrations.CreateModel(
            name='DistributorRemote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, max_length=1024)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.distributor')),
                ('remote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.remote')),
            ],
            options={
                'unique_together': {('distributor', 'remote')},
            },
        ),
        migrations.CreateModel(
            name='DistributorKeyShell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, max_length=1024)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.distributor')),
                ('key_shell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.keyshell')),
            ],
            options={
                'unique_together': {('distributor', 'key_shell')},
            },
        ),
        migrations.CreateModel(
            name='DistributorEmergencyKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, max_length=1024)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.distributor')),
                ('emergency_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lookup.emergencykey')),
            ],
            options={
                'unique_together': {('distributor', 'emergency_key')},
            },
        ),
    ]
