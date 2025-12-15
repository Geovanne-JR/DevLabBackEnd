# Documentação da API

## Autenticação JWT

- **Obter token JWT**
  - Método: `POST`
  - URL: `/api/token/`
  - Parâmetros (JSON):
    - `username`: string (obrigatório)
    - `password`: string (obrigatório)
  - Exemplo de request:
    ```bash
    curl -X POST http://localhost:8000/api/token/ \
      -H "Content-Type: application/json" \
      -d '{"username": "seu_usuario", "password": "sua_senha"}'
    ```
  - Exemplo de response:
    ```json
    {"refresh": "<refresh_token>", "access": "<access_token>"}
    ```

- **Renovar token de acesso**
  - Método: `POST`
  - URL: `/api/token/refresh/`
  - Parâmetros (JSON):
    - `refresh`: string (obrigatório)
  - Exemplo de request:
    ```bash
    curl -X POST http://localhost:8000/api/token/refresh/ \
      -H "Content-Type: application/json" \
      -d '{"refresh": "<refresh_token>"}'
    ```
  - Exemplo de response:
    ```json
    {"access": "<novo_access_token>"}
    ```

---

## Usuários

### Listar usuários
- Método: `GET`
- URL: `/api/usuarios/`
- Header: `Authorization: Bearer <access_token>`
- Exemplo de response:
    ```json
    [
      {"id": 1, "username": "admin", "email": "admin@email.com", "cargo": "Coordenador"},
      ...
    ]
    ```

### Criar usuário
- Método: `POST`
- URL: `/api/usuarios/`
- Header: `Authorization: Bearer <access_token>` (admin)
- Parâmetros (JSON):
  - `username`: string
  - `email`: string
  - `password`: string
  - `cargo`: string (opcional)
- Exemplo de request:
    ```bash
    curl -X POST http://localhost:8000/api/usuarios/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <access_token>" \
      -d '{"username": "novo", "email": "novo@email.com", "password": "senha123"}'
    ```
- Exemplo de response:
    ```json
    {"id": 2, "username": "novo", "email": "novo@email.com", "cargo": null}
    ```

### Detalhar usuário
- Método: `GET`
- URL: `/api/usuarios/{id}/`
- Header: `Authorization: Bearer <access_token>`
- Exemplo de response:
    ```json
    {"id": 2, "username": "novo", "email": "novo@email.com", "cargo": null}
    ```

### Atualizar usuário
- Método: `PUT` ou `PATCH`
- URL: `/api/usuarios/{id}/`
- Header: `Authorization: Bearer <access_token>` (admin)
- Parâmetros (JSON):
  - Campos do usuário a serem atualizados
- Exemplo de request:
    ```bash
    curl -X PUT http://localhost:8000/api/usuarios/2/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <access_token>" \
      -d '{"username": "usuario_atualizado"}'
    ```
- Exemplo de response:
    ```json
    {"id": 2, "username": "usuario_atualizado", "email": "novo@email.com", "cargo": null}
    ```

### Deletar usuário
- Método: `DELETE`
- URL: `/api/usuarios/{id}/`
- Header: `Authorization: Bearer <access_token>` (admin)
- Exemplo de request:
    ```bash
    curl -X DELETE http://localhost:8000/api/usuarios/2/ \
      -H "Authorization: Bearer <access_token>"
    ```
- Exemplo de response:
    ```json
    // Resposta vazia (204 No Content)
    ```

### Projetos de um usuário
- Método: `GET`
- URL: `/api/usuarios/{id}/projetos/`
- Header: `Authorization: Bearer <access_token>`
- Exemplo de response:
    ```json
    [
      {"id": 1, "titulo": "Projeto X", "cliente": "Cliente Y", ...},
      ...
    ]
    ```

---

## Projetos

### Listar projetos
- Método: `GET`
- URL: `/api/projetos/`
- Header: `Authorization: Bearer <access_token>`
- Exemplo de response:
    ```json
    [
      {"id": 1, "titulo": "Projeto X", "cliente": "Cliente Y", ...},
      ...
    ]
    ```

### Criar projeto
- Método: `POST`
- URL: `/api/projetos/`
- Header: `Authorization: Bearer <access_token>` (admin/professor)
- Parâmetros (JSON):
  - `titulo`, `cliente`, `descricao`, `data_Inicio`, `data_Fim_Prevista`, `status`, etc.
- Exemplo de request:
    ```bash
    curl -X POST http://localhost:8000/api/projetos/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <access_token>" \
      -d '{"titulo": "Novo Projeto", "cliente": "Cliente Z", "descricao": "Descrição do projeto", "data_Inicio": "2023-10-01", "data_Fim_Prevista": "2023-10-31", "status": "em_andamento"}'
    ```
- Exemplo de response:
    ```json
    {"id": 2, "titulo": "Novo Projeto", "cliente": "Cliente Z", "status": "em_andamento"}
    ```

### Detalhar projeto
- Método: `GET`
- URL: `/api/projetos/{id}/`
- Header: `Authorization: Bearer <access_token>`
- Exemplo de response:
    ```json
    {
      "id": 2,
      "titulo": "Novo Projeto",
      "cliente": "Cliente Z",
      "descricao": "Descrição do projeto",
      "data_Inicio": "2023-10-01",
      "data_Fim_Prevista": "2023-10-31",
      "status": "em_andamento"
    }
    ```

