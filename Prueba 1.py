# KILMAR
"""
Libreria utilizada: (mysql.connector)
Nos permite conectar Python con una base de datos que tengamos en MySQL
y almacenar/borrar datos en esa misma
"""
import mysql.connector

"""
Comando de instalacion en la terminal: pip install mysql-connector-python
"""



"""
En este apartado de abajo realizamos lo que es la conexion con nuestra base de datos,
colocamos lo que es nuestro usuario en este caso estamos utilizando root para mayor comodidad
pero logicamente en una aplicacion real se debe utilizar usuarios creados con sus respectivos permisos para evitar
incovenientes debido a que root tiene el rol maximo en cuanto a permisos, luego colocamos lo que es la contraseña del usuario
y el host que en este caso se estaria utilizando el localhost y por ultimo el nombre de la base de datos al cual queremos que obtenga la conexion.
"""
db = mysql.connector.connect(
    user="root",
    password="1234",
    host="localhost",
    database="usuarios"
)


"""
¿Que es el cursor? para entender esto de manera sencilla digamos que es una especie de control remoto en el cual
podemos enviar instrucciones a nuestra base de datos (este caso mysql) para hacer uso del insert, delete, select entre otras funciones relacionadas a las bases de datos
"""
cursor = db.cursor()

# CARLOS
"""
Esta linea de codigo inserta un nuevo registro en la tabla users con el nombre y edad proporcionados por el usuario
mediante el input y luego guarda esos cambios en la base de datos.
"""
def agregar_usuarios():
    nombre = input("Ingresa el nombre a guardar: ")
    edad = int(input("Ingresa la edad de esa persona: "))
    

                             
    sql = "INSERT INTO users (Nombre, Edad) VALUES (%s, %s)" 
    values = (nombre, edad)
    cursor.execute(sql, values)


    db.commit()
    print(cursor.rowcount, "Dato almacenado.")





"""
Esta función elimina un registro de la tabla users en la base de datos.
Primero le pide al usuario que ingrese el ID del usuario que quiere eliminar.
Luego, se genera la consulta (DELETE) que elimina al usuario cuyo ID coincida con el ingresado.
Finalmente, se confirma el cambio con db.commit() y se informa si el usuario fue eliminado o si no se encontró.
"""
def eliminar_usuarios():
    id_usuario = int(input("Ingresa el ID del usuario a eliminar: "))
    

    sql = "DELETE FROM users WHERE Id = %s"
    values = (id_usuario,)
    cursor.execute(sql, values)
 
    db.commit()
    
    """
    Verificamos si el número de filas afectadas por la consulta es mayor a 0.
    Si es así, significa que el usuario fue eliminado, de lo contrario, el ID no existía.
    """
    if cursor.rowcount > 0:
        print("Usuario con ID", id_usuario, "eliminado.")
    else:
        print("No se encontró un usuario con ese ID.")





"""
Esta función muestra todos los usuarios registrados en la tabla `users`.
Primero ejecuta una consulta SELECT para obtener todos los registros de la tabla.
Luego, recorre los resultados y los imprime uno por uno.
Si no hay registros, se notifica al usuario que no hay usuarios registrados.
"""
def mostrar_usuarios():
   
    cursor.execute("SELECT * FROM users")
    resultado = cursor.fetchall()

    """
    Si resultado contiene datos, los mostramos con un bucle.
    En caso contrario, imprimimos un mensaje indicando que no hay usuarios.
    """
    if resultado:
        print("Lista de usuarios:")
        for cliente in resultado:
            print(cliente)
    else:
        print("No hay usuarios registrados.")



# DIEGO
"""
Este codigo presenta un menú interactivo para el usuario.
El menú permite elegir entre agregar, eliminar, mostrar usuarios o salir del programa.
Dependiendo de la opción .elegida, llama a la función correspondiente.
"""
def menu():
    while True:
    
        print("\n--- Menú ---")
        print("1. Agregar usuario")
        print("2. Eliminar usuario")
        print("3. Mostrar todos los usuarios")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        """
        Dependiendo de la opción seleccionada, se llama a la función correspondiente:
        Opción 1: agregar un nuevo usuario
        Opción 2: eliminar un usuario por su ID
        Opción 3: mostrar todos los usuarios
        Opción 4: salir del programa
        """
        if opcion == "1":
            agregar_usuarios()
        elif opcion == "2":
            eliminar_usuarios()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")



# Inicia el programa mostrando el menú
menu()

"""
Al final del programa, cerramos la conexión con la base de datos.
"""
db.close()

