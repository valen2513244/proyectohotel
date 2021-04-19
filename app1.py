import streamlit as st 
import pandas as pd
import altair as alt
from datetime import time
import openpyxl 
#import smtplib as ssl

st.sidebar.title("Home")

menu = st.sidebar.selectbox(
    " Selecione una opcion",
    ('Ingresar', '$ Gastos',  'Habitaciones'))
df = pd.read_excel("data_hotel.xlsx", sheet_name="Hoja1")
data_habitaciones = pd.read_excel("lista_habitaciones.xlsx", sheet_name="Hoja1")
#st.write(data_habitaciones)
df_habitacionesfiltro = data_habitaciones["Estado"] == "Libre"
filtro = data_habitaciones[df_habitacionesfiltro]
data_gastos = pd.read_excel("lista_gastos.xlsx", sheet_name = "Hoja1")

if menu == "Ingresar":
	user = st.sidebar.text_input("Ingrese un Usuario",)
	password = st.sidebar.text_input("Ingrese una Contraseña", type="password")
	button = st.sidebar.button("Ingresar")
	if user == "valentin" and password == "1234":
		st.write("El usuario y contraseña son correctas")	
	if user == "Paulo" and password == "paulo":
		st.write("El usuario y contraseña son correctas")
	if user == "Enganchador 1" and password == "4321":
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
		("Efectivo", "Tarjeta de Credito", "Paypal"))
		Cobro = st.number_input("Cantidad por Cobrar")
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
		
		data_habitaciones.loc[data_habitaciones.Habitacion == Habitacion , "Estado" ] = "Ocupado"
		st.write(data_habitaciones)

		if st.button("Actualizar"):
			data_habitaciones.to_excel("lista_habitaciones.xlsx", sheet_name = "Hoja1", index = False)
	if user == "Enganchador 2" and password == "54321":
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
		("Efectivo", "Tarjeta de Credito", "Paypal"))
		Cobro = st.number_input("Cantidad por Cobrar")
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
			Nombre = placeholder.text_input("Nombre y Apellido", value='', key=1)
			
		data_habitaciones.loc[data_habitaciones.Habitacion == Habitacion , "Estado" ] = "Ocupado"
		st.write(data_habitaciones)

		if st.button("Actualizar"):
			data_habitaciones.to_excel("lista_habitaciones.xlsx", sheet_name = "Hoja1", index = False)

		#else:
			#st.write("Usuario o contraseña son incorrectas"
	if user == "Limpieza" and password == "251200":
		hab = st.text_input("Habitacion")
		estado = st.selectbox("Estado de la Habitacion",
		("Libre","Mantenimiento"))
		problema = st.text_input("Problemas")
		st.write(data_habitaciones)
	else:
		st.write("El usuario o contraseña son incorrectos")


if menu == "Habitaciones":
	df = pd.read_excel("data_hotel.xlsx", sheet_name="Hoja1")
	st.write(df)

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

	grafico1 = alt.Chart(data_gastos).mark_bar().encode()
	st.altair_chart(grafico1)
	st.write(data_gastos)

