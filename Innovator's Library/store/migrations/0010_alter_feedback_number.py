# Generated by Django 3.2.8 on 2021-11-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20211110_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
