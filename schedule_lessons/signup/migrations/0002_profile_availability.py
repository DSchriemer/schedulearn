# Generated by Django 2.0.3 on 2018-03-11 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='availability',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
