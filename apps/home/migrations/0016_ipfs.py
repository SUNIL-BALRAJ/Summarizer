# Generated by Django 3.2.6 on 2023-07-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_summary_file_slider_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='ipfs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_hash', models.CharField(default=True, max_length=100)),
            ],
        ),
    ]
