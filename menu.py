import PySimpleGUI as sg
from logica import crear_archivo_de_goles, crear_archivo_de_animales, construir_menu

def mod_menu():
    menu = construir_menu()
    while True:
        event, _values= menu.read()
        
        if event == "-SALIR-" or event == sg.WINDOW_CLOSED:
            break
        elif event == "-GOLES-":
            crear_archivo_de_goles()
        elif event == "-ANIMALES-":
            crear_archivo_de_animales()      
    menu.close()
