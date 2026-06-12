# To-Do List API (Backend)
Esta é a API de backend para a aplicação **To-Do List**, desenvolvida com **Django** e **Django REST Framework (DRF)**. A API fornece endpoints para gerenciamento de usuários (registro, consulta e atualização de perfil), autenticação baseada em JSON Web Tokens (JWT) e gerenciamento completo de notas (tarefas).
---
## 🛠️ Tecnologias Utilizadas
- **Python** (versão 3.10 ou superior recomendada)
- **Django** (Framework web)
- **Django REST Framework (DRF)** (Construção de APIs REST)
- **django-cors-headers** (Configuração de CORS)
- **djangorestframework-simplejwt** (Autenticação baseada em JWT)
- **SQLite** (Banco de dados padrão para desenvolvimento)
- **Pytest / pytest-django** (Framework e ambiente de testes automatizados)
---
## 📋 Pré-requisitos
Antes de iniciar, certifique-se de ter instalado em sua máquina:
- Python 3.x
- Git (opcional, para versionamento)
- Um gerenciador de pacotes como `pip` (geralmente instalado junto ao Python)
---
## ⚙️ Instalação e Configuração
Siga os passos abaixo para preparar o ambiente de desenvolvimento:
### 1. Clonar o repositório
Se ainda não clonou o repositório, execute o comando:
```bash
git clone https://github.com/C14-INATEL/to-do-list-back.git
cd to-do-list-back
```
### 2. Configurar o Ambiente Virtual (venv)
Crie e ative um ambiente virtual isolado para instalar as dependências do projeto:
**No Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```
**No Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Instalar as Dependências
Com o ambiente virtual ativo, instale os pacotes necessários:
```bash
pip install -r requirements.txt
```
### 4. Executar as Migrações do Banco de Dados
A API utiliza SQLite por padrão. Navegue para a pasta `backend` e execute as migrações para criar as tabelas necessárias:
```bash
cd backend
python manage.py migrate
```
---
## 🚀 Executando o Servidor
Para iniciar o servidor de desenvolvimento local da API, execute o comando na pasta `backend`:
```bash
python manage.py runserver
```
Por padrão, a API estará acessível em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
---
## 🧪 Testes Automatizados
O projeto utiliza o **Pytest** para a execução de testes de integração, unitários e mocks. Para rodar a suíte de testes:
1. Certifique-se de estar na pasta `backend`.
2. Execute o comando:
```bash
pytest
```
---
## 🔑 Autenticação
A maioria dos endpoints desta API exige autenticação por JWT. Para acessar estes endpoints, você deve:
1. Obter o token de acesso fazendo uma requisição `POST` em `/api/login/`.
2. Incluir o token de acesso nos cabeçalhos (headers) de todas as requisições protegidas da seguinte forma:
   ```http
   Authorization: Bearer <seu_token_access>
   ```
---
## 🔗 Endpoints da API
Abaixo estão descritos todos os endpoints disponibilizados pela API.
### 1. Autenticação e Usuários
|
 Método 
|
 Endpoint 
|
 Descrição 
|
 Requer Autenticação 
|
|
:---
|
:---
|
:---
|
:---:
|
|
`POST`
|
`/api/register/`
|
 Cria uma nova conta de usuário. 
|
 Não 
|
|
`POST`
|
`/api/login/`
|
 Autentica um usuário e retorna tokens Access e Refresh. 
|
 Não 
|
|
`POST`
|
`/api/refresh/`
|
 Gera um novo token Access usando um token Refresh válido. 
|
 Não 
|
|
`GET`
|
`/api/me/`
|
 Retorna as informações do usuário logado. 
|
 Sim 
|
|
`PUT`
|
`/api/me/`
|
 Atualiza (parcial ou totalmente) os dados do usuário logado. 
|
 Sim 
|
---
### 2. Gerenciamento de Notas (Tarefas)
|
 Método 
|
 Endpoint 
|
 Descrição 
|
 Requer Autenticação 
|
|
:---
|
:---
|
:---
|
:---:
|
|
`GET`
|
`/api/notes/`
|
 Lista todas as notas criadas pelo usuário logado. 
|
 Sim 
|
|
`POST`
|
`/api/notes/`
|
 Cria uma nova nota (tarefa). 
|
 Sim 
|
|
`GET`
|
`/api/notes/<id>/`
|
 Retorna os detalhes de uma nota específica do usuário. 
|
 Sim 
|
|
`PUT`
|
`/api/notes/<id>/`
|
 Atualiza por completo uma nota específica. 
|
 Sim 
|
|
`PATCH`
|
`/api/notes/<id>/`
|
 Atualiza de forma parcial uma nota específica (ex: marcar como concluída). 
|
 Sim 
|
|
`DELETE`
|
`/api/notes/<id>/`
|
 Deleta uma nota específica. 
|
 Sim 
|
---
## 📥 Exemplos de Payload e Resposta
### Registro de Usuário (`POST /api/register/`)
- **Corpo da Requisição (JSON):**
  ```json
  {
    "username": "joao_silva",
    "password": "senhaSegura123",
    "email": "joao@example.com",
    "first_name": "João"
  }
  ```
- **Resposta Esperada (201 Created):**
  ```json
  {
    "id": 1,
    "username": "joao_silva",
    "email": "joao@example.com",
    "first_name": "João"
  }
  ```
### Login (`POST /api/login/`)
- **Corpo da Requisição (JSON):**
  ```json
  {
    "username": "joao_silva",
    "password": "senhaSegura123"
  }
  ```
- **Resposta Esperada (200 OK):**
  ```json
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
  ```
### Obter Perfil (`GET /api/me/`)
- **Headers:** `Authorization: Bearer <token_access>`
- **Resposta Esperada (200 OK):**
  ```json
  {
    "id": 1,
    "username": "joao_silva",
    "email": "joao@example.com",
    "first_name": "João"
  }
  ```
### Criar Nota (`POST /api/notes/`)
- **Headers:** `Authorization: Bearer <token_access>`
- **Corpo da Requisição (JSON):**
  ```json
  {
    "title": "Estudar Django REST Framework",
    "done": false
  }
  ```
- **Resposta Esperada (201 Created):**
  ```json
  {
    "id": 1,
    "title": "Estudar Django REST Framework",
    "done": false
  }
  ```
### Atualizar Nota Parcialmente (`PATCH /api/notes/<id>/`)
- **Headers:** `Authorization: Bearer <token_access>`
- **Corpo da Requisição (JSON):**
  ```json
  {
    "done": true
  }
  ```
- **Resposta Esperada (200 OK):**
  ```json
  {
    "id": 1,
    "title": "Estudar Django REST Framework",
    "done": true
  }
  ```

  **Readme feito com o seguinte pronpt**
  ```
  Atue como um desenvolvedor de software sênior e especialista em documentação técnica. 
