# Generated by Django 4.0.3 on 2022-04-10 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_name'),
        ('orders', '0006_alter_salesorder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]
