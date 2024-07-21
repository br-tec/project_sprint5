
# car_data = pd.read_csv(Path("../Data/vehicles.csv")) # lendo os dados

import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

car_data = pd.read_csv(Path("./Data/vehicles.csv"))  # lendo os dados

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:  # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


# criar outra caixa de seleção
build_dispersao = st.checkbox('Criar um gráfico de dispersão')

if build_dispersao:  # se a caixa de seleção for selecionada
    st.write('Criando um gráfico de dispersãoo para a coluna odometer')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
