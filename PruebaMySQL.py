
import mysql.connector


db = mysql.connector.connect(
    user="root",
    password="1234",
    host="localhost",
    database="users"

)
cursor = db.cursor()

sql = "insert into usuarios (Usuario, Contraseña) values (%s,%s)"

values = (input("Ingrese el nombre de usuario: "),input("Ingrese la contraseña:  "))

cursor.execute(sql, values)
db.commit()


