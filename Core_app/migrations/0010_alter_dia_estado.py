# Generated by Django 4.1.3 on 2022-11-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core_app', '0009_alter_dia_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dia',
            name='estado',
            field=models.CharField(choices=[('Neutro', 'Neutro'), ('Passado', 'Passado'), ('Perdido', 'Perdido')], default=('Neutro', 'Neutro'), max_length=7),
        ),
    ]