### Atualizar projeto
- Método: `PUT` ou `PATCH`
- URL: `/api/projetos/{id}/`
- Header: `Authorization: Bearer <access_token>` (admin/professor)
- Parâmetros (JSON):
  - Campos do projeto a serem atualizados
- Exemplo de request:
    ```bash
    curl -X PATCH http://localhost:8000/api/projetos/2/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <access_token>" \
      -d '{"status": "concluido"}'
    ```
- Exemplo de response:
    ```json
    {"id": 2, "titulo": "Novo Projeto", "cliente": "Cliente Z", "status": "concluido"}
    ```

### Deletar projeto
- Método: `DELETE`
- URL: `/api/projetos/{id}/`
- Header: `Authorization: Bearer <access_token>` (admin/professor)
- Exemplo de request:
    ```bash
    curl -X DELETE http://localhost:8000/api/projetos/2/ \
      -H "Authorization: Bearer <access_token>"
    ```
- Exemplo de response:
    ```json
    // Resposta vazia (204 No Content)
    ```

### Adicionar participante ao projeto
- Método: `POST`
- URL: `/api/projetos/{id}/participantes/`
- Header: `Authorization: Bearer <access_token>` (admin/professor)
- Parâmetros (JSON):
  - `usuario_id`: int
- Exemplo de request:
    ```bash
    curl -X POST http://localhost:8000/api/projetos/1/participantes/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <access_token>" \
      -d '{"usuario_id": 2}'
    ```
- Exemplo de response:
    ```json
    {"status": "Usuário novo adicionado!"}
    ```

### Dashboard do projeto
- Método: `GET`
- URL: `/api/projetos/{id}/dashboard/`
- Header: `Authorization: Bearer <access_token>`
- Exemplo de response:
    ```json
    {
      "projeto": "Projeto X",
      "status": "em_andamento",
      "cliente": "Cliente Y",
      "equipes": [
        {
          "nome_equipe": "Equipe A",
          "lider": "usuario1",
          "total_membros": 3,
          "membros": ["usuario1", "usuario2", "usuario3"]
        }
      ]
    }
    ```

---

## Equipes

### Listar equipes
- Método: `GET`
- URL: `/api/equipes/`
- Header: `Authorization: Bearer <access_token>`
- Exemplo de response:
    ```json
    [
      {"id": 1, "nome": "Equipe A", "projeto": 1, ...},
      ...
    ]
    ```

### Criar equipe
- Método: `POST`
- URL: `/api/equipes/`
- Header: `Authorization: Bearer <access_token>` (admin)
- Parâmetros (JSON):
  - `nome`, `descricao`, `projeto`, `lider`, `membros`
- Exemplo de request:
    ```bash
    curl -X POST http://localhost:8000/api/equipes/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <access_token>" \
      -d '{"nome": "Nova Equipe", "descricao": "Descrição da equipe", "projeto": 1, "lider": 2, "membros": [2, 3]}'
    ```
- Exemplo de response:
    ```json
    {"id": 2, "nome": "Nova Equipe", "projeto": 1}
    ```

### Detalhar equipe
- Método: `GET`
- URL: `/api/equipes/{id}/`
- Header: `Authorization: Bearer <access_token>`
- Exemplo de response:
    ```json
    {"id": 2, "nome": "Nova Equipe", "descricao": "Descrição da equipe", "projeto": 1, "lider": 2, "membros": [2, 3]}
    ```

### Atualizar equipe
- Método: `PUT` ou `PATCH`
- URL: `/api/equipes/{id}/`
- Header: `Authorization: Bearer <access_token>` (admin)
- Parâmetros (JSON):
  - Campos da equipe a serem atualizados
- Exemplo de request:
    ```bash
    curl -X PATCH http://localhost:8000/api/equipes/2/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <access_token>" \
      -d '{"nome": "Equipe Atualizada"}'
    ```
- Exemplo de response:
    ```json
    {"id": 2, "nome": "Equipe Atualizada", "projeto": 1}
    ```

### Deletar equipe
- Método: `DELETE`
- URL: `/api/equipes/{id}/`
- Header: `Authorization: Bearer <access_token>` (admin)
- Exemplo de request:
    ```bash
    curl -X DELETE http://localhost:8000/api/equipes/2/ \
      -H "Authorization: Bearer <access_token>"
    ```
- Exemplo de response:
    ```json
    // Resposta vazia (204 No Content)
    ```

### Definir líder da equipe
- Método: `POST`
- URL: `/api/equipes/{id}/definir_lider/`
- Header: `Authorization: Bearer <access_token>` (admin)
- Parâmetros (JSON):
  - `usuario_id`: int
- Exemplo de request:
    ```bash
    curl -X POST http://localhost:8000/api/equipes/1/definir_lider/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <access_token>" \
      -d '{"usuario_id": 2}'
    ```
- Exemplo de response:
    ```json
    {"status": "Líder definido: novo"}
    ```

---

## Exemplos de request/response

> Para exemplos detalhados de requisições e respostas, consulte o Swagger em `/swagger/` ou veja exemplos nos blocos acima.

---

## Observações
- Todos os endpoints requerem autenticação JWT (exceto obtenção/refresh de token).
- Permissões: apenas admin/professor podem criar, editar ou deletar projetos/equipes; apenas admin pode criar/deletar usuários.
- Para detalhes de campos, consulte o Swagger ou o código fonte dos serializers.
