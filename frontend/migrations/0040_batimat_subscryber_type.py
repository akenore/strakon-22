# Generated by Django 2.1.15 on 2022-09-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0039_batimat'),
    ]

    operations = [
        migrations.AddField(
            model_name='batimat',
            name='subscryber_type',
            field=models.CharField(choices=[('1', 'Particulier'), ('2', 'Étudiant'), ('3', 'Société')], default=1, max_length=10, verbose_name="S'inscrire au temps que"),
            preserve_default=False,
        ),
    ]
