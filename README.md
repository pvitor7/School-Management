# School-Management
Sistema para o gerenciamento escolar.

<h1 align="center">
  Plataforma de Gerenciamento Escolar
</h1>


<p align = "center">
Projeto full stack para a plataforma School Management - uma plataforma de gerenciamento para as instituições de ensino. Cada campus (unidade escolar) criado pode receber o cadastro de usuários, com nível de permissão de administrador, professor e alunos. Dentro de cada campus, podem ser cadastrados diferentes cursos. E dentro de cada curso podem ser cadastradas diferentes turmas de ensino. Os usuários são vinculados às turmas, cursos e espaços de trabalho.
Este projeto faz a criação de um banco de dados, com todas as tabelas necessárias. E a criação de uma API para leitura, inclusão, atualização e deleção de dados no Banco.
</p>


<blockquote align="center"></blockquote>

<h3 align= "center">
  Tecnologias&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h3>

<p align="center" >
  As tecnologias utilizadas no projeto foram: Python | PostgreSQL | Django | Django Rest Framework | SQLite .
</p>
<br/>
<br/>

<h3 align= "center">
    Intatação e execução
<h3 align= "center">


##### 1. Clone este repositório em sua máquina local.

```
git clone git@github.com:pvitor7/PS-Python-React.git
```

##### 2. Acesse a pasta do projeto.

```
cd School-Management
```

##### 3. Crie um ambiente e o use para execução (Linux).

```
python -m venv venv
```
```
source venv/bin/activate
```

##### 4. Instale as dependências do projeto.

```
pip install -r requirements.txt
```

##### 5. Variáveis de Ambiente

Dentro do  o projeto  crie um arquivo **.env**, copiando o formato do arquivo **.env.example**  e preencha com as configurações do banco de dados:

```
cp .env.example .env
```

##### 6. Crie as tabelas no banco de dados.
Após o preenchimento das variáveis de ambiente, crie e execute as **migrations** com os seguintes comandos.

  
```
./manage.py makemigrations
```

```
./manage.py migrate
```

##### 7. Inicie o servidor.

```
./manage.py runserver
```

<br/>

OBS: Para testar os endpoints da API, você pode usar o [Postman](https://www.postman.com/) ou outra ferramenta similar.

<br/>

<h3 align= "center">

Endpoints
</h3>


### **User**

[ Voltar para os Endpoints ](#5-endpoints)

A criação do usuário é definida pelos campos abaixo

| Campo        | Tipo    | Descrição                                        |
| ------------ | ------- | ------------------------------------------------ |
| id           | string  | Identificador único do usuário.                  |
| username         | string  | O nome do usuário.                               |
| email        | string  | O e-mail do usuário.                             |
| cellphone     | string  | O número de contato do usuário.                  |
| password     | string  | A senha de login do usuário.                     |

### Endpoints

| Método | Rota              | Descrição                                                             |
| ------ | ----------------- | --------------------------------------------------------------------- |
| POST   | /login            | Gera o token de autenticação.                                         |
| POST   | /users/register   | Criação de um Usuário.                                                |
| GET    | /users/:id            | Lista todos os usuários.                                              |
| PATCH  | /users/:id            | Atualiza um Usuario usando seu ID como parâmetro                      |
| DELETE | /users/:id            | Deleta um Usuario usando seu ID como parâmetro                        |


### `POST /users`

Cria um novo usuário.

#### Parâmetros

- `username` (string, obrigatório): nome do usuário.
- `email` (string, obrigatório): e-mail do usuário.
- `cellphone` (string, obrigatório): telefone do usuário.
- `password` (string, obrigatório): senha do usuário.

#### Exemplo de requisição

```
POST `/users HTTP/1.1`
Host: http://localhost:8000
Content-Type: application/json
```

##### Corpo da Requisição:
```json

{
    "name": "João da Silva",
    "email": "joao.silva@exemplo.com",
    "password": "s3nh4s3gur4",
    "cellphone": "11900000000",
}
```

##### Exemplo de resposta

```
201 Created
```

```json
{
    "id": "123e4567-e89b-12d3-a456-426655440000",
    "name": "João da Silva",
    "email": "joao.silva@exemplo.com",
    "celphone": "11900000000",
    "created_at": "2023-02-14T18:25:43.511Z",
    "updated_at": "2023-02-14T18:25:43.511Z"
}
```


### `/login`

##### Exemplo de requisição

```
POST /login
Host: http://localhost:8000
Authorization: None
Content-type: application/json
```

##### Corpo da Requisição:

```json
{
    "email": "joao.silva@exemplo.com",
    "password": "s3nh4s3gur4",
}
```

##### Exemplo de Response:

```
200 Ok
```

```json
{
  "token": "a9ec5561c260f73c596128b7776d3e424b88d360"
}
```

#### `GET /users/:id`

Retorna informações sobre um usuário específico.


##### Exemplo de requisição

```
PATCH /users
Host: http://localhost:8000
Authorization: ea9ec5561c260f73c596128b7776d3e424b88d360
Content-type: application/json
```

##### Exemplo de Response:

```
200 OK
```
```json
{
    "id": "7b7eb384-6fce-4f10-ad25-9b26a9ce2d8a",
    "name": "João da Silva",
    "celphone": "11900000000",
	"is_active": true,
	"cart": {
		"is_finished": false,
		"products": []
	}
}
```

#### **Deletando Usuários Especifico**

#### `/users`

##### Exemplo de requisição

```
DELETE /users
Host: http://localhost:8000
Authorization: ea9ec5561c260f73c596128b7776d3e424b88d360
Content-type: application/json
```
Para Deletar um único os usuários você precisa estar logado.


##### Corpo da Requisição:

```json
Vazio
```

##### Exemplo de Response:

```
204 OK
```

```json
Vazio
```