import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot
from sklearn.ensemble import IsolationForest
import statistics as sti


st.title('Hola Mundo')
st.header('Este es un encabezado')
st.subheader('Este es un subencabezado')


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

opcion = st.slider('Seleccione un valor')

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
