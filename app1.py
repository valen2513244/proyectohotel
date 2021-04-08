import streamlit as st 
import pandas as pd
from PIL import Image
import altair as alt
st.title("Aplicacion")
st.sidebar.title("Menú")


 



#add_select = st.sidebar.selectbox(
	#"Admnistracion",
	#("Habitaciones","Gastos","Check_in","Empleado")
#)
menu = st.sidebar.radio(
    "🌐 Selecione una opcion",
    ('💻Habitaciones', '🦾 Gastos', ' 📱 Check_in' , 'Ingresar'))




if menu == "Ingresar":
	password = st.sidebar.text_input("Enter a password", type="password")

if menu == "💻Habitaciones":
	piso = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3]
	hab = ["hab1","hab2","hab3","hab4","hab5","hab6","hab7","hab8","hab9","hab10","hab11","hab12","hab13","hab14","hab15","hab16"]
	tipo = ["Matrimonial","Doble","Matrimonial","Matrimonial","Matrimonial","Doble","Doble","Doble","Triple","Doble","Doble","Matrimonial","Triple","Triple","Matrimonial","Matrimonial"]

	data = {"Piso column":piso,
		 "Habitaciones column":hab,
		 "Tipo column":tipo}
	df = pd.DataFrame(data)
	st.write(df)
