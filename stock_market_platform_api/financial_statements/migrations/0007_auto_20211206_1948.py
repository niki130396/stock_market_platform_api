# Generated by Django 3.0.5 on 2021-12-06 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_statements', '0006_auto_20211206_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statementsmetadata',
            old_name='is_financial_statement_available',
            new_name='is_income_statement_available',
        ),
    ]
