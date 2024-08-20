import streamlit as st
import sqlite3
import pandas as pd

# Função para criar a tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('resultados.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            respostas TEXT,
            acertos INTEGER,
            percentual_acerto REAL
        )
    ''')
    conn.commit()
    conn.close()

# Função para armazenar os resultados no banco de dados
def armazenar_resultado(nome, email_usuario, respostas, acertos):
    percentual_acerto = (acertos / len(respostas)) * 100
    respostas_str = "; ".join(respostas)
    
    conn = sqlite3.connect('resultados.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO resultados (nome, email, respostas, acertos, percentual_acerto)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, email_usuario, respostas_str, acertos, percentual_acerto))
    conn.commit()
    conn.close()

# Função para ler dados do banco de dados
def ler_resultados():
    conn = sqlite3.connect('resultados.db')
    cursor = conn.cursor()
    
    # Executa uma consulta para selecionar todos os dados da tabela
    cursor.execute("SELECT * FROM resultados")
    
    # Recupera todos os registros
    resultados = cursor.fetchall()
    
    # Fecha a conexão com o banco de dados
    conn.close()
    
    return resultados

# Cria a tabela se ainda não existir
criar_tabela()

# Título da aplicação
st.title("Teste Básico de Estatística")

# Registro do usuário
st.header("Registro do Usuário")
nome = st.text_input("Nome")
email_usuario = st.text_input("Email")

# Somente mostrar as perguntas se o usuário tiver registrado
if nome and email_usuario:
    st.header("Teste de Estatística")
    
    perguntas = {
        "1. O que é uma média aritmética e como ela é calculada?": [
            "A) A soma dos quadrados das diferenças dos valores em relação à média.",
            "B) O valor que aparece com mais frequência em um conjunto de dados.",
            "C) A soma de todos os valores dividida pelo número de observações.",
            "D) O valor central de um conjunto de dados ordenados."
            
        ],
            "2. Explique a diferença entre moda e mediana.": [
            "A) A moda é o valor mais frequente, enquanto a mediana é a soma de todos os valores dividida pelo número de observações.",
            "B) A moda é a média dos valores, enquanto a mediana é o valor central do conjunto de dados.",
            "C) A moda é o valor mais frequente, enquanto a mediana é o valor central em um conjunto de dados ordenados.",
            "D) A moda e a mediana sempre coincidem em um conjunto de dados."
        ],
        
        "3. O que é uma distribuição normal e quais são suas características principais?": [
            "A) Uma distribuição com múltiplos picos e uma forma assimétrica.",
            "B) Uma distribuição simétrica em torno da média, com caudas que se estendem ao infinito.",
            "C) Uma distribuição onde a mediana é sempre maior que a média.",
            "D) Uma distribuição que nunca apresenta dados abaixo da média."
        ],
        
        "4. Como é definido o desvio padrão e o que ele representa em um conjunto de dados?": [
            "A) A raiz quadrada da média dos valores do conjunto de dados.",
            "B) A medida que indica a dispersão dos valores em relação à moda.",
            "C) A raiz quadrada da variância, indicando a dispersão dos valores em relação à média.",
            "D) A soma dos valores absolutos das diferenças em relação à mediana."
        ],
        
        "5. Qual a diferença entre uma amostra e uma população em um estudo estatístico?": [
            "A) Amostra é o conjunto completo de dados, enquanto população é um subconjunto dos dados.",
            "B) População é o conjunto completo de elementos, enquanto amostra é um subconjunto representativo da população.",
            "C) População é sempre maior que a amostra em qualquer estudo.",
            "D) Amostra é a média da população."
        ],
        
        "6. O que é a variância e como ela está relacionada ao desvio padrão?": [
            "A) A variância é a raiz quadrada do desvio padrão.",
            "B) A variância é a média dos valores em um conjunto de dados.",
            "C) A variância é a média dos quadrados das diferenças dos valores em relação à média, e o desvio padrão é a raiz quadrada da variância.",
            "D) A variância sempre é menor que o desvio padrão."
        ],
        
        "7. Explique o conceito de correlação e como ele pode ser interpretado.": [
            "A) A correlação mede a força e a direção da relação linear entre duas variáveis.",
            "B) A correlação mede a diferença absoluta entre duas variáveis.",
            "C) A correlação sempre é positiva, indicando uma relação linear.",
            "D) A correlação é o quadrado da média dos valores em um conjunto de dados."
        ],
        
        "8. O que é um intervalo de confiança e como ele é utilizado?": [
            "A) Um intervalo de confiança é a média dos valores em um conjunto de dados.",
            "B) Um intervalo de confiança é uma faixa de valores que contém o verdadeiro parâmetro da população com uma certa probabilidade.",
            "C) Um intervalo de confiança é sempre igual ao desvio padrão.",
            "D) Um intervalo de confiança indica a moda de um conjunto de dados."
        ],
        
        "9. Qual a diferença entre um teste de hipótese unilateral e bilateral?": [
            "A) Um teste unilateral testa se um parâmetro é maior ou menor que um valor específico, enquanto um teste bilateral testa se o parâmetro é diferente de um valor específico.",
            "B) Um teste unilateral sempre rejeita a hipótese nula.",
            "C) Um teste bilateral testa apenas se o parâmetro é maior que um valor específico.",
            "D) Um teste bilateral nunca rejeita a hipótese nula."
        ],
        
        "10. O que significa um p-valor em um teste de hipóteses e como ele é utilizado para tomar decisões?": [
            "A) O p-valor é a probabilidade de que a hipótese alternativa seja verdadeira.",
            "B) O p-valor é a probabilidade de obter um resultado mais extremo, dado que a hipótese nula é verdadeira.",
            "C) O p-valor é sempre menor que o nível de significância.",
            "D) O p-valor indica a moda do conjunto de dados."
        ]
    }

    # Respostas corretas
    respostas_corretas = [
        "C) A soma de todos os valores dividida pelo número de observações.",
        "C) A moda é o valor mais frequente, enquanto a mediana é o valor central em um conjunto de dados ordenados.",
        "B) Uma distribuição simétrica em torno da média, com caudas que se estendem ao infinito.",
        "C) A raiz quadrada da variância, indicando a dispersão dos valores em relação à média.",
        "B) População é o conjunto completo de elementos, enquanto amostra é um subconjunto representativo da população.",
        "C) A variância é a média dos quadrados das diferenças dos valores em relação à média, e o desvio padrão é a raiz quadrada da variância.",
        "A) A correlação mede a força e a direção da relação linear entre duas variáveis.",
        "B) Um intervalo de confiança é uma faixa de valores que contém o verdadeiro parâmetro da população com uma certa probabilidade.",
        "A) Um teste unilateral testa se um parâmetro é maior ou menor que um valor específico, enquanto um teste bilateral testa se o parâmetro é diferente de um valor específico.",
        "B) O p-valor é a probabilidade de obter um resultado mais extremo, dado que a hipótese nula é verdadeira."
    ]

    respostas = []

    for pergunta, alternativas in perguntas.items():
        st.write(pergunta)
        resposta = st.radio(label="", options=alternativas, key=pergunta)
        respostas.append(resposta)

    if st.button("Finalizar Teste"):
        # Contar acertos
        acertos = sum([1 for i, resposta in enumerate(respostas) if resposta == respostas_corretas[i]])
        
        # Armazenar o resultado no banco de dados
        armazenar_resultado(nome, email_usuario, respostas, acertos)
        
        # Agradecimento ao usuário
        st.write("Obrigado por participar do teste! Suas respostas foram armazenadas com sucesso.")
        

# Ver Resultados Armazenados com Proteção por Senha
st.header("Acesso aos Resultados Armazenados")

senha_correta = "58342131"  # Defina a senha aqui

senha = st.text_input("Digite a senha para acessar os resultados:", type="password")

if st.button("Ver Resultados Armazenados"):
    if senha == senha_correta:
        resultados = ler_resultados()

        if resultados:
            st.header("Resultados Armazenados")
            # Converter para um DataFrame do pandas para melhor visualização
            colunas = ['ID', 'Nome', 'Email', 'Respostas', 'Acertos', 'Percentual de Acerto']
            df = pd.DataFrame(resultados, columns=colunas)
            st.dataframe(df)
        else:
            st.write("Nenhum resultado armazenado até o momento.")
    else:
        st.error("Senha incorreta. Acesso negado.")
