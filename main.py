import streamlit as st
import pandas as pd
import plotly_express as px

# Título de la aplicación
st.header('Cuadro de Mando de Inventario de Vehículos')

# Lectura de los datos
car_data = pd.read_csv('vehicles_us.csv') 

# Botón para el Histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # al hacer clic en el checkbox
    st.write('Creando un histograma para la columna odómetro')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para el Gráfico de Dispersión (Requisito común en TripleTen)
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Creando un gráfico de dispersión: Precio vs. Año del modelo')
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="model_year", y="price")
    # mostrar gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)