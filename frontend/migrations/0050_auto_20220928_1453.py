# Generated by Django 2.1.15 on 2022-09-28 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0049_auto_20220928_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batimat',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country'),
        ),
    ]