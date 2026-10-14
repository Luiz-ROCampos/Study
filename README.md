Study

Aplicação web desenvolvida com Python e Django para ajudar estudantes a estudar por meio de flashcards.

Funcionalidades
Cadastro e login de estudantes.
Criação de flashcards com pergunta, resposta, categoria e nível de dificuldade.
Filtro de flashcards por categoria e dificuldade.
Criação de desafios, escolhendo título, categoria, dificuldade e quantidade de perguntas.
Listagem dos desafios criados.
Ao responder um desafio, acompanhamento de estatísticas em tempo real: total de acertos, total de erros e quantidade de perguntas restantes.
Relatório detalhado em gráfico, com perguntas acertadas e erradas e as matérias incluídas no teste.
Módulos

O projeto é dividido em apps Django, cada um com sua responsabilidade:

App	Função
usuarios	Cadastro e autenticação dos estudantes
flashcard	Criação de flashcards, desafios e relatórios de desempenho
core	Configurações do projeto e roteamento de URLs
Tecnologias
Python 3.12 ou superior
Django
SQLite
HTML e CSS nos templates
Como executar localmente

Pré-requisito: Python 3.12 ou superior e Git instalados.

bash
# 1. Clonar o repositório
git clone https://github.com/Luiz-ROCampos/Study.git
cd Study

# 2. Criar e ativar o ambiente virtual
python -m venv .venv
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux ou macOS:
source .venv/bin/activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Criar as tabelas do banco de dados
python manage.py migrate

# 5. Criar um usuário administrador
pode usuar o: adm , senha: 1234

python manage.py createsuperuser

para usar um usuário comum: luiz , senha: 1234

# 6. Iniciar o servidor
python manage.py runserver

Depois, acesse http://127.0.0.1:8000 para usar a aplicação, ou http://127.0.0.1:8000/admin/ para o painel administrativo.



Estrutura do projeto
Study/
├── core/            # configurações (settings.py), URLs e WSGI
├── usuarios/         # app de cadastro e autenticação
├── flashcard/        # app de flashcards, desafios e relatórios
├── templates/         # templates HTML compartilhados
├── manage.py
└── README.md
Autor

Luiz Ricardo, graduado em Gestão da Tecnologia da Informação, em transição para o desenvolvimento back-end com Python.

Portfólio: https://luiz-rocampos.github.io
LinkedIn: https://www.linkedin.com/in/luiz-rocampos
