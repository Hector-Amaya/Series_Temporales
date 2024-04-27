import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.ensemble import IsolationForest
import statistics as sti

st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
        color: #000000;
    }
    .sidebar .sidebar-content {
        background: #212529;
        color: #ffffff;
    }
    .Widget>label {
        color: #ffffff;
    }
    .st-ck {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Hola Mundo')
st.header('Este es un encabezado')
st.subheader('Este es un subencabezado')

st.markdown("""
<center>

# Universidad de Colima
### Campus Coquimatlán
### Facultad de Ingeniería Mecánica y Eléctrica

<br>

## **Estadíticas descriptivas**

<br>
</center>

#### **Materia:** Análisis de Series Temporales
#### **Maestro:** Mata López Walter Alexander

<br>

#### **Alumno:** Amaya González Héctor Eduardo



#### **Carrera:** Ingeniería en Computación Inteligente
#### **Semestre y Grupo:** 6°B


<br>

#### **Fecha de Entrega:** 14/04/2024
""")

st.markdown('### Esto es un texto en markdown')
st.markdown("### Esto es un texto en markdown")

st.markdown(""" - Esto es un texto en markdown, listado""")
st.text('Este es un texto')
st.write('Hola Mundo')

st.markdown(""" [Esto es un texto en markdown, link] (https://www.google.com)""")
st.markdown(" [Esto es un texto en markdown, link2] (https://www.ucol.mx/)")



# Esto crea una barra lateral en la aplicación
st.sidebar.title('Opciones')

# Agrega elementos a la barra lateral
option = st.sidebar.selectbox(
    'Selecciona una opción',
    ('Inicio', 'Configuración', 'Ayuda')
)

opcion = st.sidebar.multiselect()

# Mostrar el contenido principal en función de la opción seleccionada
if option == 'Inicio':
    st.title('Página de inicio')
    st.write('¡Bienvenido a nuestra aplicación!')

elif option == 'Configuración':
    st.title('Configuración')
    st.write('¡Aquí puedes configurar tus preferencias!')

elif option == 'Ayuda':
    st.title('Ayuda')
    st.write('¡Aquí puedes encontrar ayuda y soporte!')
