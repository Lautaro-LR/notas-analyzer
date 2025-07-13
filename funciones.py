import pandas as pd
from limpieza_csv import df
import tkinter as tk
"""
Cada dia tiene un puntaje maximo diferente
Puntaje max dia 1:745
Puntaje max dia 2:600
Puntaje max dia 3:500
No se aclara con cuanto se aprueba asi que tomare el 60% de cada puntaje maximo
"""

#Limpia los label de la parte superior
#-------------------------------------------------------------------------------------------------------------
def funcion_limpiar_parte_superior(label1,label2,label3):
    """
    Limpia 3 etiquetas de tkinter

    Parametros:
    label1 (tk.Label): Primera etiqueta a limpiar,
    label2 (tk.Label): Segunda etiqueta a limpiar,
    label3 (tk.Label): Tercer etiqueta a limpiar
    """

    label1.config(text='')
    label2.config(text='')
    label3.config(text='')

#Limpia los label de la parte inferior
#-------------------------------------------------------------------------------------------------------------

def funcion_limpiar_parte_inferior(label1):
    """
    Limpia texto de una etiqueta de tkinter

    Parametro:
    label1 (tk.label): etiqueta a limpiar
    """
    label1.config(text='')

#Cuenta la cantidad de alumnos inscriptos, va a ser la misma en los 3 dias. Luego coloca ese num en los label superiores
#-------------------------------------------------------------------------------------------------------------
def funcion_contar_inscriptos(label1,label2,label3):
    """
    Cuenta la cantidad de valores unicos que hay en la columna 'Código'
    Luego modifica el texto de 3 labels con ese resultado

    Parametros:
    label1 (tk.Label): Primera etiqueta a modificar,
    label2 (tk.Label): Segunda etiqueta a modificar,
    label3 (tk.Label): Tercer etiqueta a modificar
    """
    cantidad_inscriptos = df['Código'].nunique()
    cantidad_inscriptos_str = str(cantidad_inscriptos)
    label1.config(text=f'{cantidad_inscriptos_str}')
    label2.config(text= f'{cantidad_inscriptos_str}')
    label3.config(text=f'{cantidad_inscriptos_str}')

#Cuenta la cantidad de alumnos que asistieron cada dia
#-------------------------------------------------------------------------------------------------------------
def funcion_asistencia(label1,label2,label3):
    """
    Cuenta la cantidad de alumnos que asistieron cada dia, tomando como asistencia aquellos que tienen nota
    y como ausente a los que en su nota tienen un valor Nan
    Esos resultados de asistencia luego se colocan en 3 labels, uno por cada dia de examen

    Parametros:
    label1 (tk.Label): Primera etiqueta a modificar,
    label2 (tk.Label): Segunda etiqueta a modificar,
    label3 (tk.Label): Tercer etiqueta a modificar
    """
    alumnos_que_asistieron_dia1 = df['Nota_dia_1'].count()
    alumnos_que_asistieron_dia2 = df['Nota_dia_2'].count()
    alumnos_que_asistieron_dia3 = df['Nota_dia_3'].count()
    label1.config(text = f'{alumnos_que_asistieron_dia1}')
    label2.config(text = f'{alumnos_que_asistieron_dia2}')
    label3.config(text = f'{alumnos_que_asistieron_dia3}')

#Promedia nota de cada dia
#-------------------------------------------------------------------------------------------------------------
def funcion_promedio_puntaje(label1,label2,label3):
    """
    Promedia las notas obtenidas en cada dia, luego modifica el texto de 3 labels para mostrar resultados

    Parametros:
    label1 (tk.Label): Primera etiqueta a modificar,
    label2 (tk.Label): Segunda etiqueta a modificar,
    label3 (tk.Label): Tercer etiqueta a modificar
    """

    promedio_dia1 = df['Nota_dia_1'].mean()
    promedio_dia2 = df['Nota_dia_2'].mean()
    promedio_dia3 = df['Nota_dia_3'].mean()
    label1.config(text =f'{promedio_dia1:.2f}')
    label2.config(text =f'{promedio_dia2:.2f}')
    label3.config(text =f'{promedio_dia3:.2f}')

