# Generated by Django 3.1.3 on 2020-11-11 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201111_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='nurseuser', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]