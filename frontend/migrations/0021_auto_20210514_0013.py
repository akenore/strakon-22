# Generated by Django 2.1.15 on 2021-05-14 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0020_auto_20210513_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nom'),
        ),
    ]
