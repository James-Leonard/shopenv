# Generated by Django 4.1 on 2022-08-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
