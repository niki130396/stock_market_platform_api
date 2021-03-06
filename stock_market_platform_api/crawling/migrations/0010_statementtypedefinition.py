# Generated by Django 3.0.5 on 2021-09-12 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0009_auto_20210911_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatementTypeDefinition',
            fields=[
                ('statement_type_definition_id', models.AutoField(primary_key=True, serialize=False)),
                ('statement_type_name_from_source', models.CharField(max_length=256)),
                ('crawling_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawling.CrawlingSourceDetails')),
            ],
        ),
    ]
