# Generated by Django 3.2 on 2021-05-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0005_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockd',
            name='lastprice',
            field=models.FloatField(null=True),
        ),
    ]
