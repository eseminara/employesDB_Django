# Generated by Django 4.0 on 2022-06-09 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_habilidades_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habilidades',
            old_name='hablidades',
            new_name='habilidades',
        ),
    ]