import streamlit as st

st.title('Hola Mundo')
st.header('Este es un encabezado')
st.subheader('Este es un subencabezado')

st.markdown("""
# &nbsp;
# &nbsp;
# &nbsp;
# &nbsp;
# Universidad de Colima
# Campus Coquimatlán
# Facultad de Ingeniería Mecánica y Eléctrica

## **Proyecto de Ejercicios de la 2da parcial en Streamlit**

#### **Materia:** Análisis de Series Temporales
#### **Maestro:** Mata López Walter Alexander

#### **Alumno:** Amaya González Héctor Eduardo

#### **Carrera:** Ingeniería en Computación Inteligente
#### **Semestre y Grupo:** 6°B

#### **Fecha de Entrega:** 26/04/2024
""")

st.markdown('### Esto es un texto en markdown')
st.markdown("### Esto es un texto en markdown")

st.markdown(""" - Esto es un texto en markdown, listado""")
st.text('Este es un texto')
st.write('Hola Mundo')

st.markdown(""" [Esto es un texto en markdown, link] (https://www.google.com)""")
st.markdown(" [Esto es un texto en markdown, link2] (https://www.ucol.mx/)")
