# API de Usuários e Perfis (FastAPI + ORM SQLAlchemy)

Este projeto foi desenvolvido como parte da atividade prática da disciplina de Desenvolvimento de API Backend. O objetivo central é demonstrar o uso do ORM **SQLAlchemy** para gerenciar um banco de dados relacional SQLite, focando em mapeamento de entidades e relacionamentos.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.13
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Banco de Dados:** SQLite (arquivo local `banco.db`)

## 📌 Requisitos Implementados (Checklist)
- [x] **CRUD Completo:** Rotas para Criar, Listar e Deletar usuários.
- [x] **Relacionamento 1:1:** Cada Usuário possui um Perfil vinculado via chave estrangeira.
- [x] **Criação Simultânea:** O sistema permite criar o perfil no mesmo momento do cadastro do usuário.
- [x] **Integridade de Dados:** Validação para impedir o cadastro de e-mails duplicados.
- [x] **Mapeamento de Relacionamento:** A listagem de usuários (GET) retorna automaticamente os dados do perfil associado através do ORM.

## Como Executar e Testar o Projeto

Siga os passos abaixo no seu terminal para rodar a aplicação localmente:

### 1. Clonar o Repositório
git clone [https://github.com/SEU_USUARIO/api-fastapi-orm.git](https://github.com/SEU_USUARIO/api-fastapi-orm.git)
cd api-fastapi-orm

### 2. Configurar o Ambiente Virtual
python3 -m venv venv
source venv/bin/activate  - No Mac/Linux
      # venv\Scripts\activate - No Windows

### 3. Instalar as Dependências
pip install fastapi uvicorn sqlalchemy

### 4. Iniciar o Servidor
python3 -m uvicorn main:app --reload --port 8080

### 5. Testar via Documentação Interativa (Swagger)
Com o servidor rodando, acesse o link abaixo para realizar os testes de POST, GET e DELETE diretamente pelo navegador:
👉 http://127.0.0.1:8080/docs

Desenvolvido por: Marcel Filho
