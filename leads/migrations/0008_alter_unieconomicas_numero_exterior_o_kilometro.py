# Generated by Django 4.0.6 on 2025-03-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_alter_unieconomicas_letra_exterior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unieconomicas',
            name='Numero_exterior_o_kilometro',
            field=models.CharField(max_length=20, null=True, verbose_name='Numero exterior'),
        ),
    ]
