# Generated by Django 4.1 on 2022-08-09 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
