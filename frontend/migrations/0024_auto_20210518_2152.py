# Generated by Django 2.1.15 on 2021-05-18 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0023_auto_20210518_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Titre'),
        ),
    ]