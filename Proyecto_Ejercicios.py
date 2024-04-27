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

st.markdown("<center> ### Proyecto parcial", unsafe_allow_html=True)
st.markdown("<center><h2 class='centered'>Facultad de Ingeniería Mecánica y Eléctrica</h2>", unsafe_allow_html=True)
st.markdown("<h3 class='centered'>Ingeniería en Computación Inteligente</h3>", unsafe_allow_html=True)


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
# option = st.sidebar.selectbox(
#     'Selecciona una opción',
#     ('Inicio', 'Configuración', 'Ayuda')
# )

option = st.sidebar.radio(
    'Selecciona una opción', 
    ('Inicio', 'Configuración', 'Ayuda')
)


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
