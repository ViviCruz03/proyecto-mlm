# Generated by Django 4.0.6 on 2025-03-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_remove_unieconomicas_clase_uniec_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unieconomicas',
            name='idUni',
        ),
    ]
