import pandas as pd

"""
Link para descargar archivos csv
https://www.kaggle.com/datasets/maicolab/university-admission/data?select=resultados_dia3.csv

En este archivo se cargans los csv, se unen, para luego seleccionar con que columnas se va a trabajar
Se reemplazan ',' por '.' en los datos numericos (notas de cada duia)
"""

#lee y le asigna el contenido de los csv a una variable cada uno
df1 = pd.read_csv('resultados_dia1.csv')
df2 = pd.read_csv('resultados_dia2.csv')
df3 = pd.read_csv('resultados_dia3.csv')

#Une df1 y 2 
df_union_1_2 = pd.merge(df1,df2, on=['Código'], how='outer')
#une a los anterior el df3
df_total = pd.merge(df_union_1_2,df3, on=['Código'], how='outer')

#imprime columnas para luego ver cuales quiero, y que nombre tienen
print(df_total.columns)

#Selecciono columnas 'Código','Nombre','Puntaje_x','Puntaje_y','Prueba 3'
df = df_total[['Código','Nombre','Puntaje_x','Puntaje_y','Prueba 3']]

#Renombra columnas
df.rename(columns={'Puntaje_x':'Nota_dia_1',
                   'Puntaje_y':'Nota_dia_2',
                   'Prueba 3':'Nota_dia_3'}, inplace=True)

#Exporta nuevo csv con las columnas seleccionadas
df.to_csv('Notas dia 1,2 y 3.csv',index=False)
print(df)

#Las notas estan en formato string, asi que primero se reemplazaa la coma por punto: luego se convierte a float o entero
#Hay datos dentro de las notas que dicen 'Ausente', en este los datos que no pueda convertir a numero los deja vacios
df['Nota_dia_1'] = pd.to_numeric(
    df['Nota_dia_1'].str.replace(',','.', regex=False),errors='coerce')
df['Nota_dia_2'] = pd.to_numeric(
    df['Nota_dia_2'].str.replace(',','.', regex=False),errors='coerce')
df['Nota_dia_3'] = pd.to_numeric(
    df['Nota_dia_3'].str.replace(',','.', regex=False),errors='coerce')


print(df)




