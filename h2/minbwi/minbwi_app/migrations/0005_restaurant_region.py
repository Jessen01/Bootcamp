# Generated by Django 4.1.1 on 2022-09-08 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minbwi_app', '0004_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='region',
            field=models.ForeignKey(default=None,  null=True,on_delete=django.db.models.deletion.CASCADE, to='minbwi_app.region'),
        ),
    ]
