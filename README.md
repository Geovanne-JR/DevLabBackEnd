# DevLabBackEnd

## Descrição do Sistema

O DevLabBackEnd é uma aplicação desenvolvida em Django para o gerenciamento integrado de projetos, equipes e usuários do programa DevLab. O sistema centraliza todas as informações relevantes, simplificando o acompanhamento das atividades acadêmicas e promovendo a interação eficiente entre diferentes perfis de usuários, como estudantes, professores e coordenadores. Entre as principais funcionalidades, destacam-se o cadastro e gerenciamento de projetos, equipes e usuários, a associação de participantes, a definição de líderes e a consulta ao histórico de participação no programa.

## Como instalar dependências

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd DevLabBackEnd
   ```
2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requeriments.txt
   ```

## Como configurar o banco

O sistema já está configurado para usar SQLite por padrão. Para criar as tabelas do banco, execute:

```bash
python manage.py migrate
```

## Como criar usuário admin

Crie um superusuário para acessar o admin do Django:

```bash
python manage.py createsuperuser
```

Siga as instruções para definir usuário, e-mail e senha.

## Como rodar o servidor e testar a API

1. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```
2. **Acesse o admin:**
   - Navegue até `http://localhost:8000/admin/` e faça login com o superusuário criado.

3. **Testar a API:**
   - Os endpoints principais estão em `http://localhost:8000/api/`:
     - `/api/usuarios/` — Usuários (JWT obrigatório)
     - `/api/projetos/` — Projetos
     - `/api/equipes/` — Equipes
   - Para autenticar, obtenha um token JWT:
     ```bash
     curl -X POST http://localhost:8000/api/token/ \
       -H "Content-Type: application/json" \
       -d '{"username": "seu_usuario", "password": "sua_senha"}'
     ```
     O retorno será:
     ```json
     {"refresh": "...", "access": "..."}
     ```
     Use o token de acesso para autenticar nas requisições (sempre via Bearer):
     ```bash
     curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/usuarios/
     ```
   - Para renovar o token de acesso:
     ```bash
     curl -X POST http://localhost:8000/api/token/refresh/ \
       -H "Content-Type: application/json" \
       -d '{"refresh": "<refresh_token>"}'
     ```

4. **Observação importante sobre autenticação:**
   - A autenticação padrão da API é JWT, usando o header Authorization: Bearer.
   - Não é necessário login por sessão/cookies para uso da API.

## Documentação Interativa e Referência da API

- Acesse a documentação interativa da API pelo Swagger UI em: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Ou utilize a interface ReDoc em: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
- Para detalhes de endpoints, exemplos de requisições e respostas, consulte também a documentação em [`docs/API.md`](./centro/docs/API.md)

## Observações
- O sistema utiliza autenticação JWT para a API.
- Para criar usuários via API, é necessário estar autenticado como admin.

## EDR
<img width="480" height="473" alt="ERD" src="https://github.com/user-attachments/assets/0c5af28e-5624-41c8-a86d-eb8f41c0f363" />

## 📚 Rotas Principais do Sistema

### 🌐 Rotas Base da API

| Método | Endpoint | Descrição | Permissão |
|------|--------|----------|-----------|
| GET | /api/ | API Root do Django REST Framework (lista de endpoints disponíveis) | Público |
| GET | /api/projetos/ | Lista todos os projetos (filtrada conforme o perfil do usuário) | Público / Autenticado |
| GET | /api/equipes/ | Lista todas as equipes cadastradas | Público / Autenticado |
| GET | /api/usuarios/ | Lista todos os usuários do sistema | Autenticado |

---

### 🏠 Rota de Página Inicial (HTML)

| Método | Endpoint | Descrição |
|------|--------|----------|
| GET | /api/home/ | Página inicial do sistema com visualização dos projetos |

### 👥 Rotas de Equipes

| Método | Endpoint | Descrição |
|------|--------|----------|
| GET | /api/equipes/ | Lista todas as equipes |
| POST | /api/equipes/ | Criação de equipe (Admin) |
| GET | /api/equipes/{id}/ | Detalhes de uma equipe |
| POST | /api/equipes/{id}/definir_lider/ | Define o líder da equipe |

---

### 📁 Rotas de Projetos

| Método | Endpoint | Descrição |
|------|--------|----------|
| GET | /api/projetos/ | Lista projetos disponíveis |
| GET | /api/projetos/{id}/ | Detalhes de um projeto |
| GET | /api/projetos/{id}/dashboard/ | Dashboard do projeto |
| POST | /api/projetos/{id}/participantes/ | Adiciona participantes ao projeto |

## Estrutura do Projeto

- **centro/**: App principal contendo regras de negócio, APIs, permissões e templates.
- **devlab_backend/**: Configurações centrais do projeto Django.
- **templates/**: Sobrescrita de templates do Django Admin e Django REST Framework.

DevLabBackEnd/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── README.md
├── .gitignore
├── venv/
├── centro/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
│   ├── tests.py
│   ├── migrations/
│   │   └── __init__.py
│   └── templates/
│       └── centro/
│           ├── base.html
│           ├── home.html
│           ├── projeto_detalhe.html
│           └── adicionar_membro.html
├── devlab_backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── templates/
│       ├── admin/
|       ├── rest_framework/      
```

- `centro/`: App principal com modelos, views, serializers, permissões e rotas da API.
- `devlab_backend/`: Configurações globais do projeto Django.
- `templates/`: Páginas HTML para visualização web.

## Equipe
- Geovanne
- Júlio
- Márcia
