import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Análisis Estadístico de Datos CSV")

# Generar datos de prueba
data = {
    "Nombre": ["Juan", "Maria", "Pedro", "Laura", "Carlos", "Ana", "Luis", "Sofia", "Jorge", "Diana"],
    "Edad": [28, 34, 45, 29, 30, 40, 35, 27, 50, 33],
    "Salario": [50000, 60000, 75000, 55000, 52000, 80000, 58000, 48000, 90000, 62000],
    "Genero": ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"],
    "Departamento": ["Ventas", "Marketing", "IT", "Ventas", "Marketing", "IT", "Ventas", "Marketing", "IT", "Ventas"]
}

df = pd.DataFrame(data)

# Mostrar el dataframe original
st.write("### DataFrame Original")
st.write(df)

# Generar estadísticas descriptivas (solo para columnas numéricas)
st.write("### Estadísticas Descriptivas")
st.write(df.describe(include='number'))  # Filtra solo columnas numéricas

# Mostrar información adicional
st.write("### Información Adicional")
st.write(f"Número de filas: {df.shape[0]}")
st.write(f"Número de columnas: {df.shape[1]}")
st.write("Tipos de datos:")
st.write(df.dtypes)

# Mostrar valores nulos por columna
st.write("### Valores Nulos por Columna")
st.write(df.isnull().sum())

# Filtrar solo columnas numéricas para la matriz de correlación
columnas_numericas = df.select_dtypes(include=['number']).columns
if len(columnas_numericas) >= 2:
    st.write("### Matriz de Correlación")
    st.write(df[columnas_numericas].corr())
else:
    st.write("⚠️ No hay suficientes columnas numéricas para calcular la correlación.")
