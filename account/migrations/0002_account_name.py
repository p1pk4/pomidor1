# Generated by Django 4.0.3 on 2022-04-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default='from account_models', max_length=100),
        ),
    ]