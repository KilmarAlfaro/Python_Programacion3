import smtplib

server = "smtp.gmail.com"
puerto = 587
correo = "kilmarbonilla72@gmail.com"
contraseña = "bzxd aiup jhpw rvoh"


# conex puede ser cualquier name 
conex = smtplib.SMTP(server,puerto)

# print(conex.ehlo()) esto sirve para comprobar si hay conexion con el servidor y el puerto

conex.starttls()
conex.login(correo,contraseña)
conex.sendmail(correo,correo,"Subject: Asunto del "+"mensaje\n\n Este es el cuerpo JIHJ")

conex.quit()