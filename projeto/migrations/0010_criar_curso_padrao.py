from django.db import migrations

def criar_curso_padrao(apps, schema_editor):
    Curso = apps.get_model('projeto', 'Curso')
    if not Curso.objects.exists():  # Evita duplicações
        Curso.objects.create(nome="Informática para Internet", descricao="Curso fixo de TI")

class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0009_curso_descricao_alter_curso_nome_and_more'),  # Substitua pelo nome da última migração antes dessa
    ]

    operations = [
        migrations.RunPython(criar_curso_padrao),
    ]