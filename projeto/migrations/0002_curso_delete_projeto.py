# Generated by Django 5.1.2 on 2025-02-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('duracao', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Projeto',
        ),
    ]
