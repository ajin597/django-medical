# Generated by Django 5.0.2 on 2024-03-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MedicineName', models.CharField(max_length=500)),
                ('Description', models.TextField()),
                ('ExpiryDate', models.DateField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
