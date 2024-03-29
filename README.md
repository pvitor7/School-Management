# School-Management
Sistema para o gerenciamento escolar.

<h1 align="center">
  Plataforma de Gerenciamento Escolar
</h1>


<p align = "center">
Projeto full stack School Management - uma plataforma de gerenciamento para as instituições de ensino. Cada campus (unidade escolar) criado pode receber o cadastro de usuários, com nível de permissão de administrador, professor, assistente de turma e estudante. Dentro de cada campus, podem ser cadastrados diferentes cursos. E dentro de cada curso podem ser cadastradas diferentes turmas. Os usuários são vinculados às turmas, cursos e espaços de trabalho.
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


<h4 align= "center">
  Relacionamentos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h4>


<img src='Relations.png'>
<br/>

<h3 align= "center">
    Intatação e execução
<h3 align= "center">


##### 1. Clone este repositório em sua máquina local.

```
git clone git@github.com:pvitor7/School-Management.git
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

##### 8. Testes.
A aplicação também conta com testes (em desenvolvimento), que podem ser executados com o seguinte comando:

```
./manage.py test 
```
<br/>

<h3 align= "center">

Sobre a aplicação
</h3>



O primeiro usuário criado será designado como proprietário (role 9), ele poderá criar um ou mais campus, cadastrar administradores (role 7, sem vínculo de classe), professores (role 5), assistentes de classe (role 3) e alunos  (role 1).
As dicliplinas (subjects) são associadas aos alunos e ao curso, elas criarão 4 campos de pontuação que podem ser utilizados para calcular a média final e definir critérios de aprovação.

Abaixo seguem exemplos de todas e suas respectivas permissões, que poderão ser acessadas na docuntação, desde que o projeto esteja em execução, no seguinte local: http://localhost:8000/schema/swagger-ui/

<br/>

<h3 align= "center">

Endpoints
</h3>



<br/>

**OBS:** Para testar os endpoints da API, você pode usar o [Postman](https://www.postman.com/) ou outra ferramenta similar.

**Para execução local:** http://localhost:8000 <br/> **Deploy:** https://school-manager-api-foe3.onrender.com
<br/>



#### **User**


Endpoints: http://localhost:8000/schema/swagger-ui/#/users/
| Método | Rota              | Descrição                                       | Permissão              |
| ------ | ----------------- | ------------------------------------------------|-----------------------------------------------------------|
| POST   | /users/register   | Criação de um Usuário.                          | Livre apenas para o primeiro usuário criado, que será o proprietário|
| POST   | /login            | Gera o token de autenticação.                   | Sem permissão (token) necessária |
| GET    | /users/:id        | Recupera um usuário pelo ID.                    | Assistentes, Professores, Administradores ou proprietários|
| GET    | /users/           | Lista todos os usuários.                        | Assistentes, Professores, Administradores ou proprietários|
| PATCH  | /users/:id        | Atualiza um Usuario usando seu ID como parâmetro | O próprio usuário (atualização de senha), administradores ou proprietários (outras propriedades)|
| DELETE | /users/:id        | Deleta um Usuario usando seu ID como parâmetro   | Administradores ou proprietários |


<br/>

#### **Roles**
Endpoints: http://localhost:8000/schema/swagger-ui/#/roles/
| Método | Rota              | Descrição                                       | Permissão                                                 |
| ------ | ----------------- | ------------------------------------------------|-----------------------------------------------------------|
| GET   | /campus/roles/    | Lista a tabela roles (permissões) e suas informações         | Administradores ou proprietários                          |

<br/>

#### **Campus**
Endpoints: http://localhost:8000/schema/swagger-ui/#/campus/
| Método | Rota              | Descrição                                       | Permissão                                                 |
| ------ | ----------------- | ------------------------------------------------|-----------------------------------------------------------|
| POST   | /campus/  | Criação de um Campus                            | Apenas o proprietário, que será o primeiro usuário criado, não precisará de token de Administrador e não precisará passar a propriedade 'role' (que corresponde ao nível de permissão, com role ID) na instituição. |
| GET    | /campus/          | Lista todos os campus                           | Todos os usuários vinculados                              |
| GET    | /campus/:id       | Recupera um Campus por ID                       | Todos os usuários vinculados                              |
| PATCH  | /campus/:id       | Atualiza um Campus usando seu ID como parâmetro | Administradores ou proprietários                          |
| DELETE | /campus/:id       | Deleta um Usuario usando seu ID como parâmetro  | Proprietários                                             |

<br/>

#### **Cursos**
Endpoints: http://localhost:8000/schema/swagger-ui/#/courses/
| Método | Rota              | Descrição                                       | Permissão                                                 |
| ------ | ----------------- | ------------------------------------------------|-----------------------------------------------------------|
| POST   | /campus/:id/cursos/register  | Criação de um curso                             | Administradores ou proprietários                          |
| GET    | /campus/:id/cursos/          | Lista todos os cursos                           | Todos os usuários vinculados                              |
| GET    | /campus/:id/cursos/:id       | Recupera um curso por ID                        | Todos os usuários vinculados                              |
| PATCH  | /campus/:id/cursos/:id       | Atualiza um curso usando seu ID como parâmetro  | Administradores ou proprietários                          |
| DELETE | /campus/:id/cursos/:id       | Deleta um curso usando seu ID como parâmetro  | Administradores ou proprietários                          |

<br/>

#### **Classes**
Endpoints: http://localhost:8000/schema/swagger-ui/#/classes/
| Método | Rota              | Descrição                                       | Permissão                                                 |
| ------ | ----------------- | ------------------------------------------------|-----------------------------------------------------------|
| POST   | /campus/cursos/:id/classes/register | Criação de uma classe                           | Administradores ou proprietários                          |
| GET    | /campus/cursos/:id/classes/         | Lista todas as classes                          | Todos os usuários vinculados                              |
| GET    | /campus/cursos/:id/classes/:id      | Recupera uma classe por ID                      | Todos os usuários vinculados                              |
| PATCH  | /campus/cursos/:id/classes/:id      | Atualiza uma classe usando seu ID como parâmetro| Administradores ou proprietários                          |
| DELETE | /campus/cursos/:id/classes/:id      | Deleta uma classe usando seu ID como parâmetro  | Administradores ou proprietários                          |

<br/>

#### **Subjects**
Endpoints: http://localhost:8000/schema/swagger-ui/#/subjects/
| Método | Rota              | Descrição                                       | Permissão                                                 |
| ------ | ----------------- | ------------------------------------------------|-----------------------------------------------------------|
| POST   | /campus/cursos/:id/subjects/ | Criação de uma disciplina                           | Administradores ou proprietários                          |
| GET    | campus/cursos/:id/subjects/         | Lista todas as disciplinas                          | Todos os usuários vinculados                              |
| GET    | campus/cursos/:id/subjects/:id      | Recupera uma disciplina por ID                      | Todos os usuários vinculados                              |
| PATCH  | campus/cursos/:id/subjects/:id      | Atualiza uma disciplina usando seu ID como parâmetro| Administradores ou proprietários                          |
| DELETE | campus/cursos/:id/subjects/:id      | Deleta uma disciplina usando seu ID como parâmetro  | Administradores ou proprietários                          |

