# Generated by Django 3.0.5 on 2021-03-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_statements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatementsMetaData',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('market_cap', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('ipo_year', models.IntegerField(blank=True, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('sector', models.CharField(blank=True, max_length=255, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SomeTable',
        ),
    ]
