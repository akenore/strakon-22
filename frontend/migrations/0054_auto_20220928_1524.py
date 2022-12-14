# Generated by Django 2.1.15 on 2022-09-28 15:24

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0053_auto_20220928_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batimat',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country'),
        ),
        migrations.AlterField(
            model_name='batimat',
            name='state',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='country', chained_model_field='city', on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
    ]
