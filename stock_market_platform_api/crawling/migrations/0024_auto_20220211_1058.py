# Generated by Django 3.0.5 on 2022-02-11 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0023_auto_20220211_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialstatementline',
            name='normalized_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crawling.NormalizedFieldTree'),
        ),
    ]
