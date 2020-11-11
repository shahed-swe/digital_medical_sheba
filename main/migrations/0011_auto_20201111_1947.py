# Generated by Django 3.1.3 on 2020-11-11 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201111_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='doctoruser', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
