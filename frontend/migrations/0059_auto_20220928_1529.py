# Generated by Django 2.1.15 on 2022-09-28 15:29

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0058_auto_20220928_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batimat',
            name='state',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='country', chained_model_field='country', on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
    ]
