# Generated by Django 5.1.6 on 2025-02-23 00:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0014_modulo_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topico',
            old_name='conteudo',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='modulo',
            name='descricao',
        ),
        migrations.AddField(
            model_name='modulo',
            name='ordem',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='projeto.disciplina'),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='nome',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='topico',
            name='modulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topicos', to='projeto.modulo'),
        ),
        migrations.AlterField(
            model_name='topico',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
