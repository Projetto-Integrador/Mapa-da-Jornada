# **Mapa da Jornada**

Bem-vindo ao **Mapa da Jornada**, um projeto Django para auxiliar na jornada de aprendizado, mapeando disciplinas e permitindo que usuários autenticados se inscrevam de forma interativa. Este sistema foi desenvolvido para oferecer uma experiência fluida, com suporte a requisições AJAX para inscrições assíncronas.

## **Visão Geral**
O **Mapa da Jornada** é uma aplicação web que:

- Lista disciplinas associadas ao curso **"Informática para Internet"**.
- Permite que usuários logados se inscrevam em disciplinas usando **AJAX**.
- Exibe as disciplinas inscritas em uma página paginada.
- Restringe ações (**inscrição, cancelamento**) a usuários autenticados.

## **Integrantes do Projeto
- **Jean Lucas**
- **Thierry Henry**
- **Eduardo Maurício**

## **Tecnologias Utilizadas**
- **Django**: Framework backend para Python.
- **SQLite**: Banco de dados padrão (pode ser substituído por PostgreSQL ou outro).
- **HTML/CSS**: Templates frontend com **Tailwind CSS** (parcialmente integrado).
- **jQuery**: Para requisições **AJAX**.
- **Python**: Linguagem principal do backend.

## **Pré-requisitos**
- **Python 3.8+**
- **Django 4.x**
- **jQuery** (incluído via CDN no template)
- **Um navegador moderno**

## **Instalação**
### **Clone o Repositório:**
```bash
git clone https://github.com/Projetto-Integrador/Mapa-da-Jornada.git
```

### **Crie um Ambiente Virtual:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1     # Windows
```

### **Instale as Dependências:**
```bash
pip install django
```

### **Configure o Banco de Dados:**
```bash
python manage.py migrate
```

### **Crie um Superusuário:**
```bash
python manage.py createsuperuser
```

### **Rode o Servidor:**
```bash
python manage.py runserver
```
Acesse em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## **Funcionalidades**
### **Página Inicial (`/`)**
- Lista disciplinas do curso **"Informática para Internet"**.
- Botão **"Inscrever-se"** visível apenas para usuários logados.
- Usa **AJAX** para inscrição assíncrona:
  - **Mensagem de sucesso (verde)**: "Você se inscreveu em [Disciplina] com sucesso!"
  - **Mensagem de aviso (amarelo)**: "Você já está inscrito em [Disciplina]." (exibida no topo).
  - **Mensagem de erro (vermelho)**: Para falhas na requisição.

### **Minhas Disciplinas (`/minhasdisciplinas/`)**
- Exibe as disciplinas inscritas pelo usuário logado.
- Paginação com **3 itens por página**.
- Botão **"Cancelar Inscrição"** para remover disciplinas.

## **Autenticação**
- Usa o modelo **Usuario** personalizado em `contas/models.py`.
- Configurado em `settings.py` com `AUTH_USER_MODEL = 'contas.Usuario'`.
- **Requer login** para inscrição e acesso a `/minhasdisciplinas/`.

## **Como Usar**
### **Acesse a Página Inicial:**
- **Sem login**: Veja as disciplinas, mas sem opção de inscrição.
- **Com login**: Clique em **"Inscrever-se"** para adicionar disciplinas.

### **Inscreva-se em uma Disciplina:**
1. Faça login em `/accounts/login/`.
2. Na página inicial, clique em **"Inscrever-se"**. O botão desaparece, e uma mensagem aparece no topo.

### **Veja Suas Disciplinas:**
- Acesse `/minhasdisciplinas/` para visualizar e gerenciar suas inscrições.

## **Configuração Adicional**
### **Adicionar Disciplinas:**
Use o **admin (`/admin/`)** para criar disciplinas associadas ao curso **"Informática para Internet"**.
Exemplo:
```python
python manage.py shell
>>> from projeto.models import Curso, Disciplina
>>> curso = Curso.objects.get_or_create(nome="Informática para Internet")[0]
>>> Disciplina.objects.create(nome="Disciplina 1", curso=curso)
```

### **Personalizar Estilos:**
Edite `base.html` e os **CSS inline** para ajustar o design.

## **Depuração**
Logs no console do servidor mostram:
- **Index** - Usuário logado: `[username]` ou Anônimo.
- **Inscrição** - Usuário logado: `[username]`, Disciplina: `[nome]`, Criada: `[True/False]`.
- **Minhas Disciplinas** - Usuário logado: `[username]`, Inscrições: `[lista]`.

## **Contribuições**
1. Faça um **fork** do repositório.
2. Crie uma branch: `git checkout -b minha-feature`.
3. Commit suas mudanças: `git commit -m "Adiciona feature X"`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um **Pull Request**.

## **Licença**
Este projeto é de código aberto sob a licença **MIT**.
