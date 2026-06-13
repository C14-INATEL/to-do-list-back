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

### 1. Autenticação e Usuários

| Método | Endpoint | Descrição | Requer Autenticação |
| :--- | :--- | :--- | :---: |
| `POST` | `/api/register/` | Cria uma nova conta de usuário. | Não |
| `POST` | `/api/login/` | Autentica um usuário e retorna tokens Access e Refresh. | Não |
| `POST` | `/api/refresh/` | Gera um novo token Access usando um token Refresh válido. | Não |
| `GET` | `/api/me/` | Retorna as informações do usuário logado. | Sim |
| `PUT` | `/api/me/` | Atualiza (parcial ou totalmente) os dados do usuário logado. | Sim |

### 2. Gerenciamento de Notas (Tarefas)

| Método | Endpoint | Descrição | Requer Autenticação |
| :--- | :--- | :--- | :---: |
| `GET` | `/api/notes/` | Lista todas as notas criadas pelo usuário logado. | Sim |
| `POST` | `/api/notes/` | Cria uma nova nota (tarefa). | Sim |
| `GET` | `/api/notes/<id>/` | Retorna os detalhes de uma nota específica do usuário. | Sim |
| `PUT` | `/api/notes/<id>/` | Atualiza por completo uma nota específica. | Sim |
| `PATCH` | `/api/notes/<id>/` | Atualiza de forma parcial uma nota específica (ex: marcar como concluída). | Sim |
| `DELETE` | `/api/notes/<id>/` | Deleta uma nota específica. | Sim |

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

---

# 📋 Documentação de Processo (Requisitos NP2)

> [!NOTE]
> Esta seção apresenta os processos e a maturidade de engenharia de software adotados pelo grupo para a entrega da NP2.

## 3.1 — Histórias de Usuário (User Stories)

Abaixo estão descritas as principais Histórias de Usuário que guiaram o desenvolvimento do backend de To-Do List.

### US01 - Registro de Usuário (Cadastro)
* **Como** visitante da aplicação
* **Eu quero** criar uma conta informando nome de usuário, e-mail e senha
* **Para que** eu possa ter meu próprio espaço seguro para salvar minhas tarefas
* **Prioridade:** Alta
* **Status final:** Entregue
* **Critérios de Aceitação:**
  * **Given (Dado)** que sou um visitante não cadastrado e envio dados válidos (username, email, password) para o endpoint `/api/register/`
  * **When (Quando)** a requisição for processada
  * **Then (Então)** o sistema deve retornar status `201 Created`, salvar o usuário no banco de dados e retornar os dados cadastrados (omitindo a senha por segurança).
