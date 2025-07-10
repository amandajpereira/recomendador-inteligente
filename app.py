import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregar dados
df = pd.read_csv('alimentos.csv')

# Preparar TF-IDF - removi stop_words pois pode cortar palavras em português
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['descricao'])  # Note o 'descricao' sem acento

st.title('🍏 Recomendador Inteligente de Alimentos')

alimento_input = st.text_input('Digite um alimento:')

def recomendar(alimento):
    # Verifica se o alimento existe
    if alimento not in df['nome'].values:
        return f"'{alimento}' não encontrado. Tente: {', '.join(df['nome'].sample(3).values)}"
    
    idx = df[df['nome'] == alimento].index[0]
    categoria = df.loc[idx, 'categoria']
    
    # Pega os índices dos alimentos da mesma categoria
    indices_categoria = df[df['categoria'] == categoria].index
    
    # Calcula similaridade apenas com os da mesma categoria
    similaridades = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix[indices_categoria]
    ).flatten()
    
    # Ordena e pega os mais similares (excluindo ele mesmo)
    similares_idx = similaridades.argsort()[-4:-1][::-1]
    recomendados = df.loc[indices_categoria[similares_idx], 'nome'].tolist()
    
    return recomendados

if alimento_input:
    resultado = recomendar(alimento_input.strip())  # strip() remove espaços extras
    if isinstance(resultado, str):
        st.error(resultado)  # Mensagem de erro em vermelho
    else:
        st.success("Recomendações:")  # Mensagem de sucesso em verde
        for item in resultado:
            st.write(f"🍴 {item}")