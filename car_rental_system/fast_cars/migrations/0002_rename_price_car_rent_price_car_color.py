# Generated by Django 4.1.7 on 2023-06-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='price',
            new_name='rent_price',
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='Black', max_length=50),
        ),
    ]
