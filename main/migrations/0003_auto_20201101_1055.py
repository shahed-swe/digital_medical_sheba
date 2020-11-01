# Generated by Django 3.1.2 on 2020-11-01 04:55

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('main', '0002_auto_20201030_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_assistant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_nurse',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
    ]
