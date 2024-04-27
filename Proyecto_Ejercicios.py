import streamlit as st

st.title('Hola Mundo')
st.header('Este es un encabezado')
st.subheader('Este es un subencabezado')

st.markdown("""
<center>

# Universidad de Colima
### Campus Coquimatlán
### Facultad de Ingeniería Mecánica y Eléctrica

<br>

## **Proyecto de Ejercicios de la 2da parcial en Streamlit**

<br>
</center>

#### **Materia:** Análisis de Series Temporales
#### **Maestro:** Mata López Walter Alexander

<br>

#### **Alumno:** Amaya González Héctor Eduardo

#### **Carrera:** Ingeniería en Computación Inteligente
#### **Semestre y Grupo:** 6°B

<br>

#### **Fecha de Entrega:** 26/04/2024
""")
st.markdown('### Esto es un texto en markdown')
st.markdown("### Esto es un texto en markdown")

st.markdown(""" - Esto es un texto en markdown, listado""")
st.text('Este es un texto')
st.write('Hola Mundo')

st.markdown(""" [Esto es un texto en markdown, link] (https://www.google.com)""")
st.markdown(" [Esto es un texto en markdown, link2] (https://www.ucol.mx/)")
