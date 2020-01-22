# Generated by Django 2.2.9 on 2020-01-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kirim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kirim_destination', models.CharField(choices=[('CAI-KUL', 'Cairo to KL'), ('KUL-CAI', 'KL to Cairo')], default='CAI-KUL', max_length=10)),
                ('location', models.CharField(max_length=120)),
                ('submission_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=20.0, max_digits=4)),
                ('available_units', models.DecimalField(decimal_places=2, default=20.0, max_digits=4)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
