# Generated by Django 4.2.6 on 2023-11-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_technician_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmaitem',
            name='technicians',
            field=models.ManyToManyField(blank=True, to='app.technician'),
        ),
        migrations.AlterField(
            model_name='technician',
            name='rma_items',
            field=models.ManyToManyField(blank=True, to='app.rmaitem'),
        ),
    ]
