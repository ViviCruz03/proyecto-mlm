# Generated by Django 4.0.6 on 2025-03-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_estado_consulta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unieconomicas',
            name='clase_uniEc',
        ),
        migrations.RemoveField(
            model_name='unieconomicas',
            name='codigoPos',
        ),
        migrations.RemoveField(
            model_name='unieconomicas',
            name='correp_uniEc',
        ),
        migrations.RemoveField(
            model_name='unieconomicas',
            name='direc_uniEc',
        ),
        migrations.RemoveField(
            model_name='unieconomicas',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='unieconomicas',
            name='long',
        ),
        migrations.RemoveField(
            model_name='unieconomicas',
            name='nom_uniEc',
        ),
        migrations.RemoveField(
            model_name='unieconomicas',
            name='status',
        ),
        migrations.RemoveField(
            model_name='unieconomicas',
            name='tel_uniEc',
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='CleeUni',
            field=models.CharField(max_length=100, null=True, verbose_name='Clee'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Codigo_postal',
            field=models.CharField(max_length=6, null=True, verbose_name='Codigo postal'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Correo_electronico',
            field=models.CharField(max_length=250, null=True, verbose_name='Correo'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Descripcion_estrato_personal_ocupado',
            field=models.CharField(max_length=300, null=True, verbose_name='Descripcion del estrato'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Entidad_federetiva',
            field=models.CharField(max_length=250, null=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Fecha_de_incorporacion_al_denue',
            field=models.DateField(null=True, verbose_name='Fecha de incorporación al denue'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Latitud',
            field=models.CharField(max_length=200, null=True, verbose_name='Latitud'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Letra_exterior',
            field=models.CharField(max_length=4, null=True, verbose_name='Letra exterior'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Localidad',
            field=models.CharField(max_length=250, null=True, verbose_name='Localidad'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Longitud',
            field=models.CharField(max_length=200, null=True, verbose_name='Longitud'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Municipio',
            field=models.CharField(max_length=250, null=True, verbose_name='Municipio'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Nombre_de_asentamiento_humano',
            field=models.CharField(max_length=250, null=True, verbose_name='Asentamiento humano'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Nombre_de_clase_de_la_actividad',
            field=models.CharField(max_length=250, null=True, verbose_name='Nombre de la clase de la actividad'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Nombre_de_la_Unidad_Economica',
            field=models.CharField(max_length=250, null=True, verbose_name='Nombre de la unidad Economica'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Nombre_de_la_vialidad',
            field=models.CharField(max_length=250, null=True, verbose_name='Nombre de la vialidad'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Numero_de_telefono',
            field=models.CharField(max_length=13, null=True, verbose_name='Telefono'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Numero_exterior_o_kilometro',
            field=models.CharField(max_length=4, null=True, verbose_name='Numero exterior'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Razon_social',
            field=models.CharField(max_length=250, null=True, verbose_name='Razón social'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='Sitio_en_Internet',
            field=models.CharField(max_length=250, null=True, verbose_name='Sitio web'),
        ),
        migrations.AddField(
            model_name='unieconomicas',
            name='idUni',
            field=models.CharField(max_length=50, null=True, verbose_name='ID'),
        ),
    ]
