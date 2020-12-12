# Generated by Django 3.1.2 on 2020-11-26 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20201126_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportProblem',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.patient')),
                ('problem', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'problem_reports',
            },
        ),
    ]