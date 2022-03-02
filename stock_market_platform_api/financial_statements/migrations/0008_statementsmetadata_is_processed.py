# Generated by Django 3.0.5 on 2021-12-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_statements', '0007_auto_20211206_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='statementsmetadata',
            name='is_processed',
            field=models.BooleanField(default=False, help_text='Signals if a symbol is currently being processed by a spider'),
        ),
    ]
