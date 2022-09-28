# Generated by Django 2.1.15 on 2022-09-28 15:44

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0010_auto_20200508_1851'),
        ('frontend', '0062_auto_20220928_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batimat',
            old_name='country',
            new_name='pays',
        ),
        migrations.RemoveField(
            model_name='batimat',
            name='state',
        ),
        migrations.AddField(
            model_name='batimat',
            name='ville',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='pays', chained_model_field='country', default=1, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
            preserve_default=False,
        ),
    ]