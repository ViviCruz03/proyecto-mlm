# Generated by Django 4.0.6 on 2025-03-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0013_alter_consulta_supervisor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
