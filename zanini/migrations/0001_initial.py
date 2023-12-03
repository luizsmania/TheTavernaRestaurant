# Generated by Django 4.2.7 on 2023-11-20 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('booking_time', models.CharField(choices=[('2', ' 2pm to 3pm'), ('3', ' 3pm to 4pm'), ('4', ' 4pm to 5pm'), ('5', ' 5pm to 6pm'), ('6', ' 6pm to 7pm'), ('7', ' 7pm to 8pm'), ('8', ' 8pm to 9pm')], max_length=1)),
                ('table_size', models.CharField(choices=[('2', 'Table for two'), ('4', 'Table for four'), ('6', 'Table for six')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]