import streamlit as st 
import pandas as pd
import altair as alt
from datetime import time
import openpyxl
import plotly.express as px

url1 = "https://drive.google.com/file/d/1Z-3jLryDVe3mjbzxQnqdZjxUnnnRi_wm/view?usp=sharing"
url2 = "https://drive.google.com/file/d/1YvOOnzVD6BstJolyMzMDEMQLKznPSnea/view?usp=sharing"
url3 = "https://drive.google.com/file/d/1iSH7msuIsO2XEHxFBizG9dCCGk7Ime6K/view?usp=sharing"
url4 = "https://drive.google.com/file/d/1wJ7M38FoK1kHHpM0Qy3h7TbJ3-arq0vl/view?usp=sharing"
file_id1=url1.split('/')[-2]
file_id2=url2.split('/')[-2]
file_id3=url3.split('/')[-2]
file_id4=url4.split('/')[-2]

dwn_url1='https://drive.google.com/uc?id=' + file_id1
dwn_url2='https://drive.google.com/uc?id=' + file_id2
dwn_url3='https://drive.google.com/uc?id=' + file_id3
dwn_url4='https://drive.google.com/uc?id=' + file_id4

data_gastosurl = pd.read_excel(dwn_url1)
data_hotelurl = pd.read_excel(dwn_url2)
lista_gastosurl = pd.read_excel(dwn_url3)
lista_habitacionesurl = pd.read_excel(dwn_url4)

st.sidebar.title("Home")
df = pd.read_excel("data_hotel.xlsx", sheet_name="Hoja1")
menu = st.sidebar.selectbox(
    " Selecione una opcion",
    ('Ingresar', '$ Gastos',  'Habitaciones'))
df = pd.read_excel("data_hotel.xlsx", sheet_name="Hoja1")
data_habitaciones = pd.read_excel("lista_habitaciones.xlsx", sheet_name="Hoja1")
#st.write(data_habitaciones)
df_habitacionesfiltro = data_habitaciones["Estado"] == "Libre"
filtro = data_habitaciones[df_habitacionesfiltro]
df_habitacionesfiltro2 = data_habitaciones["Estado"] == "Ocupado"
filtro2 = data_habitaciones[df_habitacionesfiltro2]
data_gastos = pd.read_excel("lista_gastos.xlsx", sheet_name = "Hoja1")

if menu == "Ingresar":
	user = st.sidebar.text_input("Ingrese un Usuario",)
	password = st.sidebar.text_input("Ingrese una Contraseña", type="password")
	button = st.sidebar.button("Ingresar")
	if user == "Administrador" and password == "6543":
		st.title("Gastos")
		fig = px.bar(data_gastos, x="Fecha", y="Monto", color="Descripcion", barmode="group")
		st.write(fig)
		st.title("Recaudación")



	if user == "Vendedor 1" and password == "4321":
		st.write("El usuario y contraseña son correctas")
		st.title("Check_in")
		Habitacion = st.selectbox("Escoja Habitacion", filtro["Habitacion"].unique())
		Nombre = st.text_input("Nombre y Apellido")
		Cedula = st.text_input("RUC o Numero de Cedula")
		ciudad = st.text_input("Ciudad")
		Pasajeros = st.text_input("Numero_Pasajeros")
		Email = st.text_input("Email")
		Telefono = st.text_input("Telefono")
		Entrada = st.date_input("Entrada")
		Salida= st.date_input("Salida")
		Pago = st.radio("Seleccione un Metodo de Pago",
		("Efectivo", "Tarjeta de Credito"))
		Cobro = st.number_input("Cantidad por Cobrar", min_value=15, value=1000)
		df = df.append({"Habitacion":Habitacion,
					"Nombre y Apellido":Nombre,
					"RUC o Numero de Cedula":Cedula,
					"Ciudad":ciudad,
					"Pasajeros":Pasajeros,
					"Email":Email,
					"Telefono":Telefono,
					"Entrada":Entrada,
					"Salida":Salida,
					"Metodo de Pago":Pago,
					"Cantidad por Cobrar":Cobro
                   	},ignore_index = True)

		if st.button("Guardar"):
			df.to_excel("data_hotel.xlsx",sheet_name ="Hoja1", index = False)
			data_habitaciones.to_excel("lista_habitaciones.xlsx", sheet_name = "Hoja1", index = False)

		#data_habitaciones.loc[data_habitaciones.Habitacion == Habitacion , "Estado" ] = "Ocupado"
		#st.write(data_habitaciones)

	if user == "Vendedor 2" and password == "54321": 
		st.write("El usuario y contraseña son correctas")
		st.title("Check_in")
		Habitacion = st.selectbox("Escoja Habitacion", filtro["Habitacion"].unique())
		Nombre = st.text_input("Nombre y Apellido")
		Cedula = st.text_input("RUC o Numero de Cedula")
		ciudad = st.text_input("Ciudad")
		Pasajeros = st.text_input("Numero_Pasajeros")
		Email = st.text_input("Email")
		Telefono = st.text_input("Telefono")
		Entrada = st.date_input("Entrada")
		Salida= st.date_input("Salida")
		Pago = st.radio("Seleccione un Metodo de Pago",
		("Efectivo", "Tarjeta de Credito"))
		Cobro = st.number_input("Cantidad por Cobrar", min_value=15, value=1000)
		df = df.append({"Habitacion":Habitacion,
					"Nombre y Apellido":Nombre,
					"RUC o Numero de Cedula":Cedula,
					"Ciudad":ciudad,
					"Pasajeros":Pasajeros,
					"Email":Email,
					"Telefono":Telefono,
					"Entrada":Entrada,
					"Salida":Salida,
					"Metodo de Pago":Pago,
					"Cantidad por Cobrar":Cobro
                   	},ignore_index = True)
		placeholder = st.empty()

		if st.button("Guardar"):
			df.to_excel("data_hotel.xlsx",sheet_name ="Hoja1", index = False)
			data_habitaciones.to_excel("lista_habitaciones.xlsx", sheet_name = "Hoja1", index = False)
		data_habitaciones.loc[data_habitaciones.Habitacion == Habitacion , "Estado" ] = "Ocupado"
		st.write(data_habitaciones)

	

	if user == "Limpieza" and password == "251200":
		st.title("Limpieza")
		Habitacion = st.selectbox("Escoja Habitacion", filtro2["Habitacion"].unique())
		estado = st.selectbox("Estado de la Habitacion",
		("Libre","Mantenimiento"))
		st.write(data_habitaciones)
		if st.button("Guardar"):
			data_habitaciones.to_excel("lista_habitaciones.xlsx", sheet_name="Hoja1",index=False)


if menu == "Habitaciones":
	st.write(df)
	df_estadisticas= df.describe()
	st.write(df_estadisticas)
	df_monto = df["Cantidad por Cobrar"].sum()
	st.write(df_monto)
if menu == "$ Gastos":
	st.title("Gastos del dia")
	Fecha = st.date_input("Ingrese la Fecha")
	gastos2 = st.selectbox("Descripcion",
		("Agua","Luz","Internet"))
	monto = st.number_input("Monto")
	data_gastos = data_gastos.append({"Fecha":Fecha,
									  "Descripcion": gastos2,
									  "Monto": monto
									  },ignore_index = True)
	if st.button("Guardar"):
		data_gastos.to_excel("lista_gastos.xlsx", sheet_name = "Hoja1", index = False)


