import streamlit as st 
import pandas as pd
from PIL import Image
import altair as alt
from datetime import time
import folium 
from streamlit_folium import folium_static
import json 
from geopy.geocoders import Nominatim 
import os


st.sidebar.title("Home")

menu = st.sidebar.radio(
    "🌐 Selecione una opcion",
    ('Ingresar', '$ Gastos', 'Check_in' , '💻Habitaciones'))

if menu == "Ingresar":
	user = st.text_input("Ingrese un Usuario",)
	password = st.text_input("Ingrese una Contraseña", type="password")
	button = st.button("Ingresar")
	if user == "valentin" and password == "1234":
		st.write("Contraseña correcta")
	else:
		st.write("Contraseña incorrecta")

if menu == "💻Habitaciones":
	piso = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3]
	hab = ["hab1","hab2","hab3","hab4","hab5","hab6","hab7","hab8","hab9","hab10","hab11","hab12","hab13","hab14","hab15","hab16"]
	tipo = ["Matrimonial","Doble","Matrimonial","Matrimonial","Matrimonial","Doble","Doble","Doble","Triple","Doble","Doble","Matrimonial","Triple","Triple","Matrimonial","Matrimonial"]

	data = {"Piso ":piso,
		 "Habitaciones ":hab,
		 "Tipo ":tipo}
	df = pd.DataFrame(data)
	st.write(df)
 	
if menu == "Check_in":
	st.title("Check_in")
	st.text_input("Nombre y Apellido")
	st.text_input("RUC o Cedula de Identidad")
	st.text_input("Ciudad")
	st.text_input("Numero de Pasajeros")
	st.text_input("Email")
	st.text_input("Telefono")
	st.date_input("Entrada el")
	st.date_input("Salida el")
	st.title("Metodo de Pago")
	st.radio("",
		("Efectivo","Tarjeta de Credito","Tarjeta de Debito","Paypal"))
	st.button("Enviar Formulario")


tipo = st.selectbox("Tipo de mapa",("OpenStreetMap", "Stamen Terrain","Stamen Toner","Stamen Watercolor","CartoDB dark_matter"
))

mapa = folium.Map(tiles=tipo, location=[-1.39699 , -78.42289], zoom_start=3)

folium.Marker(location=[-1.39699 , -78.42289]
,icon=folium.Icon(color="red")).add_to(mapa)

folium.LayerControl().add_to(mapa)

folium_static(mapa)

