# Generated by Django 3.2.16 on 2023-05-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20230426_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy_energy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(default=True, max_length=20)),
                ('meter_id', models.IntegerField(default=True, max_length=100)),
                ('quantity', models.IntegerField(default=True)),
                ('energy_price', models.IntegerField(default=True)),
            ],
        ),
    ]
