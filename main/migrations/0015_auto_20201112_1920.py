# Generated by Django 3.1.2 on 2020-11-12 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201111_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmedicine',
            name='medicine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_medicine', to='main.medicine'),
        ),
    ]
