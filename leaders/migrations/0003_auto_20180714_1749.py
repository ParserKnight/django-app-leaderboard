# Generated by Django 2.0.7 on 2018-07-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0002_auto_20180714_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='posicion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participante',
            name='posicion_old',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
