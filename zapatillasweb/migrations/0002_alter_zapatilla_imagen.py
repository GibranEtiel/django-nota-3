# Generated by Django 5.0.6 on 2024-07-03 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapatillasweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapatilla',
            name='imagen',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
