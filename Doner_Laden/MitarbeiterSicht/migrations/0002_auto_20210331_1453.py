# Generated by Django 3.1.7 on 2021-03-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MitarbeiterSicht', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourceproduct',
            name='catagory',
        ),
        migrations.AddField(
            model_name='resourceproduct',
            name='catagory',
            field=models.ManyToManyField(to='MitarbeiterSicht.ResourceCatagory'),
        ),
    ]
