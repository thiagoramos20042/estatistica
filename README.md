# Teste Básico de Estatística com Armazenamento em Banco de Dados

## Descrição

Esta aplicação interativa, desenvolvida com **Streamlit**, aplica testes básicos de estatística aos usuários e armazena os resultados em um banco de dados **SQLite** para futuras análises. O acesso aos resultados é protegido por senha, garantindo segurança e privacidade.

---

## Funcionalidades

### Registro e Teste
- **Registro do Usuário**: Nome e email são obrigatórios para iniciar o teste.
- **Perguntas**: O teste possui **10 perguntas** de múltipla escolha sobre conceitos fundamentais de estatística.
- **Armazenamento de Resultados**: As respostas, número de acertos e percentual de acertos são salvos no banco de dados.

### Consulta aos Resultados
- **Proteção por Senha**: Apenas usuários com a senha correta podem acessar os resultados armazenados.
- **Exibição Tabular**: Resultados são exibidos em formato tabular com suporte da biblioteca `pandas`.

---

## Estrutura do Projeto

### Banco de Dados

O banco de dados **SQLite** (`resultados.db`) contém uma tabela chamada `resultados` com os seguintes campos:

| Campo              | Tipo      | Descrição                                      |
|---------------------|-----------|-----------------------------------------------|
| `id`               | INTEGER   | Identificador único (chave primária).         |
| `nome`             | TEXT      | Nome do usuário.                              |
| `email`            | TEXT      | Email do usuário.                             |
| `respostas`        | TEXT      | Respostas fornecidas (armazenadas como string).|
| `acertos`          | INTEGER   | Número de respostas corretas.                 |
| `percentual_acerto`| REAL      | Percentual de acerto no teste.                |

### Principais Arquivos

- `main.py`: Arquivo principal da aplicação contendo a interface e as funcionalidades.
- `resultados.db`: Banco de dados SQLite para armazenar os resultados dos testes.

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **Streamlit**: Para a criação de interface interativa.
- **SQLite**: Para armazenamento de dados.
- **Pandas**: Para manipulação e exibição de dados em formato tabular.

---

## Pré-requisitos

Certifique-se de que as seguintes bibliotecas estão instaladas no seu ambiente:

```bash
pip install streamlit pandas
