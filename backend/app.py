import smtplib
from email.message import EmailMessage

#datos a tomar de una base de datos
email = "a01625609@tec.mx"
username = "Mayra"
expiration = "2025-07-31"

#plantilla del mensaje
msg = f"""Asunto: Renovación de suscripciones

Hola {username},
Tu suscripción expira el {expiration}. Renuevala para seguir disfrutando de nuestros servicios.

¡Gracias!"""

msg = EmailMessage()
msg['Subject'] = "Renovacion de suscripciones" #asunto
msg['From'] = "mayraeb2012@gmail.com" #remitente
msg['To'] = email #destinatario
msg.set_content(f"""Hola {username},
Tu suscripción expira el {expiration}. Renuevala para seguir disfrutando de nuestros servicios.
¡Gracias!""")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("mayraeb2012@gmail.com", "xpoh mzjn fjml cvqf") #correo y contraseña del remitente (la contraseña se genera en el link de arriba)
    server.send_message(msg) #se envía el mensaje
    #verificar que se envió el correo
    print("Correo enviado")
