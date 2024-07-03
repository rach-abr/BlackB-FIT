class Persona:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, fecha_ingreso):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso


class Ejercicio:
    def __init__(self, nombre, repeticiones, series, peso_kg):
        self.nombre = nombre
        self.repeticiones = repeticiones
        self.series = series
        self.peso_kg = peso_kg


class Gimnasio:
    def __init__(self):
        self.personas = []
        self.rutinas = {}

    def agregar_persona(self):
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        dni = input("Ingrese el DNI de la persona: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento de la persona (YYYY-MM-DD): ")
        fecha_ingreso = input("Ingrese la fecha de ingreso al gimnasio (YYYY-MM-DD): ")

        persona = Persona(nombre, apellido, dni, fecha_nacimiento, fecha_ingreso)
        self.personas.append(persona)
        print(f"Persona {nombre} {apellido} agregada exitosamente.")

    def buscar_persona_por_apellido(self, apellido):
        for persona in self.personas:
            if persona.apellido == apellido:
                return persona
        return None

    def agregar_ejercicio(self, apellido, nombre_ejercicio, repeticiones, series, peso_kg):
        persona = self.buscar_persona_por_apellido(apellido)
        if persona:
            if apellido in self.rutinas:
                self.rutinas[apellido].append(Ejercicio(nombre_ejercicio, repeticiones, series, peso_kg))
            else:
                self.rutinas[apellido] = [Ejercicio(nombre_ejercicio, repeticiones, series, peso_kg)]
            print(f"Ejercicio '{nombre_ejercicio}' agregado para {apellido} con {repeticiones} repeticiones, {series} series y {peso_kg} KG.")
        else:
            print(f"No se encontró la persona con apellido '{apellido}'. No se pudo agregar el ejercicio.")

    def eliminar_ejercicio(self, apellido, nombre_ejercicio):
        if apellido in self.rutinas:
            for ejercicio in self.rutinas[apellido]:
                if ejercicio.nombre == nombre_ejercicio:
                    self.rutinas[apellido].remove(ejercicio)
                    print(f"Ejercicio '{nombre_ejercicio}' eliminado para {apellido}.")
                    return
        print(f"No se encontró el ejercicio '{nombre_ejercicio}' para {apellido}.")

    def modificar_ejercicio(self, apellido, ejercicio_viejo, ejercicio_nuevo, repeticiones, series, peso_kg):
        if apellido in self.rutinas:
            for ejercicio in self.rutinas[apellido]:
                if ejercicio.nombre == ejercicio_viejo:
                    ejercicio.nombre = ejercicio_nuevo
                    ejercicio.repeticiones = repeticiones
                    ejercicio.series = series
                    ejercicio.peso_kg = peso_kg
                    print(f"Ejercicio '{ejercicio_viejo}' modificado a '{ejercicio_nuevo}' para {apellido} con {repeticiones} repeticiones, {series} series y {peso_kg} KG.")
                    return
        print(f"No se encontró el ejercicio '{ejercicio_viejo}' para {apellido}.")

    def ver_ejercicios(self, apellido):
        if apellido in self.rutinas:
            print(f"\n--- Ejercicios Agregados para {apellido} ---")
            for ejercicio in self.rutinas[apellido]:
                print(f"- {ejercicio.nombre}: {ejercicio.repeticiones} repeticiones, {ejercicio.series} series, {ejercicio.peso_kg} KG")
        else:
            print(f"No se encontraron ejercicios agregados para {apellido}.")


def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar persona")
    print("2. Buscar persona por apellido")
    print("3. Agregar ejercicio a una persona")
    print("4. Eliminar ejercicio de una persona")
    print("5. Modificar ejercicio de una persona")
    print("6. Ver ejercicios agregados de una persona")
    print("7. Salir")


def main():
    gimnasio = Gimnasio()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gimnasio.agregar_persona()
        elif opcion == "2":
            apellido_buscar = input("Ingrese el apellido para buscar personas: ")
            persona_encontrada = gimnasio.buscar_persona_por_apellido(apellido_buscar)
            if persona_encontrada:
                print(f"Persona encontrada: {persona_encontrada.nombre} {persona_encontrada.apellido}")
            else:
                print(f"No se encontró ninguna persona con el apellido '{apellido_buscar}'.")
        elif opcion == "3":
            apellido = input("Ingrese el apellido de la persona: ")
            nombre_ejercicio = input("Ingrese el nombre del ejercicio: ")
            repeticiones = int(input("Ingrese el número de repeticiones: "))
            series = int(input("Ingrese el número de series: "))
            peso_kg = float(input("Ingrese el peso en kilogramos (KG): "))
            gimnasio.agregar_ejercicio(apellido, nombre_ejercicio, repeticiones, series, peso_kg)
        elif opcion == "4":
            apellido = input("Ingrese el apellido de la persona: ")
            nombre_ejercicio = input("Ingrese el nombre del ejercicio a eliminar: ")
            gimnasio.eliminar_ejercicio(apellido, nombre_ejercicio)
        elif opcion == "5":
            apellido = input("Ingrese el apellido de la persona: ")
            ejercicio_viejo = input("Ingrese el nombre del ejercicio a modificar: ")
            ejercicio_nuevo = input("Ingrese el nuevo nombre del ejercicio: ")
            repeticiones = int(input("Ingrese el número de repeticiones: "))
            series = int(input("Ingrese el número de series: "))
            peso_kg = float(input("Ingrese el peso en kilogramos (KG): "))
            gimnasio.modificar_ejercicio(apellido, ejercicio_viejo, ejercicio_nuevo, repeticiones, series, peso_kg)
        elif opcion == "6":
            apellido = input("Ingrese el apellido de la persona para ver sus ejercicios: ")
            gimnasio.ver_ejercicios(apellido)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")


if __name__ == "__main__":
    main()
    