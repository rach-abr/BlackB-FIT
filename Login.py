'''
BlackBFIT
Autores: Rachel Herbas, Gaston Violla, Nestor ... 
Version: 1.0
'''
import os
import json
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

def limpiarPantalla():
    os.system("cls")
    return

# Función para abrir o crear el archivo JSON y cargar los datos
def abrir_o_crear_json(nombre_archivo):
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                datos = json.load(f)
        except json.JSONDecodeError:
            datos = {}
    else:
        datos = {}
        with open(nombre_archivo, 'w') as f:
            json.dump(datos, f, indent=4)
    
    return datos

# Inicializar usuarios_registrados utilizando la función abrir_o_crear_json
usuarios_registrados = abrir_o_crear_json("usuarios.json")

class Persona:
    def __init__(self, nombre=None, apellido=None, dni=None, fecha_ingreso=None, contraseña=None):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_ingreso = fecha_ingreso
        self.contraseña = contraseña
        
    def registrarse(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.dni = input("Ingrese su DNI: ")
        self.fecha_ingreso = datetime.now().strftime("%d/%m/%y")
        self.contraseña = input("Escriba una contraseña: ")
        
        # Crea un nuevo registro de usuario
        nuevo_usuario = {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dni': self.dni,
            'fecha_ingreso': self.fecha_ingreso,
            'contraseña': self.contraseña
        }
        
        # Agregar nuevo usuario al diccionario de usuarios registrados
        usuarios_registrados[self.dni] = nuevo_usuario
        
        # Guardar todos los usuarios actualizados en el archivo usuarios.json
        guardar_datos()

# Función para guardar todos los datos actualizados en el archivo usuarios.json
def guardar_datos():
    with open("usuarios.json", 'w', encoding='utf-8') as f: # "w" -Escribir- Abre un archivo para escribir, crea el archivo si no existe.
        json.dump(usuarios_registrados, f, ensure_ascii=False, indent=4)

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios():
    print("Usuarios registrados: ")
    print(usuarios_registrados)

# Función para iniciar sesión
def sesion(usuario, contraseña):
    if not usuario or not contraseña:
        print("Ingrese un dato válido.")
    else:
        for dni, datos_usuario in usuarios_registrados.items():
            if usuario == datos_usuario["nombre"] and contraseña == datos_usuario["contraseña"]:
                print("Inicio de sesión exitoso.")
                return
        print("Usuario o contraseña incorrectos.")

# Función para mostrar el menú principal
def mostrar_menu():
    print(Fore.YELLOW + "BlackB FIT".center(45))
    print(Fore.YELLOW + "Menú Principal".center(45))
    print("="*45)
    print(Fore.YELLOW + "\t1" + Fore.RESET + " Registrarse")
    print(Fore.YELLOW + "\t2" + Fore.RESET + " Iniciar sesión")
    print(Fore.YELLOW + "\t3" + Fore.RESET + " Ver usuarios registrados")
    print(Fore.YELLOW + "\t4" + Fore.RESET + " Salir")

# Función principal del programa
def main():
   while True:
       mostrar_menu()
       opcion = input("Seleccione una opción: ")
       
       if opcion == "1":
           persona = Persona()
           persona.registrarse()
       elif opcion == "2":
           usuario = input("Ingrese su nombre: ")
           contraseña = input("Ingrese su contraseña: ")
           sesion(usuario, contraseña)
       elif opcion == "3":
           mostrar_usuarios()
       elif opcion == "4":
           print("="*45)
           print(Fore.YELLOW + "Saliendo del programa, vuelva prontos...".center(45))
           break
       else:
           print("Opción inválida.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()