#Porcentaje de aprobados
#-------------------------------------------------------------------------------------------------------------
def funcion_porcentaje_aprobados(label1,label2,label3):
    """
    Calcula porcentaje de aprobados por dia, tomando como referencia que se aprueba con una nota superior
    o igual al 60%, muestra los resultados en 3 labels

    Parametros:
    label1 (tk.Label): Primera etiqueta a modificar,
    label2 (tk.Label): Segunda etiqueta a modificar,
    label3 (tk.Label): Tercer etiqueta a modificar
    """
    #Elimino valores nan o no numericos
    notas1 = df['Nota_dia_1'].dropna()
    notas2 = df['Nota_dia_2'].dropna()
    notas3 = df['Nota_dia_3'].dropna()
    #Promedio los alumnos que obtuvieron una nota mayor o igual al 60%
    aprobados_dia1 = (notas1>=(745*0.6)).mean()*100
    aprobados_dia2 = (notas2>=(600*0.6)).mean()*100
    aprobados_dia3 = (notas3>=(500*0.6)).mean()*100
    #Muestro los resultados, con 2 decimales
    label1.config(text = f'{aprobados_dia1:.2f}%')
    label2.config(text = f'{aprobados_dia2:.2f}%')
    label3.config(text = f'{aprobados_dia3:.2f}%')

#Porcentaje de asistencia
#-------------------------------------------------------------------------------------------------------------
def funcion_porcentaje_asistencia(label1,label2,label3):
    """
    Calcula porcentaje de asistencia por cada uno de los dias de examen
    Luego los resultados se colocan en 3 labels, uno por cada dia

    Parametros:
    label1 (tk.Label): Primera etiqueta a modificar,
    label2 (tk.Label): Segunda etiqueta a modificar,
    label3 (tk.Label): Tercer etiqueta a modificar
    """
    asistencia_dia1 = (df['Nota_dia_1'].count()/6176)*100
    asistencia_dia2 = (df['Nota_dia_2'].count()/6176)*100
    asistencia_dia3 = (df['Nota_dia_3'].count()/6176)*100

    label1.config(text =f'{asistencia_dia1:.2f}%')
    label2.config(text =f'{asistencia_dia2:.2f}%')
    label3.config(text =f'{asistencia_dia3:.2f}%')

#Porcentaje de faltas
#-------------------------------------------------------------------------------------------------------------
def funcion_porcentaje_faltas(label1,label2,label3):
    """
    Calcula porcentaje de falta por cada uno de los dias de examen
    Luego los resultados se colocan en 3 labels, uno por cada dia

    Parametros:
    label1 (tk.Label): Primera etiqueta a modificar,
    label2 (tk.Label): Segunda etiqueta a modificar,
    label3 (tk.Label): Tercer etiqueta a modificar
    """
    faltas_dia1 = ((6176-df['Nota_dia_1'].count())/6176)*100
    faltas_dia2 = ((6176-df['Nota_dia_2'].count())/6176)*100
    faltas_dia3 = ((6176-df['Nota_dia_3'].count())/6176)*100

    label1.config(text=f'{faltas_dia1:.2f}%')
    label2.config(text=f'{faltas_dia2:.2f}%')
    label3.config(text=f'{faltas_dia3:.2f}%')

#Buscar por nombre
#-------------------------------------------------------------------------------------------------------------
def funcion_buscar_por_nombre(nombre_entry,label_resultado):
    """
    Busca en el archivo csv un nombre que obtiene a partir de un tk.Entry
    en caso de encontrar el nombre utiliza esos datos para modificar el texto de un label, mostrando: Nombre-Nota_dia_1-Nota_dia2-Nota_dia3;
    caso contrario se mostrara un mnj que especifica que no se encontro el nombre buscado

    Parametros:
    nombre_entry (tk.Entry): nombre a buscar
    label_resultado(tk.Label): Etiqueta donde se mostrara el resultado 
    """
    nombre = nombre_entry.get()
    alumno = df[df['Nombre'] == nombre]
    if alumno.empty:
        label_resultado.config(text = 'No se ha encontrado ningun resultado para ese nombre')
    else:
        alumno = alumno.drop(columns='Código')
        label_resultado.config(text = alumno.to_string(index=False, col_space=20))

def funcion_buscar_por_codigo(codigo_entry,label_resultado):
    """
    Busca en el archivo csv un codigo que obtiene a partir de un tk.Entry
    en caso de encontrar el codigo utiliza esos datos para modificar el texto de un label, mostrando: Nombre-Nota_dia_1-Nota_dia2-Nota_dia3;
    caso contrario se mostrara un mnj que especifica que no se encontro el codigo buscado

    Parametros:
    nombre_entry (tk.Entry): codigo a buscar
    label_resultado(tk.Label): Etiqueta donde se mostrara el resultado    
    """
    codigo = codigo_entry.get()
    alumno = df[df['Código'] == codigo]
    if alumno.empty:
        label_resultado.config(text = 'No se ha encontrado ningun resultado para ese codigo')
    else:
        alumno = alumno.drop(columns='Código')
        label_resultado.config(text = alumno.to_string(index=False, col_space=20))



    

