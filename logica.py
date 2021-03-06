import csv
import PySimpleGUI as sg
import json

def construir_menu():
    """Esta función define las caracteristicas de la ventana principal y devuelve la ventana creada"""
    """Ventana: -Boton para Crear archivo de goles de Messi
                -Boton para Crear archivo de animales
                -Boton para salir(unica forma de cerrar la ventana"""
    layout=[[sg.Text("-Elige una opción-")],[sg.Button("Goles de cabeza de Lionel Messi", size =(50, 10), key = "-GOLES-")], [sg.Button("Animales de la familia de los elefantes", size =(50, 10), key = "-ANIMALES-")], [sg.Button("Salir", size =(50, 10), key = "-SALIR-")]]
    menu = sg.Window("ACTIVIDAD 1 POR Python Plus - TEORIA -", layout, no_titlebar = True)
    return menu

def crear_archivo_de_goles(): 
    """
    Esta función crea un archivo de texto, en la carpeta de del repositorio local con la informacion de los goles de cabeze de Messi
    El archivo creado tiene formato JSON, con:
        -El equipo contrario
        -El minuto en que fue hecho
        -La competicion (Liga o Champions)
    Los datos se obtienen de un archivo csv
    """

    archivo = open("Lionel Messi Goals.csv", "r")
    arch = open("Archivo de goles de cabeza con Formato JSON", "w")

    csvreader = csv.reader(archivo, delimiter=';')
    
    csvreader.__next__()

    datos = {"Cont":"Contrario","Min": "Minuto","Com": "Competicion"}
    json.dump(datos, arch)

    for linea in csvreader:
        if linea[9] == "Head":            
            datos = {"Cont":linea[3],"Min":linea[5],"Com":linea[1]}
            json.dump(datos, arch)
    archivo.close()
    arch.close()

def crear_archivo_de_animales():
    """
    Crea un archivo de texto con formato JSON de animales de la familia de los elefantes
    Los datos del Texto son:
    -Nombre de la Especie
    -La Familia, en este caso de elefantes
    -La Clase, en este caso Mamifero
    """

    archivo = open("animals.csv", "r")
    arch = open("Archivo de Animales con Formato JSON", "w")

    csvreader = csv.reader(archivo, delimiter=',')
    
    csvreader.__next__()

    datos = {"Nom":"Nombre","Familia": "Familia","Clase": "Clase"}
    json.dump(datos, arch)
    
    for linea in csvreader:
        if linea[12] == "Elephantidae":            
            datos = {"Nom":linea[1],"Familia":linea[12],"Clase":linea[5]}
            json.dump(datos, arch)
    archivo.close()
    arch.close()







    
