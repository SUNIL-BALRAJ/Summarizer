# Generated by Django 3.2.6 on 2023-07-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20230728_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary_file',
            name='uploadAudio',
        ),
        migrations.AddField(
            model_name='summary_file',
            name='p_num',
            field=models.CharField(default=True, max_length=10),
        ),
    ]
