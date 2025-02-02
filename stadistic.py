import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Análisis Estadístico de Datos CSV")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Leer el archivo CSV
    df = pd.read_csv(uploaded_file)
    
    # Mostrar el dataframe original
    st.write("### DataFrame Original")
    st.write(df)
    
    # Generar estadísticas descriptivas
    st.write("### Estadísticas Descriptivas")
    st.write(df.describe())
    
    # Mostrar información adicional
    st.write("### Información Adicional")
    st.write(f"Número de filas: {df.shape[0]}")
    st.write(f"Número de columnas: {df.shape[1]}")
    st.write("Tipos de datos:")
    st.write(df.dtypes)
    
    # Mostrar valores nulos por columna
    st.write("### Valores Nulos por Columna")
    st.write(df.isnull().sum())
    
    # Mostrar correlación entre variables numéricas
    st.write("### Matriz de Correlación")
    st.write(df.corr())
    
else:
    st.write("Por favor, sube un archivo CSV para comenzar el análisis.")
