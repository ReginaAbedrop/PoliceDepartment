import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px 
import plotly.graph_objects as go


st.title('Police Department')

st.write('This webpage shows the information of the incidents in San Francisco in the years 2018, 2019 and 2020.')
#Carga del dataset
df = pd.read_csv("Police.csv")
df = df[['Report Type Description','Filed Online','Incident Category','Incident Subcategory','Incident Description','Resolution','Police District','Analysis Neighborhood','Latitude','Longitude','Incident Day of Week','Incident Year']]


#District filter
district=df['Police District'].unique() # Todos los distritos
district=st.sidebar.selectbox("Choose a Police District: ", district)
df=df[df['Police District']==district]

#Neighborhood filter
neighborhood=df['Analysis Neighborhood'].unique()
neighborhood=st.sidebar.selectbox("Choose a Neighborhood: ", neighborhood)
df=df[df['Analysis Neighborhood']==neighborhood]


st.title('Incidents by Police Department')

st.write('Police District :', district)
st.write('Neighborhood  :', neighborhood)

#DataSet
st.write('This is the complete Police Report of 2018,2019 and 2020 of the Neighborhood selected.')
st.dataframe(df)


#Gráfica 1 
st.subheader('Number of Police reports by year')
agree2 = st.checkbox('Click here to visualize the reports by year')
if agree2:
    freq = df.groupby('Incident Year')[['Analysis Neighborhood']].count()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=freq.index, y=freq['Analysis Neighborhood']))
    fig.update_layout(title="Number of reports by year",
        xaxis_title="Year",
        yaxis_title="Total",
        legend_title="Variables",
        font=dict(
        size=12))
    st.plotly_chart(fig, use_container_width=True)


#Tabs
tab1,tab2,tab3,tab4=  st.tabs(['All years', '2018','2019','2020'])

with tab1:
    #Mapa Incidentes
    st.subheader('Incidents Map')
    mapa = df[['Latitude','Longitude']]
    mapa=mapa.rename(columns={"Latitude": "lat", "Longitude": "lon"})
    mapa = mapa.dropna()
    st.map(mapa)
     
    st.subheader('Incidents per year')
    fig3 = px.histogram(df, x='Incident Category', color='Incident Year')
    st.plotly_chart(fig3 , use_container_width=True)

with tab2:
    #Mapa Incidentes
    t2=df[df['Incident Year']==2018]
    st.subheader('Incidents Map in 2018')
    mapa = t2[['Latitude','Longitude']]
    mapa=mapa.rename(columns={"Latitude": "lat", "Longitude": "lon"})
    mapa = mapa.dropna()
    st.map(mapa)
    
    st.subheader('Incidents in 2018')
    fig3 = px.histogram(t2, x='Incident Category', color_discrete_sequence=['red'])
    st.plotly_chart(fig3 , use_container_width=True)
    
    
with tab3:
    #Mapa Incidentes
    t3=df[df['Incident Year']==2019]
    st.subheader('Incidents Map in 2019')
    mapa = t3[['Latitude','Longitude']]
    mapa=mapa.rename(columns={"Latitude": "lat", "Longitude": "lon"})
    mapa = mapa.dropna()
    st.map(mapa)
    
    st.subheader('Incidents in 2019')
    fig3 = px.histogram(t3, x='Incident Category', color_discrete_sequence=['green'])
    st.plotly_chart(fig3 , use_container_width=True)
    
   
with tab4:
    #Mapa Incidentes
    t4=df[df['Incident Year']==2020]
    st.subheader('Incidents Map in 2020')
    mapa = t4[['Latitude','Longitude']]
    mapa=mapa.rename(columns={"Latitude": "lat", "Longitude": "lon"})
    mapa = mapa.dropna()
    st.map(mapa)
    
    st.subheader('Incidents in 2020')
    fig3 = px.histogram(t4, x='Incident Category', color_discrete_sequence=['blue'])
    st.plotly_chart(fig3 , use_container_width=True)

    


