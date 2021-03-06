# Generated by Django 3.2.8 on 2021-11-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_book_img_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('number', models.PositiveIntegerField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=100, null=True)),
                ('comment', models.TextField()),
                ('book_req', models.CharField(max_length=50)),
            ],
        ),
    ]
