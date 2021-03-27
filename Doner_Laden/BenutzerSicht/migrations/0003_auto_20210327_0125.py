# Generated by Django 3.1.7 on 2021-03-27 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BenutzerSicht', '0002_auto_20210325_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Catagories',
                'db_table': 'catagories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='uploads')),
                ('quantity', models.PositiveIntegerField()),
                ('catagory', models.ManyToManyField(to='BenutzerSicht.Catagory')),
            ],
        ),
        migrations.DeleteModel(
            name='Kunde',
        ),
    ]
