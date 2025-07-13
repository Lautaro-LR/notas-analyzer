import tkinter as tk
from funciones import funcion_limpiar_parte_inferior,funcion_limpiar_parte_superior,funcion_contar_inscriptos,funcion_asistencia,funcion_promedio_puntaje
from funciones import funcion_buscar_por_codigo,funcion_porcentaje_aprobados, funcion_porcentaje_asistencia,funcion_porcentaje_faltas, funcion_buscar_por_nombre

ventana = tk.Tk()

#variables para espaciado,alto y ancho de botones
#-------------------------------------------------------------------------------------------------------------
alto = 1                    #Alto estandar para botones
ancho = 25                  #Ancho estandar para botones
Separacion_estandar_x = 8   #Espacio horizontal entre widgets
Separacion_estandar_y = 8   #Espacio vertical entre widgets

#Titulo dias, y labels para dar resultados debajo del titulo de cada dia
#-------------------------------------------------------------------------------------------------------------
dia_1 = tk.Label(ventana, text='     Dia 1     ',relief="solid")
dia_1.grid(row=0, column=2,padx=10,pady=10,)

dia_2 = tk.Label(ventana, text='     Dia 2     ',relief="solid")
dia_2.grid(row=0, column=3,padx=10,pady=10,)

dia_3 = tk.Label(ventana, text='     Dia 3     ',relief="solid")
dia_3.grid(row=0, column=4,padx=10,pady=10,)

info_dia_1 = tk.Label(ventana, text='',
    width=2, height=2,
    relief="solid", bd=2,
    fg="black", bg="white", highlightbackground="red", 
    highlightthickness=2)
info_dia_1.grid(row=1,column=2, columnspan=1, rowspan=1,padx=7,pady=7,sticky='nsew')

info_dia_2 = tk.Label(ventana, text='',
    width=2, height=2,
    relief="solid", bd=2,
    fg="black", bg="white", highlightbackground="red", 
    highlightthickness=2)
info_dia_2.grid(row=1,column=3, columnspan=1, rowspan=1,padx=7,pady=7,sticky='nsew')

info_dia_3 = tk.Label(ventana, text='',
    width=2, height=2,
    relief="solid", bd=2,
    fg="black", bg="white", highlightbackground="red", 
    highlightthickness=2)
info_dia_3.grid(row=1,column=4, columnspan=1, rowspan=1,padx=7,pady=7,sticky='nsew')

#Botones parte superior
#-------------------------------------------------------------------------------------------------------------
boton_prom_puntaje = tk.Button(ventana, text= 'Promedio puntaje',width=ancho, height=alto, command=lambda : funcion_promedio_puntaje(info_dia_1,info_dia_2,info_dia_3))
boton_prom_puntaje.grid(row=3,column=0,padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

boton_alumnos_asistieron = tk.Button(ventana, text= 'Alumnos que asistieron',width=ancho, height=alto, command=lambda: funcion_asistencia(info_dia_1,info_dia_2,info_dia_3))
boton_alumnos_asistieron.grid(row=1,column=0,padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

boton_cantidad_alumnos_inscriptos = tk.Button(ventana,text='Alumnos inscriptos',width=ancho, height=alto, command=lambda: funcion_contar_inscriptos(info_dia_1,info_dia_2,info_dia_3))
boton_cantidad_alumnos_inscriptos.grid(row=2,column=0,padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

boton_porcentaje_aprobados = tk.Button(ventana,text='Porcentaje de aprobados',width=ancho, height=alto,command=lambda: funcion_porcentaje_aprobados(info_dia_1,info_dia_2,info_dia_3))
boton_porcentaje_aprobados.grid(row=3,column=1,padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

boton_porcentaje_faltas = tk.Button(ventana,text='Porcentaje de faltas',width=ancho, height=alto,command=lambda : funcion_porcentaje_faltas(info_dia_1,info_dia_2,info_dia_3))
boton_porcentaje_faltas.grid(row=1,column=1,padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

boton_porcentaje_asistencia = tk.Button(ventana, text='Porcentaje asistencia',width=ancho, height=alto,command=lambda : funcion_porcentaje_asistencia(info_dia_1,info_dia_2,info_dia_3))
boton_porcentaje_asistencia.grid(row=2,column=1, padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

#Boton limpiar parte superior
#-------------------------------------------------------------------------------------------------------------
boton_limpiar_superior = tk.Button(ventana,text='Limpiar', width=ancho, height=alto,command=lambda: funcion_limpiar_parte_superior(info_dia_1,info_dia_2,info_dia_3) )
boton_limpiar_superior.grid(row=0, column=5,padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

#Linea que separa parte superior de inferior
#-------------------------------------------------------------------------------------------------------------
linea_mitad = tk.Frame(ventana,height=2,bg='black', relief='ridge')
linea_mitad.grid(row=4,column=0,columnspan=20,sticky='ew',padx=5,pady=5)

#Botones parte inferior
#-------------------------------------------------------------------------------------------------------------
boton_buscar_por_nombre = tk.Button(ventana, text='Buscar alumno por nombre: ',width=ancho, height=alto, command=lambda : funcion_buscar_por_nombre(nombre_para_buscar,label_resultado_busqueda))
boton_buscar_por_nombre.grid(row=5, column=0, padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

boton_buscar_por_codigo = tk.Button(ventana, text='Buscar alumno por codigo: ',width=ancho, height=alto, command=lambda : funcion_buscar_por_codigo(codigo_para_buscar,label_resultado_busqueda))
boton_buscar_por_codigo.grid(row=6, column=0, padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

#Entrada de nombre y codigo
#-------------------------------------------------------------------------------------------------------------
nombre_para_buscar = tk.Entry(ventana,width=35)
nombre_para_buscar.grid(row=5, column=1)

codigo_para_buscar = tk.Entry(ventana,width=35)
codigo_para_buscar.grid(row=6, column=1)

#Label para mostrar resultados de la buqueda
#-------------------------------------------------------------------------------------------------------------
label_resultado_busqueda = tk.Label(ventana, text='',
    width=30, height=3,
    relief="solid", bd=2,
    fg="black", bg="white", highlightbackground="red", 
    highlightthickness=2,justify='left',anchor='nw',
    font=('Courier', 11))
label_resultado_busqueda.grid(row=7,column=0, columnspan=7, rowspan=1,padx=7,pady=7,sticky='nsew')

#Boton limpiar parte inferior
#-------------------------------------------------------------------------------------------------------------
boton_limpiar_inferior = tk.Button(ventana,text='Limpiar', width=ancho, height=alto, command=lambda: funcion_limpiar_parte_inferior(label_resultado_busqueda))
boton_limpiar_inferior.grid(row=5, column=5,padx=Separacion_estandar_x,pady=Separacion_estandar_y,sticky='w')

ventana.mainloop()
    