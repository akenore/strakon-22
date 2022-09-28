# Generated by Django 2.1.15 on 2021-06-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0028_journeeutilisateur2021_selected_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.IntegerField(verbose_name='Ajouter Date de jour')),
            ],
            options={
                'verbose_name': 'Ajouter Date de jour',
                'verbose_name_plural': 'Ajouter Les Dates de jours',
            },
        ),
        migrations.RemoveField(
            model_name='journeeutilisateur2021',
            name='selected_date',
        ),
        migrations.AddField(
            model_name='journeeutilisateur2021',
            name='selected_date',
            field=models.ManyToManyField(to='frontend.SelectDate'),
        ),
    ]