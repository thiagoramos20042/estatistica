# Estatística | Quiz e consulta de resultados

Teste interativo de conceitos estatísticos com cadastro, pontuação e consulta de resultados armazenados.

**Formação e fundamentos** · Aplicação Streamlit

[← Data Science, IA e Automações · Thiago Oliveira](https://github.com/thiagoramos20042/thiagoramos20042) · [Catálogo de projetos](https://github.com/thiagoramos20042/thiagoramos20042/blob/main/PROJETOS.md)

## Objetivo

Aplicar um questionário e organizar as respostas em uma base local para acompanhamento.

## O que você encontra

- Cadastro do participante por nome e e-mail.
- Correção do questionário e cálculo do percentual de acertos.
- Armazenamento em SQLite e tela de consulta aos resultados.

## Tecnologias

Python · Streamlit · pandas · SQLite

## Arquivos principais

| Arquivo | Conteúdo |
| --- | --- |
| [estatistica.py](estatistica.py) | Interface, questionário e persistência dos resultados. |

## Como explorar

Na raiz do repositório, em um ambiente Python separado:

```bash
python -m pip install streamlit pandas
python -m streamlit run estatistica.py
```

## Contexto do projeto

O arquivo de entrada é estatistica.py. O banco resultados.db é criado pelo script. A consulta utiliza a verificação de senha implementada no protótipo.

---

Integra o [portfólio de Thiago Oliveira](https://github.com/thiagoramos20042).
