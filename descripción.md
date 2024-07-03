## BlackB FIT

## Descripcion del Proyecto

El proyecto BlackB Fit es una aplicación de consola que permite a los usuarios gestionar rutinas de ejercicios para el gimnasio y tambien brinda ya una rutina para realizar 5 dias a la semana y bajar de peso. La aplicación ofrece funcionalidades para agregar ejercicios, series y repeticiones, como tambien se puede agegar los pesos en Kg para cada ejercicio. Tambien tiene la funcion de mostrar la rutina creada por e; usuario. Se guardaran los datos de cada usuario con persistencia de datos mediante el uso de archivos de texto (json).

El objetivo principal de este proyecto es proporcionar una herramienta sencilla y eficaz para almacenar y consultar las rutinas creadas, facilitando la preferencias de cada persona.

## Público Objetivo

Este proyecto está dirigido para una amplia gama de usuarios interesadas mejorar su salud y forma física. 


## 1. Funcionalidades Básicas

    1- Registro de Usuario - Permite a los nuevos usuarios registrarse proporcionando un nombre de usuario y una contraseña.
    2- Inicio de Sesión - Los usuarios registrados pueden iniciar sesión con su nombre de usuario y contraseña.

### 3. Menú Principal

- Una vez que un usuario ha iniciado sesión, puede acceder a las siguientes opciones:

  - **Rutina por 5 días**: Muestra una rutina predefinida para cinco días, con ejercicios específicos para diferentes grupos musculares.
  - **Crear Rutina Personalizada**: Permite al usuario crear una rutina personalizada especificando los ejercicios, series, repeticiones y peso.
  - **Ver Rutina Personalizada**: Muestra la rutina personalizada creada por el usuario.
  - **Salir**: Cierra el programa.

## Instalación

1. **Clonar el repositorio o descargar los archivos**.

2. **Instalar las dependencias**:

   Este programa utiliza la librería `colorama` para la coloración del texto en la terminal. Puedes instalarla usando `pip`:

   ```bash
   pip install colorama


2. Persistencia de Datos
    - Almacenamiento en Archivos de Texto: Utilizar archivos de texto para guardar y leer los términos y sus definiciones.
    - Formato del Archivo: Cada término y su definición se deben almacenar en un formato
3. Interfaz de Usuario
    - Interfaz de Consola: Proporcionar una interfaz de línea de comandos que permita al usuario interactuar con el glosario.
    - Menú Principal: Ofrecer un menú principal desde el cual el usuario pueda seleccionar las diferentes funcionalidades (Agregar, Buscar, Modificar, Eliminar, Listar).
4.  Validaciones de Datos
    - Entrada de Usuario: Validar la entrada del usuario para asegurar que los términos y definiciones no estén vacíos y que los términos no se repitan.
    - Gestión de Errores: Manejar posibles errores, como intentos de búsqueda o modificación de términos que no existen en el glosario.
5.  Estructura del Código
    - Modularidad: Organizar el código en funciones y, si es necesario, en clases, para mejorar la legibilidad y mantenibilidad.
    - Funciones Principales: Crear funciones específicas para agregar, buscar, modificar, eliminar y listar términos.
    - Manejo de Archivos: Crear funciones para leer y escribir en los archivos de texto.
6.  Documentación
    - Comentarios en el Código: Incluir comentarios en el código para explicar el propósito y funcionamiento de las diferentes partes.
    - Archivo README: Proporcionar un archivo README que describa el propósito del proyecto, cómo ejecutarlo y cómo utilizar las diferentes funcionalidades.