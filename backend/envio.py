import smtplib
from email.message import EmailMessage

def enviar_correo(destinatario, username='Usuario', expiration='2025-07-31'):
    try:
        # Crear el mensaje
        msg = EmailMessage()
        msg['Subject'] = "Renovación de suscripciones"
        msg['From'] = "mayraeb2012@gmail.com"         # remitente
        msg['To'] = destinatario                      # destinatario dinámico
        msg.set_content(f"""Hola {username},
Tu suscripción expira el {expiration}. Renuevala para seguir disfrutando de nuestros servicios.
¡Gracias!""")

        # Enviar el correo
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("mayraeb2012@gmail.com", "xpoh mzjn fjml cvqf")  # usa tu contraseña de aplicación
            server.send_message(msg)

        print("Correo enviado a", destinatario)
        return True

    except Exception as e:
        print("Error al enviar correo:", e)
        return False
