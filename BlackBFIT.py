'''
BlackBFIT
Autores: Gaston Violla
         Rachel Herbas
         Nestor Schygiel  
Version: 3.0
'''

import json
import os
import getpass
from colorama import init, Fore, Style
from datetime import datetime

# Inicializar colorama
init(autoreset=True)

# Archivo JSON para guardar datos de usuarios
USERS_FILE = 'usuarios.json'

# Funciones para manejo de usuarios
def cargar_usuarios():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    return {}

def guardar_usuarios(usuarios):
    with open(USERS_FILE, 'w') as file:
        json.dump(usuarios, file, indent=4)

def registrar_usuario(usuarios):
    print("="*45)
    print(Fore.GREEN + "Registro de usuario".center(45))
    username = input("Nombre de usuario: ")
    if username in usuarios:
        print(Fore.RED + "El usuario ya existe. Intente con otro nombre.")
        return None
    password = getpass.getpass("Contraseña: ")
    fecha_ingreso = datetime.now().strftime("%d-%m-%Y") #para dar formato a la fecha
    usuarios[username] = {"password": password, "fecha_ingreso": fecha_ingreso, "rutinas": {}}
    guardar_usuarios(usuarios)
    print(Fore.GREEN + "Usuario registrado con éxito.".center(45))
    print("="*45)
    return username

def iniciar_sesion(usuarios):
    print(Fore.GREEN + "Inicio de sesión".center(45))
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")
    if username in usuarios and usuarios[username]['password'] == password:
        print(Fore.GREEN + "Inicio de sesión exitoso.".center(45))
        return username
    else:
        print(Fore.RED + "Usuario o contraseña incorrectos.")
        return None

# Definición de la rutina por 5 días
rutina_5_dias = {
    "Día 1: Piernas y Glúteos": [
        "Calentamiento: 5-10 minutos de cardio (cinta de correr, bicicleta estática, elíptica, etc.).",
        "Sentadillas: 3 series de 12 repeticiones.",
        "Peso muerto: 3 series de 10 repeticiones.",
        "Zancadas: 3 series de 12 repeticiones (cada pierna).",
        "Elevaciones de cadera: 3 series de 15 repeticiones.",
        "Extensiones de piernas: 3 series de 12 repeticiones.",
        "Curl de piernas: 3 series de 12 repeticiones."
    ],
    "Día 2: Abdominales y Cardio": [
        "Calentamiento: 5-10 minutos de cardio.",
        "Plancha: 3 series de 30-60 segundos.",
        "Crunches: 3 series de 15 repeticiones.",
        "Giros rusos: 3 series de 12 repeticiones (cada lado).",
        "Mountain climbers: 3 series de 12 repeticiones (cada lado).",
        "Cardio de elección (correr, saltar la cuerda, bicicleta, etc.): 20-30 minutos."
    ],
    "Día 3: Brazos y Hombros": [
        "Calentamiento: 5-10 minutos de cardio.",
        "Press de hombros con mancuernas: 3 series de 12 repeticiones.",
        "Flexiones de brazos: 3 series de 10 repeticiones.",
        "Curl de bíceps con mancuernas: 3 series de 12 repeticiones.",
        "Tríceps en polea alta: 3 series de 12 repeticiones.",
        "Elevaciones laterales de hombros: 3 series de 12 repeticiones."
    ],
    "Día 4: Espalda y Cardio": [
        "Calentamiento: 5-10 minutos de cardio.",
        "Remo con barra: 3 series de 12 repeticiones.",
        "Dominadas asistidas o jalones en polea: 3 series de 10 repeticiones.",
        "Peso muerto rumano: 3 series de 10 repeticiones.",
        "Hip thrust con barra: 3 series de 12 repeticiones.",
        "Cardio de elección: 20-30 minutos."
    ],
    "Día 5: Cuerpo completo y Cardio": [
        "Calentamiento: 5-10 minutos de cardio.",
        "Burpees: 3 series de 10 repeticiones.",
        "Sentadillas con salto: 3 series de 12 repeticiones.",
        "Flexiones de brazos: 3 series de 10 repeticiones.",
        "Plancha: 3 series de 30-60 segundos.",
        "Cardio de elección: 20-30 minutos."
    ]
}

