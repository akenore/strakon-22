# Generated by Django 2.1.15 on 2021-05-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_auto_20210512_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenceetablissement',
            name='commande',
            field=models.CharField(choices=[('Licence', 'Licence'), ('Mise à jour', 'Mise à jour')], default='Licence', max_length=50, verbose_name='Commandez'),
        ),
        migrations.AlterField(
            model_name='licenceetudiant',
            name='commande',
            field=models.CharField(choices=[('Licence', 'Licence'), ('Mise à jour', 'Mise à jour')], default='Licence', max_length=50, verbose_name='Commandez'),
        ),
    ]
