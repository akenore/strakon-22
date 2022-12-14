# Generated by Django 2.1.15 on 2021-05-10 10:22

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20210510_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Publié')),
                ('name', models.CharField(max_length=50, verbose_name='Titre')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('name',))),
                ('image', models.ImageField(default='default.jpg', upload_to='gallery/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallerys',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='blog/', verbose_name='Image principale'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='video/', verbose_name='Image principale'),
        ),
    ]
