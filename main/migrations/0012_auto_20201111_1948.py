# Generated by Django 3.1.3 on 2020-11-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201111_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
