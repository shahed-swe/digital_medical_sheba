# Generated by Django 3.1.4 on 2020-12-21 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_patienthealthreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportproblem',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='ReportProblem',
        ),
    ]