* **Rastreabilidade:** [PR #1](https://github.com/C14-INATEL/to-do-list-back/pull/1) ➔ [test_integration.py::test_user_registration](file:///C:/Users/felip/Documents/C14/to-do-list-back/backend/tests/users/test_integration.py#L15-L25)

---

### US02 - Autenticação de Usuário (Login JWT)
* **Como** usuário já cadastrado
* **Eu quero** fazer login informando minhas credenciais (usuário e senha)
* **Para que** eu possa obter um token JWT válido para acessar meus dados protegidos
* **Prioridade:** Alta
* **Status final:** Entregue
* **Critérios de Aceitação:**
  * **Given (Dado)** que sou um usuário cadastrado e envio as credenciais corretas para o endpoint `/api/login/`
  * **When (Quando)** a requisição de login for efetuada
  * **Then (Então)** o sistema deve retornar status `200 OK` contendo os tokens `access` e `refresh` no corpo da resposta.
* **Rastreabilidade:** [PR #1](https://github.com/C14-INATEL/to-do-list-back/pull/1) ➔ [test_integration.py::test_login_success](file:///C:/Users/felip/Documents/C14/to-do-list-back/backend/tests/users/test_integration.py#L36-L47)

---

### US03 - Consulta e Atualização do Perfil de Usuário
* **Como** usuário autenticado no sistema
* **Eu quero** visualizar e poder alterar as informações do meu perfil (nome de usuário, e-mail e primeiro nome)
* **Para que** eu possa manter meus dados cadastrais sempre atualizados
* **Prioridade:** Média
* **Status final:** Entregue
* **Critérios de Aceitação:**
  * **Given (Dado)** que estou autenticado e envio uma requisição PUT para `/api/me/` com novos dados válidos
  * **When (Quando)** a atualização for processada
  * **Then (Então)** o sistema deve salvar as modificações no banco de dados, retornar status `200 OK` e as informações de perfil atualizadas.
* **Rastreabilidade:** [PR #1](https://github.com/C14-INATEL/to-do-list-back/pull/1) ➔ [test_integration.py::test_update_user_detail](file:///C:/Users/felip/Documents/C14/to-do-list-back/backend/tests/users/test_integration.py#L76-L88)

---

### US04 - Criação de Notas (Tarefas)
* **Como** usuário autenticado
* **Eu quero** criar uma nova nota informando um título
* **Para que** eu possa registrar minhas obrigações diárias na minha lista de tarefas
* **Prioridade:** Alta
* **Status final:** Entregue
* **Critérios de Aceitação:**
  * **Given (Dado)** que estou devidamente autenticado na API e envio uma requisição POST para `/api/notes/` com um título válido (ex: "Estudar para a prova de NP2")
  * **When (Quando)** a nota for criada
  * **Then (Então)** o sistema deve retornar status `201 Created`, associar a nota criada ao meu usuário e retornar o ID, título e o status `done` padrão como `false`.
* **Rastreabilidade:** [PR #2](https://github.com/C14-INATEL/to-do-list-back/pull/2) ➔ [users/views.py::NoteListCreateView](file:///C:/Users/felip/Documents/C14/to-do-list-back/backend/users/views.py#L43-L60)

---

### US05 - Listagem, Atualização e Exclusão de Notas
* **Como** usuário autenticado
* **Eu quero** listar apenas as minhas notas criadas, poder alterá-las (marcar como concluída) ou excluí-las
* **Para que** eu possa gerenciar o ciclo de vida das minhas tarefas sem visualizar as notas de outros usuários
* **Prioridade:** Alta
* **Status final:** Entregue
* **Critérios de Aceitação:**
  * **Given (Dado)** que possuo notas cadastradas e faço uma requisição PATCH para `/api/notes/<id>/` com o payload `{"done": true}`
  * **When (Quando)** a requisição for processada
  * **Then (Então)** o sistema deve marcar aquela tarefa específica como concluída no banco de dados, mantendo-a segura dos outros usuários.
* **Rastreabilidade:** [PR #2](https://github.com/C14-INATEL/to-do-list-back/pull/2) ➔ [users/views.py::NoteDetailView](file:///C:/Users/felip/Documents/C14/to-do-list-back/backend/users/views.py#L62-L93)

---

## 3.2 — Metodologia de Desenvolvimento

* **Metodologia Adotada:** **Scrum Híbrido com Kanban**. Adotamos o Kanban para a visualização clara do fluxo de desenvolvimento (To Do, In Progress, In Review, Done) integrado ao GitHub Projects, enquanto mantivemos a estrutura do Scrum para divisão de Sprints.
* **Papéis no Grupo:**
  * **Product Owner (PO):** Felipe Santos de Souza (definição e priorização do Backlog e User Stories).
  * **Facilitador (Scrum Master):** [Nome de outro Integrante] (remoção de impedimentos e organização de reuniões).
  * **Desenvolvedores:** Todos os membros atuaram ativamente na codificação da API Django REST, configuração do banco de dados SQLite e infraestrutura.
  * **QA/Testes:** [Nome de outro Integrante] e equipe (foco na cobertura de testes com Pytest e implementação da esteira de testes na pipeline).
* **Cadência e Reuniões:** Ciclos (Sprints) com duração de 15 dias. Realizamos reuniões rápidas semanais (de cerca de 15 minutos) via Discord/WhatsApp para alinhar o que foi feito, o que seria feito a seguir e possíveis impedimentos.
* **DoD (Definition of Done):** Uma tarefa foi considerada concluída quando o código passou por revisão de Pull Request (pelo menos 1 aprovação), todos os testes rodaram localmente com sucesso, o código estava alinhado ao padrão PEP 8 e a pipeline de integração contínua (CI) no GitLab executou sem erros.
* **Métricas Utilizadas:** 
  * Quantidade de issues entregues por sprint.
  * Cobertura de testes unitários e de integração (alvo mínimo de 80%).
  * Número de conflitos de merge encontrados (para avaliar a saúde das branches).

---

## 3.3 — Dinâmica de Desenvolvimento

* **Divisão de Tarefas:** As tarefas foram divididas nas reuniões de planejamento de sprint baseando-se na afinidade técnica e na carga de trabalho de cada membro. Dividimos o trabalho entre autenticação/usuários, gerenciamento de notas (tarefas) e infraestrutura de testes/pipelines.
* **Fluxo de Branches e Commits:** Adotamos um fluxo simplificado baseado no GitFlow. As modificações eram feitas em branches do tipo `feature/nome-da-funcionalidade` ou `fix/nome-da-correcao` criadas a partir da branch `main`. Mensagens de commit seguiram o padrão descritivo (ex: `feat: adiciona JWT autenticacao` ou `fix: corrige validacao de campos vazios`).
* **Processo de Code Review:** Nenhum código foi mesclado diretamente na branch `main`. Todo o desenvolvimento passou pela abertura de Pull Requests no GitHub, que exigiram a avaliação e aprovação de pelo menos um outro membro do grupo antes do merge final.
* **Desafios e Resolução de Conflitos:** O maior bloqueio enfrentado foi o conflito de merge simultâneo no arquivo de rotas (`urls.py`) e nas dependências do projeto (`requirements.txt`). O grupo resolveu alinhando-se previamente nos canais de comunicação sobre quem alteraria configurações globais, além de adotar a prática de fazer `git rebase` frequente em relação à `main`.
* **Lições Aprendidas:**
  * Alinhamento estrito sobre versões de dependências no início poupa muitas horas de debugging de ambiente.
  * O desenvolvimento de testes automatizados desde o primeiro dia facilita a refatoração do código com segurança.
  * O uso do GitLab CI/CD foi essencial para detectar rapidamente falhas de integração sem a necessidade de testes manuais frequentes.

---

## 4 — Uso de Inteligência Artificial

O uso de ferramentas de IA no desenvolvimento deste projeto foi transparente e seguiu as seguintes diretrizes:

* **Modelos Utilizados:** [Claude 3.5 Sonnet, Gemini]
* **Finalidades de Uso:** Geração da estrutura de documentação (README), geração de esqueleto de código, refatoração de funções, automação de testes unitários com pytest, auxílio em debugging de ambiente.
* **Exemplos de Prompts:**
  1. *Prompt:*
     ```text
     Atue como um desenvolvedor de software sênior e especialista em documentação técnica. 
     Sua tarefa é criar um arquivo README.md completo, profissional e altamente escaneável para o meu projeto. O README completo deve satisfazer: instalação, execução, uso e funcionalidades...
     ```
     *Resultado:* **Aceito**. Serviu de esqueleto base para a documentação inicial do projeto (README.md).

* **Dinâmica de Uso:** [Como a IA foi integrada no dia a dia. Ex: Utilizada individualmente pelos desenvolvedores, em pair programming ou para acelerar a escrita de códigos manuais com o github copilot autocomplete, acelera o desenvolvimento e nos traz resultados mais rápidos]

* **Resultado Pipeline**
[![image.png](https://i.postimg.cc/YScgbQdM/image.png)](https://postimg.cc/PC4PqvGR)
[![image.png](https://i.postimg.cc/dQSh5810/image.png)](https://postimg.cc/rzxymR56)
