
# API Projeto Django

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-green.svg?logo=Django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)




## Instituições de Fomento e Parceria
[![Website IFB](https://img.shields.io/badge/Website-IFB-%23508C3C.svg?labelColor=%23C8102E)](https://www.ifb.edu.br/) 
[![Website ihwbr](https://img.shields.io/badge/Website-ihwbr-%23DAA520.svg?labelColor=%232E2E2E)](https://hardware.org.br/)

## Orientador 

[![LinkedIn Rodrigo Duran](https://img.shields.io/badge/LinkedIn-Rodrigo_Duran-%230077B5.svg?labelColor=%23FFFFFF&logo=linkedin)]()
[![GitHub rodrigoduranbfd](https://img.shields.io/badge/GitHub-rodrigoduranbfd_(Rodrugo_Duran)-%23181717.svg?logo=github&logoColor=white)](https://github.com/rodrigoduranbfd)


## Sumário

- [Visão Geral](#visão-geral)
- [Pacotes Utilizados](#pacotes-utilizados)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Diagrama de Banco de Dados](#diagrama-de-banco-de-dados)
- [Documentação da API](#documentação-da-api)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Deploy](#deploy)

## Visão Geral

📌 Descrição Geral do Sistema

O sistema foi desenvolvido para gerenciar projetos, equipes e usuários do programa DevLab, centralizando informações e facilitando o acompanhamento das atividades acadêmicas. Seu propósito é fornecer uma camada de serviços segura, organizada e escalável, permitindo que diferentes perfis de usuários, como estudantes, professores e coordenadores interajam com os dados de forma eficiente.

O sistema resolve o problema da falta de controle unificado sobre as equipes e os participantes dos projetos, oferecendo uma visão estruturada das relações entre usuários, projetos e funções desempenhadas ao longo do programa.

🎯 Objetivos Principais

Oferecer uma plataforma backend robusta com autenticação e controle de acesso.

Gerenciar projetos, suas respectivas equipes e os usuários envolvidos.

Registrar a função de cada usuário dentro de cada equipe/projeto, incluindo liderança.

Permitir que um usuário participe de vários projetos e equipes simultaneamente.

Disponibilizar visões agregadas sobre a participação de um usuário no DevLab.

Facilitar a geração de relatórios sobre projetos, equipes e históricos de participação.

🧩 Domínio de Aplicação

O sistema se aplica ao contexto educacional do DevLab, um programa em que turmas de cursos técnicos e superiores desenvolvem projetos reais em parceria com setores internos e externos da instituição.

👥 Público-Alvo

Estudantes envolvidos em projetos.

Professores/orientadores que supervisionam equipes.

Coordenadores responsáveis pela gestão do DevLab.

Sistemas externos que desejem consumir os dados via API.

⚙️ Funcionalidades de Alto Nível

CRUD de projetos, equipes e usuários.

Associação de usuários a projetos e equipes.

Definição de líderes de equipe.

Consulta de histórico completo de participação de cada usuário.

Endpoints para relatórios e análises agregadas.

Autenticação segura para proteger os dados. 

## Pacotes Utilizados


| Pacote                  | Versão       | Descrição                                      |
|-------------------------|--------------|------------------------------------------------|
| Django                  | >=6.0        | Framework web principal                        |
| djangorestframework     | >=3.11.0     | Toolkit para construção de APIs REST           |
| asgiref                 | latest       | Biblioteca auxiliar do Django para suporte a ASGI (Async Server Gateway Interface).|
| sqlparse                | >=0.5.4      | Utilitário para análise e formatação de SQL, usado internamente pelo Django.ambiente.|
| tzdata                  | 2025.2       | Banco de dados de fusos horários (timezone data) necessário para ambientes sem suporte nativo.|


## Estrutura do Projeto

Apresente a organização dos diretórios e arquivos principais. Utilize uma árvore de diretórios para visualização clara.

```
projeto_api/
├── manage.py
├── requirements.txt
├── .env.example
├── projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   └── ...
├── docs/
│   └── database_diagram.png
└── scripts/
    └── deploy.sh
```

Descreva brevemente o propósito de cada diretório e módulo relevante.

## Diagrama de Banco de Dados

![Diagrama de Banco de Dados](./docs/database_diagram.png)

> **Descrição:** Inclua um diagrama ER (Entidade-Relacionamento) gerado por ferramentas como `django-extensions` ou `pygraphviz`. Descreva as principais entidades, relacionamentos e campos críticos.

## Documentação da API

A documentação interativa está disponível em `/api/docs/` (Swagger UI) ou `/api/redoc/` (ReDoc) no ambiente de desenvolvimento.

### Endpoints Principais

| Método | Endpoint              | Descrição                          | Autenticação |
|--------|-----------------------|------------------------------------|--------------|
| GET    | `/api/items/`         | Lista todos os itens               | Opcional     |
| POST   | `/api/items/`         | Cria um novo item                  | Requerida    |
| GET    | `/api/items/{id}/`    | Recupera um item específico        | Opcional     |
| ...    | ...                   | ...                                | ...          |

> **Detalhes:** Consulte a interface Swagger para schemas de request/response, parâmetros e exemplos.

## Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente local.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/usuario/DevLabBackEnd.git
   cd DevLabBackEnd
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   ```bash
   cp .env.example .env
   # Edite .env com suas credenciais
   ```

5. **Aplique as migrações e inicie o servidor:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 👥 Equipe

- Geovanne
-  Júlio 
- Márcia


