# Generated by Django 4.1.7 on 2023-06-29 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name': 'servicios La Coruña'},
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='Servicio'),
        ),
    ]