Sua tarefa é criar um arquivo README.md completo, profissional e altamente escaneável para o meu projeto. O README completo deve satisfazer  : instalação, execução, uso e funcionalidades

Use formatação Markdown avançada, incluindo badges, blocos de código bem estruturados, tabelas e emojis funcionais como âncoras visuais. O tom deve ser profissional e claro, ideal para desenvolvedores e recrutadores.

O README deve conter obrigatoriamente as seguintes seções estruturadas:

1. SOBRE O PROJETO E FUNCIONALIDADES
- Uma introdução breve.
- Uma lista em tópicos curtos e diretos com as principais funcionalidades (features) do sistema.

2. INSTALAÇÃO
- Pré-requisitos necessários antes de começar (Ex: Node instalado, Docker, etc).
- Passo a passo numerado de como clonar o repositório e instalar as dependências.
- Exemplo de configuração de variáveis de ambiente (.env), se aplicável.

3. EXECUÇÃO
- Comando exato para rodar o projeto em modo de desenvolvimento.
- Comando para rodar em modo de produção (se houver).
- Comando para rodar os testes (se houver).

4. USO
- Uma explicação prática de como interagir com o projeto após executá-lo.
- Exemplos de endpoints principais (se for API) ou rotas/telas chaves (se for frontend).
- Inclua um exemplo rápido de código, requisição cURL ou payload JSON para ilustrar o uso.

Gere o código formatado dentro de um bloco de código Markdown para que eu possa copiar facilmente.
```