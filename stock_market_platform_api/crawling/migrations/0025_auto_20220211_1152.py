# Generated by Django 3.0.5 on 2022-02-11 11:52

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0024_auto_20220211_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialstatementline',
            name='normalized_field',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crawling.NormalizedFieldTree'),
        ),
    ]
