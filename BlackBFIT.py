'''
Glosario de Términos de Programación
Autor: Serbluk Sergio
fecha: 2024
version: 1.0
'''
import os 
import colorama # para instalar colorama (pip install colorama)
import time
def limpiarPantalla():
    '''
    funcion para limpiar la pantalla
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    os.system("cls")
    return
def menu():
    '''
    funcion para limpiar la pantalla
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    limpiarPantalla()
    print(colorama.Fore.GREEN + "Glosario de Términos de Programación".center(45))
    print("="*45)
    print(colorama.Fore.BLUE + "\t1" + colorama.Fore.RESET + " para agregar un nuevo término")
    print(colorama.Fore.BLUE + "\t2" + colorama.Fore.RESET + " para modificar un término")
    print(colorama.Fore.BLUE + "\t3" + colorama.Fore.RESET + " para eliminar un término")
    print(colorama.Fore.BLUE + "\t4" + colorama.Fore.RESET + " buscar un término")
    print(colorama.Fore.BLUE + "\t5" + colorama.Fore.RESET + " para listar todos las entradas")
    print(colorama.Fore.BLUE + "\t6" + colorama.Fore.RESET + " para Salir")
    op = int(input(colorama.Fore.CYAN + "seleccione una opción: " + colorama.Fore.RESET ))
    return op
def agregar(lista,termino=""):
    '''
    funcion para limpiar la pantalla
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    if termino=="":
        termino=input("ingrese un termino: ")
        while termino == "":
            print("el termino no puede estar vacio!!")
            termino=input("ingrese un termino: ")
        if termino in [ t[0] for t in lista]:
            print("el termino ya se encuenta en el glosario!")
            input(colorama.Fore.RED + "presione enter para continuar...")
            return
    definicion=input("ingrese la definicion: ")
    while definicion=="":
        print("la definicion no puede estar vacia! ")
        definicion=input("ingrese la definicion: ")
    lista.append((termino,definicion))
    print("el termino se agrego correctamente!")
    print(lista)
    return
def listar(lista):
    '''
    funcion para listar los datos por pantalla
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    limpiarPantalla()
    print("Lista de términos")
    print("="*45)
    for t , d in lista:
        print(f"{t}: {d}")
    print("Fin de la lista.")
    
    return
def buscar(lista):
    '''
    funcion para buscar datos en el glosario y mostrar por pantalla
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    termino=input("ingrese el término a buscar: ")
    for t,d in lista:
        if termino.lower()==t.lower():
            print(f"{t}: {d}")
            input(colorama.Fore.RED + "presione enter para continuar...")
            return
    res=input("término no encontrado en la lisa, lo quiere agreagar s/n: ")
    if res.lower() == "n":
        return
    elif res.lower()=="s":
        agregar(lista,termino)
    return
def eliminar(lista):
    '''
    funcion para eliminar datos de la lista
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    elemento=input("ingrese el término que quiere eliminar: ")
    for t,d in lista:
        if t.lower()==elemento.lower():
            lista.remove((t,d))
            print(f"término eliminado: {elemento}")
            return
    print(f"no se encontro '{elemento}' en la lista de términos! ")
    return
def modificar(lista):
    '''
    funcion para buscar un termino en la lista y luego modificar(reescribir) los datos de la tupla
    Autor: Sergio Serbluk
    fecha: 2024
    version: 1.0
    '''
    termino=input("ingrese el termino a modificar: ")
    for i in range(len(lista)):
        if lista[i][0]==termino:
            print(f"ternimo: {lista[i][0]}\n \t descripcion: {lista[i][1]}")
            definicion=input("ingrese la nueva definicion: ")
            while definicion == "":
                print("la definicion no puede estar vacia!")
                definicion=input("ingrese la nueva definicion: ")
            lista[i]=(termino, definicion)
            print("los datos se modificaron correctamente!")
            return
    print("el elemento no de encontro en la lista!")
    return
    return

#programa principal
colorama.init() #inicializamos colorama para poder usarlo
terminos=[]
op = menu()
while op !=6:
    match op:
        case 1:
            print("agregar")
            agregar(terminos)
            time.sleep(5)
            #input(colorama.Fore.RED + "presione enter para continuar...")
        case 2:
            print("modificar")
            modificar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 3:
            print("eliminar")
            eliminar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 4:
            print("buscar")
            buscar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case 5:
            print("listar todos")
            listar(terminos)
            input(colorama.Fore.RED + "presione enter para continuar...")
        case _:
            print("error!")
            input(colorama.Fore.RED + "presione enter para continuar...")
    op = menu()