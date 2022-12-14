# Generated by Django 4.0 on 2022-06-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_rename_employee_empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hablidades', models.CharField(max_length=50, verbose_name='Habilidades')),
            ],
            options={
                'verbose_name': 'Habilidades',
                'verbose_name_plural': 'Habilidades de Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['departamento'], 'verbose_name': 'Lista Personal', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('0', 'Otro'), ('1', 'Contador'), ('2', 'Administrador'), ('3', 'Vendedor')], max_length=1, verbose_name='Puesto'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='hablidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
