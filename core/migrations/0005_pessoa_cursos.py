# Generated by Django 4.2 on 2023-04-12 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
        ('core', '0004_telefone_padrao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='cursos',
            field=models.ManyToManyField(to='curso.curso'),
        ),
    ]
