# Skinroutine - Integração Back-end e Banco de Dados (Padrão DAO)

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos, aplicando a persistência de dados em MySQL utilizando Python e o **Padrão DAO (Data Access Object)**.

## 👥 Equipe e Tecnologias
* **Linguagem:** Python
* **Banco de Dados:** MySQL (Driver: `mysql-connector-python`)
* **Arquitetura:** Orientação a Objetos com separação de camadas (Model, DAO, Database)

---

## ⚙️ Pré-requisitos para Execução

Antes de rodar o sistema, certifique-se de que possui instalado em sua máquina:
1. **Python** (versão 3.x com o PATH configurado).
2. **Servidor MySQL** ativo (com o banco da Entrega 4 criado).

---

## 🚀 Passo a Passo para Baixar e Rodar

### 1. Clonar o repositório
Abra o terminal na pasta de sua preferência e clone o projeto (ou baixe o arquivo ZIP diretamente pelo GitHub):
`git clone <URL_DO_SEU_REPOSITORIO>`
`cd <NOME_DA_PASTA>`

### 2. Instalar a dependência do MySQL
No terminal, execute o comando para instalar o conector oficial do MySQL para Python:
`python -m pip install mysql-connector-python`

### 3. Configurar a Conexão com o Banco
Abra o arquivo **database.py** e ajuste as credenciais de acordo com o seu ambiente MySQL local (usuário, senha e nome do banco de dados).

### 4. Executar a Aplicação
Com tudo configurado, rode o sistema principal pelo terminal:
`python main.py`

---

## 📋 Funcionalidades do CRUD Demonstradas
* **C (Create):** Cadastro de novos usuários informando nome, e-mail, senha e tipo de pele.
* **R (Read):** Listagem geral de todos os registros e busca específica por ID.
* **U (Update):** Atualização de dados cadastrais de forma consistente.
* **D (Delete):** Exclusão lógica ou definitiva de registros no banco.