def mostrar_rutina_5_dias():
    for dia, ejercicios in rutina_5_dias.items():
        print(Fore.YELLOW + f"\n{dia}:")
        for ejercicio in ejercicios:
            print(f"- {ejercicio}")

# Funciones del menú
def mostrar_rutina(rutina):
    for dia, ejercicios in rutina.items():
        print(Fore.YELLOW + f"\n{dia.capitalize()}:")
        for ejercicio in ejercicios:
            print(f"- {ejercicio['nombre']}: {ejercicio['series']} series de {ejercicio['repeticiones']} reps con {ejercicio['peso']} kg")

def crear_rutina_personalizada(usuario, usuarios):
    print(Fore.CYAN + "Creando rutina personalizada...".center(45))
    print("*"*45)
    rutina = {}
    for i in range(1, 6): #elemento que esta corriendo del 1 al 6 
        dia = f"dia {i}"
        ejercicios = []
        while True:
            ejercicio = {}
            ejercicio['nombre'] = input(Fore.GREEN + f"Nombre del ejercicio para el {dia} (o 'fin' para terminar): ")
            if ejercicio['nombre'].lower() == 'fin':
                break
            ejercicio['series'] = int(input("Número de series: "))
            ejercicio['repeticiones'] = int(input("Número de repeticiones: "))
            ejercicio['peso'] = float(input("Peso (kg): "))
            ejercicios.append(ejercicio)
        rutina[dia] = ejercicios
    usuarios[usuario]['rutinas'] = rutina
    guardar_usuarios(usuarios)
    print(Fore.GREEN + "Rutina personalizada creada con éxito.")

def ver_rutina_personalizada(usuario, usuarios):
    print(Fore.CYAN + "Viendo rutina personalizada...")
    if 'rutinas' in usuarios[usuario]:
        mostrar_rutina(usuarios[usuario]['rutinas'])
    else:
        print(Fore.RED + "No tiene ninguna rutina personalizada. Cree una primero.")

def menu_principal(usuario, usuarios):
    while True:
        print(Fore.YELLOW + "Menú principal".center(45))
        print(Fore.YELLOW + "\t1." + Fore.RESET + " Rutina por 5 días")
        print(Fore.YELLOW + "\t2." + Fore.RESET + " Crear rutina personalizada")
        print(Fore.YELLOW + "\t3." + Fore.RESET + " Ver rutina personalizada")
        print(Fore.YELLOW + "\t4." + Fore.RESET + " Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_rutina_5_dias()
        elif opcion == "2":
            crear_rutina_personalizada(usuario, usuarios)
        elif opcion == "3":
            ver_rutina_personalizada(usuario, usuarios)
        elif opcion == "4":
            print(Fore.GREEN + "Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción no válida")

def main():
    usuarios = cargar_usuarios()
    while True:
        print(Fore.YELLOW + "Bienvenido a BLACK B FIT".center(45))
        print("="*45)
        print(Fore.YELLOW + "\t1." + Fore.RESET + " Iniciar sesión")
        print(Fore.YELLOW + "\t2." + Fore.RESET + " Registrarse")
        print(Fore.YELLOW + "\t3." + Fore.RESET + " Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            usuario = iniciar_sesion(usuarios)
            if usuario:
                menu_principal(usuario, usuarios)
        elif opcion == "2":
            usuario = registrar_usuario(usuarios)
            if usuario:
                menu_principal(usuario, usuarios)
        elif opcion == "3":
            print("="*45)
            print(Fore.YELLOW + "Saliendo del programa, vuelva prontos...")
            break
        else:
            print(Fore.RED + "Opción no válida")

if __name__ == "__main__":
    main()