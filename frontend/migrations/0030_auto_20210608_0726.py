# Generated by Django 2.1.15 on 2021-06-08 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0029_auto_20210604_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journeeutilisateur2021',
            name='accompagnee',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Accompagnée de'),
        ),
    ]
