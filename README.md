# 📦 Sistema de Controle de Estoque - Eletrônicos Full

## 📖 Sobre o projeto

O Sistema de Controle de Estoque foi desenvolvido em Python com o objetivo de auxiliar no gerenciamento de produtos de uma loja de eletrônicos.

O sistema permite ao administrador controlar o estoque de forma simples através de um menu interativo no terminal, realizando operações de cadastro, consulta, atualização e exclusão de produtos.

As informações são armazenadas em um arquivo JSON, permitindo que os dados permaneçam salvos mesmo após o encerramento da aplicação.

---

## 🎯 Objetivo

Desenvolver um sistema em Python aplicando conceitos de:

* Lógica de programação
* Funções
* Manipulação de arquivos
* Estruturas de dados
* Tratamento de exceções
* Persistência de dados utilizando JSON

---

## 🛠️ Tecnologias utilizadas

* Python 3
* JSON
* Biblioteca padrão do Pythonfaça 

---

## 📂 Estrutura dos dados

Os produtos são armazenados em um arquivo JSON seguindo a estrutura abaixo:

```json
{
    "1": {
        "nome": "Mouse",
        "quantidade": 10,
        "preço": 79.90
    },
    "2": {
        "nome": "Teclado",
        "quantidade": 5,
        "preço": 149.90
    }
}
```

---

## ⚙️ Funcionalidades

O sistema oferece as seguintes funcionalidades:

* Login administrativo por senha
* Visualização dos produtos cadastrados
* Cadastro de novos produtos
* Atualização de quantidade e preço
* Exclusão de produtos
* Persistência dos dados em arquivo JSON
* Tratamento de erros durante leitura e gravação dos arquivos

---

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

2. Entre na pasta do projeto:

```bash
cd nome-do-projeto
```

3. Execute o arquivo principal:

```bash
python main.py
```

---

## 📋 Menu do sistema

Ao acessar o sistema, o administrador poderá escolher uma das opções:

```text
1 - Ver estoque
2 - Atualizar produto
3 - Adicionar produto
4 - Deletar produto
```

---

## 📁 Organização do projeto

```text
📦 projeto
│
├── main.py
├── estoque.json
└── README.md
```

---

## 💾 Persistência dos dados

Todos os produtos são armazenados em um arquivo JSON.

Sempre que um produto é adicionado, atualizado ou removido, as informações são automaticamente gravadas no arquivo, mantendo os dados salvos para futuras execuções.

---

## 👨‍💻 Autor

**Breno Camargo**

Projeto desenvolvido para a disciplina da faculdade como prática de desenvolvimento de software utilizando Python.
