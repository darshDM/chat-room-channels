# Generated by Django 3.1.4 on 2020-12-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20201208_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='member',
        ),
        migrations.AddField(
            model_name='room',
            name='group',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
