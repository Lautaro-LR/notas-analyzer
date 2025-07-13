# Analisis de notas, mostrando datos en interfaz grafica

Es proyecto es una aplicacion desarrollada con python, para analizar notas de alumnos en distintos dias de examen,
utilizando `pandas` para el manejo de datos, y `Tkinkter` para la interfaz grafica

-----

Funciones principales:
    - Cargar, leer y unir archivos csv con pandas
    - Botones para mostrar calculos y resultados en la interfaz
    - Busqueda de alumnos por nombre o codigo
    - Calculo de promedios, porcentaje de faltas, entre otros

-----

Estructura:
    - interfaz.py           #Archivo principal, interfaz grafica
    - funciones.py          #Funciones que se usan con los tk.button de la interfaz
    - limpieza_csv.py       #Une, y modela los datos de los csv
    - Notas dia 1,2 y 3     #csv que se crea en limpieza_csv.py, es el archivo usado para calcular funciones y demas
    - resultados_dia1       #csv de las notas del dia 1
    - resultados_dia1       #csv de las notas del dia 2
    - resultados_dia1       #csv de las notas del dia 3
    - README.md             #Documentacion del proyecto
    - venv                  #Entorno virtual

-----

Requisitos:
    - python 
    - pandas
    - tkinter

``bash

pip install pandas