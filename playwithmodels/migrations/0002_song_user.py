# Generated by Django 3.2.8 on 2021-10-23 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playwithmodels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='playwithmodels.user'),
        ),
    ]
