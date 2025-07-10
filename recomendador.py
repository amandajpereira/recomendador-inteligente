import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Carrega os dados do CSV
df = pd.read_csv('alimentos.csv')

# 2. Junta o nome com a descrição para gerar os vetores
df['text'] = df['nome'] + ' ' + df['descricao']

# 3. Vetoriza os textos
vectorizer = TfidfVectorizer()
vetores = vectorizer.fit_transform(df['text'])

# 4. Função de recomendação filtrada por categoria
def recomendar(alimento, top_n=3):
    if alimento not in df['nome'].values:
        return 'Alimento não encontrado.'
    
    idx = df.index[df['nome'] == alimento][0]
    categoria = df.loc[idx, 'categoria']
    
    # Filtra só os alimentos da mesma categoria
    df_filtrado = df[df['categoria'] == categoria]
    
    # Vetoriza novamente só os textos filtrados
    vetores_filtrados = vectorizer.transform(df_filtrado['text'])
    
    # Índice do alimento filtrado
    idx_filtrado = df_filtrado.index.get_loc(idx)
    
    sim = cosine_similarity(vetores_filtrados[idx_filtrado], vetores_filtrados).flatten()
    sim[idx_filtrado] = 0  # ignora ele mesmo
    top_indices = sim.argsort()[::-1][:top_n]
    
    return df_filtrado.iloc[top_indices][['nome', 'categoria']]

# 5. Teste
entrada = input("Digite um alimento: ").lower()
resultado = recomendar(entrada)

print("\nRecomendações:")
print(resultado)
