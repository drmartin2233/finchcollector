# Generated by Django 4.1.7 on 2023-03-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='age',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]