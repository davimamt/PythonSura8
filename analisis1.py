from cgitb import html
import pandas as pd 

#CARGAR DATOS
dataFrame=pd.read_csv('./empleados.csv')
#print(dataFrame)

#CARGAR TODOS LOS DATOS
#print(dataFrame.to_string())

#CARGAR LOS PRIMERO N REGISTROS DE UN BANCO DE DATOS
#print(dataFrame.head(20))


#CARGAR LOS ULTIMO N REGISTROS DE UN BANCO DE DATOS
#print(dataFrame.tail(20))

#OBTENER INFORMACION DE LOS DATOS CARGADOS
#print(dataFrame.info())
#print(dataFrame.describe())


#ACCEDER A DATOS O REGISTROS ESPECIFICOS
#print(dataFrame["nombres"].head())
#print(dataFrame["salario"].tail())

#ACCEDER A REGISTROS POR SU INDICE
#print(dataFrame.iloc[20:30])
#print(dataFrame.iloc[[10,20,30,40]])
'''
tabla=(dataFrame.loc[[4, 25], ["nombres"]])
html=tabla.to_html()
text_file=open("index.html", "w")
text_file.write(html)
text_file.close()
'''

#filtros con condiciones logicas
print(dataFrame[(dataFrame["salario"]>5500000) & (dataFrame["cargo"]=="analista2")])