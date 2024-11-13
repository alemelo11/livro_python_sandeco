import streamlit as st
import joblib

import streamlit as st
import joblib

# Carregar o modelo salvo
ia_faixa_etaria = joblib.load('modelo_knn_faixa_etaria.pkl')

# Título
st.title("Calculo de Faixa Etária")

# Receber entrada do usuário
idade_input = st.text_input("Idade")

# Verificar se o input não está vazio antes de converter
if idade_input:
    idade = int(idade_input)

    # Calcular a faixa etária quando o botão for clicado
    if st.button("Calcular"):
        faixa_predita = ia_faixa_etaria.predict([[idade]])
        st.write(f'Faixa etária prevista para idade {idade}: {faixa_predita[0]}')
else:
    st.write("Por favor, insira uma idade.")



