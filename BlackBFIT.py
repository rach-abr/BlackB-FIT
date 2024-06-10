'''
BlackBFIT
Autores: Rachel Herbas, Gaston .., Nestor ... , Jose ...
Fecha: 2024
Version: 1.0
'''
import os 
import colorama
import time

def limpiarPantalla():
    os.system("cls")
    return

ejercicios = {
    "Pecho": ["Press de banca con barra, Apertura con mancuernas"],
    "Espalda": ["Dominadas, Remo con barra"],
    "Brazos": ["Extencion de triceps, Biceps con mancuernas"],
    "Hombros": ["Press militar, Elevaciones laterales"],
    "Piernas": ["Prensa de piernas, Sentadilla con barra"],
    "Gluteos": ["Hiptrust, Sentadilla sumo con peso"]
}

pesoKg = {
    "Pecho": [0,0],
    "Espalda": [0,0],
    "Brazos": [0,0],
    "Hombros": [0,0],
    "Piernas": [0,0],
    "Gluteos": [0,0]
}

def menu():
    limpiarPantalla()
    print(colorama.Fore.YELLOW + "BlackB FIT".center(45))
    print("="*45)
    print(colorama.Fore.YELLOW + "\t1" + colorama.Fore.RESET + " Pecho")
    print(colorama.Fore.YELLOW + "\t2" + colorama.Fore.RESET + " Espalda")
    print(colorama.Fore.YELLOW + "\t3" + colorama.Fore.RESET + " Brazos")
    print(colorama.Fore.YELLOW + "\t4" + colorama.Fore.RESET + " Hombros")
    print(colorama.Fore.YELLOW + "\t5" + colorama.Fore.RESET + " Piernas")
    print(colorama.Fore.YELLOW + "\t6" + colorama.Fore.RESET + " Gluteos")
    print(colorama.Fore.YELLOW + "\t7" + colorama.Fore.RESET + " Agregar/Modificar/Eliminar peso en KG")
    print(colorama.Fore.YELLOW + "\t8" + colorama.Fore.RESET + " Salir")
    op = int(input(colorama.Fore.MAGENTA + "Seleccione una zona a trabajar: ".center(45) + colorama.Fore.RESET ))
    return op

def gestionar_peso(zona):
    print(f"\nGestión de pesos para {zona}:")
    for x, ejercicio in enumerate(ejercicios[zona], 1):
        print(f"{x}. {ejercicio} - Peso actual: {pesoKg[zona][x - 1]} kg")
    opcion = int(input("Seleccione un ejercicio para modificar el peso (1-2): "))
    accion = input("Desea agregar/modificar/eliminar el peso (a/m/e): ").lower()
    if accion == 'a' or accion == 'm':
        nuevo_peso = float(input("Ingrese el nuevo peso: "))
        pesoKg[zona][opcion - 1] = nuevo_peso
        print(f"Peso actualizado: {pesoKg[zona][opcion - 1]} kg")
    elif accion == 'e':
        pesoKg[zona][opcion - 1] = 0
        print("Peso eliminado.")
    else:
        print("Acción no válida.")

#programa principal
colorama.init() 
terminos=[]
op = menu()
while op !=9:
    match op:
        case 1:
            print("agregar")
            agregar(terminos)
            time.sleep(5)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 2:
            print("modificar")
            modificar(terminos)
            input(colorama.Fore.RED + "Presione enter para continuar...")
        case 3:
            print("eliminar")
            eliminar(terminos)
            input(colorama.Fore.RED + "Presione enter para continuar...")
        case 4:
            print("buscar")
            buscar(terminos)
            input(colorama.Fore.RED + "Presione enter para continuar...")
        case 5:
            print("listar todos")
            listar(terminos)
            input(colorama.Fore.RED + "Presione enter para continuar...")
        case 6:
            print("listar todos")
            listar(terminos)
            input(colorama.Fore.RED + "Presione enter para continuar...")
        case 7:
            print("listar todos")
            listar(terminos)
            input(colorama.Fore.RED + "Presione enter para continuar...")
        case 8:
            print("listar todos")
            listar(terminos)
            input(colorama.Fore.RED + "Presione enter para continuar...")
        case _:
            print("error!")
            input(colorama.Fore.RED + "Presione enter para continuar...")
    op = menu()