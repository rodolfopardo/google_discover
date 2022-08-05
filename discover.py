#Librerias para aplicar 


import streamlit as st #streamlit
import pandas as pd #pandas
import numpy as np #numpy
import altair as alt


#Definir secuencia de busqueda de datos  

discover = pd.read_csv("datadiscover.csv")

columnas = ["dia", "ligamx", "seleccion"]

discover.columns = columnas

agosto = discover.iloc[92:125]
julio = discover.iloc[61:91]
junio = discover.iloc[31:60]
mayo = discover.iloc[0:30]

suma_liga_mx_ag = agosto["ligamx"].sum()
suma_seleccion_ag = agosto["seleccion"].sum()

suma_liga_mx_jl = julio["ligamx"].sum()
suma_seleccion_jl = julio["seleccion"].sum()

suma_liga_mx_jn = junio["ligamx"].sum()
suma_seleccion_jn = junio["seleccion"].sum()

suma_liga_mx_my = mayo["ligamx"].sum()
suma_seleccion_my = mayo["seleccion"].sum()


#Comenzar a mostrar secuencias 

st.write("## Google Discover  Ultimos dias 🤳")
st.write("### Notas de impacto por día - Google Discover API")


#Breve implicancia 
st.write("Se analiza una base con la siguiente cantidad de días en Discover: ", discover.shape[0])
st.write("Se analiza una base con la siguiente cantidad de columnas: ", discover.shape[1])

#Muestro DataFrame 

st.dataframe(discover, width=800, height=400)

st.write("### Notas De Discover - Impacto diario en LIGA MX")

#chart_data = pd.DataFrame(
     #discover["Notas Liga MX"], discover["Notas Seccion"],
     #columns=['LigaMX', 'Seccion'])

#fig = sns.lineplot(data = discover, x = "dia" , y = "ligamx")
#fig = plt.figure(figsize=(10, 4))
#sns.lineplot(x = "dia", y = "ligamx", data = discover)
#st.pyplot(fig)


#st.metric(label="Cantidad de notas en Julio", value=int(suma_liga_mx_jl), delta= int(suma_liga_mx_jn))

col1, col2, col3, col4 = st.columns(4)
col1.metric("Notas en Mayo", int(suma_liga_mx_my))
col2.metric("Notas en Junio", int(suma_liga_mx_jn))
col3.metric("Notas en Julio", int(suma_liga_mx_jl))
col4.metric("Notas en Agosto", int(suma_liga_mx_ag))

chart = alt.Chart(discover).mark_line().encode(
  x=alt.X("dia"),
  y=alt.Y("ligamx"),
  color = alt.value("green")).properties(title="Notas por día - Liga MX", width=800, height=400)
st.altair_chart(chart, use_container_width=False)

bars = alt.Chart(discover[92:125]).mark_bar().encode(
    x="dia",
    y="ligamx"
).properties(title="Notas por dia en Agosto - Liga MX", width=800, height=400)


text = bars.mark_text(
    align='center',
    #baseline='',
    #dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='ligamx:Q'
)

chart1 = bars +text
st.altair_chart(chart1, use_container_width=False)

st.write("### Notas De Discover - Impacto diario en Seleccion")


col1, col2, col3, col4 = st.columns(4)
col1.metric("Notas en Mayo", int(suma_seleccion_my))
col2.metric("Notas en Junio", int(suma_seleccion_jn))
col3.metric("Notas en Julio", int(suma_seleccion_jl))
col4.metric("Notas en Agosto", int(suma_seleccion_ag))


chart = alt.Chart(discover).mark_line().encode(
  x=alt.X('dia'),
  y=alt.Y('seleccion'),
  color = alt.value("blue")).properties(title="Notas por día - Selección", width=800, height=400)
st.altair_chart(chart, use_container_width=False)

bars = alt.Chart(discover[92:125]).mark_bar().encode(
    x="dia",
    y="seleccion"
).properties(title="Notas por dia en Agosto - Seleccion", width=800, height=400)


text = bars.mark_text(
    align='center',
    #baseline='',
    #dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='seleccion:Q'
)

chart1 = bars +text
st.altair_chart(chart1, use_container_width=False)





## Correlación de variables 

st.write("## Investigacion correlación de variables - Agosto")

corr = discover[92:125].corr()
st.write(corr)

st.write("""
0: asociación nula.

0.1: asociación pequeña.

0.3: asociación mediana.

0.5: asociación moderada.

0.7: asociación alta.

0.9: asociación muy alta.

  """)


chart = alt.Chart(discover).mark_point().encode(
  x=alt.X('ligamx'),
  y=alt.Y('seleccion'),
  opacity=alt.value(0.6),
  color=alt.value('red')).properties(title="Correlacion de variables", width=800, height=500)
st.altair_chart(chart, use_container_width=False)










