# Generated by Django 4.0.6 on 2025-03-14 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_Cons', models.CharField(max_length=200, verbose_name='Consulta')),
                ('fecha_Cons', models.DateField(verbose_name='Fecha')),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.asesor', verbose_name='Asesor')),
                ('uniEc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.unieconomicas', verbose_name='Unidades Economicas')),
            ],
        ),
    ]
