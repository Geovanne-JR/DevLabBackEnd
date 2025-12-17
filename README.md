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

## Estrutura do Projeto

```
DevLabBackEnd/
├── manage.py
├── requeriments.txt
├── db.sqlite3
├── README.md
├── centro/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   ├── migrations/
│   └── templates/
├── devlab_backend/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
```

- `centro/`: App principal com modelos, views, serializers, permissões e rotas da API.
- `devlab_backend/`: Configurações globais do projeto Django.
- `templates/`: Páginas HTML para visualização web.

## Equipe
- Geovanne
- Júlio
- Márcia
