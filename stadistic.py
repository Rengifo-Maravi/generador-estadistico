import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la aplicación
st.title("Análisis Estadístico de Datos en formato CSV")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube un archivo CSV donde en la primera fila esten el nombre de las variables", type=["csv"])

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
    
    # Seleccionar una columna numérica para el análisis de outliers
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns
    columna_seleccionada = st.selectbox("Selecciona una columna numérica para analizar outliers", columnas_numericas)
    
    if columna_seleccionada:
        # Calcular los límites para detectar outliers
        Q1 = df[columna_seleccionada].quantile(0.25)
        Q3 = df[columna_seleccionada].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        
        # Identificar outliers
        outliers = df[(df[columna_seleccionada] < limite_inferior) | (df[columna_seleccionada] > limite_superior)]
        
        # Mostrar los límites y los outliers
        st.write(f"Límite inferior: {limite_inferior}")
        st.write(f"Límite superior: {limite_superior}")
        st.write("### Valores Atípicos (Outliers)")
        st.write(outliers)
        
        # Crear gráficos
        st.write("### Gráficos de Análisis de Outliers")
        
        # Gráfico de caja (boxplot)
        st.write("#### Diagrama de Caja (Boxplot)")
        fig, ax = plt.subplots()
        sns.boxplot(x=df[columna_seleccionada], ax=ax)
        ax.set_title(f"Boxplot de {columna_seleccionada}")
        st.pyplot(fig)
        
        # Gráfico de dispersión con límites
        st.write("#### Gráfico de Dispersión con Límites")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df.index, y=df[columna_seleccionada], ax=ax, color='blue', label='Datos')
        ax.axhline(limite_superior, color='red', linestyle='--', label='Límite Superior')
        ax.axhline(limite_inferior, color='green', linestyle='--', label='Límite Inferior')
        ax.scatter(outliers.index, outliers[columna_seleccionada], color='red', label='Outliers')
        ax.set_title(f"Scatter Plot de {columna_seleccionada} con Outliers")
        ax.legend()
        st.pyplot(fig)
        
else:
    st.write("sube un archivo CSV donde la primera en la primera columna este el nombre de todas las variables, por favor para comenzar el análisis.")
