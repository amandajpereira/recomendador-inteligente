# 🧠 Recomendador Inteligente de Alimentos

Projeto simples de sistema de recomendação feito em Python.

Você digita o nome de um alimento (que pode ou não estar presente na base de dados), e o sistema retorna **alimentos semelhantes da mesma categoria** (como frutas, carnes, laticínios, etc).

---

## 🛠 Tecnologias usadas

- Python  
- Pandas  
- Scikit-learn (TF-IDF e Similaridade Cosseno)
- Streamlit	Interface web 

---

## 📦 Como rodar o projeto
### 🌐 **Online** (recomendado):  
Acesse diretamente pelo link:  
👉 [https://recomendador-inteligente.streamlit.app/](https://recomendador-inteligente-rfmtf3abodymyungq8tf54.streamlit.app/)

### 💻 Localmente:
git clone 

cd recomendador-inteligente

pip install -r requirements.txt

streamlit run app.py

## 💡 Como funciona
O sistema usa TF-IDF para transformar as descrições em vetores numéricos

Compara os vetores usando similaridade cosseno

Filtra os resultados para retornar apenas alimentos da mesma categoria do alimento consultado

## 📁 Estrutura dos arquivos
alimentos.csv: Base de dados contendo alimentos, categorias e descrições

recomendador.py: Script principal que faz a recomendação

README.md: Este arquivo


