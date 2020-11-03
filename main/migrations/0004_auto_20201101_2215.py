# Generated by Django 3.1.2 on 2020-11-01 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('main', '0003_auto_20201101_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.patient')),
                ('bill', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'billing_information',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'feedback_section',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(blank=True, max_length=120, null=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'medicine_info',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterModelTable(
            name='assistant',
            table='assistant_info',
        ),
        migrations.AlterModelTable(
            name='doctor',
            table='doctor_info',
        ),
        migrations.AlterModelTable(
            name='nurse',
            table='nurse_info',
        ),
        migrations.AlterModelTable(
            name='patient',
            table='patient_info',
        ),
        migrations.CreateModel(
            name='assignNurse',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.patient')),
                ('nurse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assign_nurse', to='main.nurse')),
            ],
            options={
                'db_table': 'assigned_nurse',
            },
        ),
        migrations.CreateModel(
            name='assignMedicine',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.patient')),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assign_medicine', to='main.medicine')),
            ],
            options={
                'db_table': 'assigned_medicine',
            },
        ),
        migrations.CreateModel(
            name='assignAssistant',
            fields=[
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.doctor')),
                ('assistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assign_assistant', to='main.assistant')),
            ],
            options={
                'db_table': 'assigned_assistant',
            },
        ),
    ]