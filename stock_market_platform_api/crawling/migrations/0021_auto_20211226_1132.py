# Generated by Django 3.0.5 on 2021-12-26 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0020_financialstatementfact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashflowfield',
            name='crawling_source',
        ),
        migrations.RemoveField(
            model_name='cashflowfield',
            name='normalized_field',
        ),
        migrations.RemoveField(
            model_name='incomestatementfield',
            name='crawling_source',
        ),
        migrations.RemoveField(
            model_name='incomestatementfield',
            name='normalized_field',
        ),
        migrations.DeleteModel(
            name='BalanceSheetField',
        ),
        migrations.DeleteModel(
            name='CashFlowField',
        ),
        migrations.DeleteModel(
            name='IncomeStatementField',
        ),
    ]
