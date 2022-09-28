# Generated by Django 2.1.15 on 2021-05-10 09:54

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Publié')),
                ('name', models.CharField(max_length=50, verbose_name='Titre')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('name',))),
                ('image', models.ImageField(default='logo-home.jpg', upload_to='video/', verbose_name='Image principale')),
                ('language', models.CharField(max_length=50, verbose_name='Langue de vidéo')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
    ]