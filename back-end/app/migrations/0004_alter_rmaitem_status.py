# Generated by Django 4.2.6 on 2023-11-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_rmaitem_resolution_alter_rmaitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmaitem',
            name='status',
            field=models.CharField(choices=[('Recibidos', 'Recibidos'), ('En Taller', 'En Taller'), ('Reparado', 'Reparado')], max_length=20),
        ),
    ]
