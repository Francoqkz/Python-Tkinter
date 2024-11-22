from email.message import EmailMessage  # Construir la estructura del email
import smtplib  # Conectar con el servidor y enviarlo
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image  # Python Image Library

# Función para enviar correo
def enviar_email():
    remitente = remitente_entry.get().strip()

    # Obtener destinatario según la opción seleccionada
    if destinatario_var.get() == "Otro":
        destinatario_seleccionado = destinatario_manual_entry.get().strip()
    else:
        destinatario_seleccionado = destinatario_var.get().strip()

    asunto_texto = asunto.get().strip()
    mensaje_texto = mensaje.get(1.0, 'end').strip()

    # Validación de campos básicos
    if not remitente or not destinatario_seleccionado or not asunto_texto or not mensaje_texto:
        messagebox.showerror("ERROR", "Todos los campos son obligatorios.")
        return

    # Configuración del servidor
    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    try:
        # Estructura del email
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario_seleccionado
        email["Subject"] = asunto_texto
        email.set_content(mensaje_texto)

        # Envío de email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
            smtp.login(remitente, "znbv bsbp dtzn mnxj") 
            smtp.send_message(email)

        # Guardar copia del correo
        if guardar_copia.get():
            with open("copia_correo.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"Remitente: {remitente}\n")
                archivo.write(f"Destinatario: {destinatario_seleccionado}\n")
                archivo.write(f"Asunto: {asunto_texto}\n")
                archivo.write(f"Mensaje: {mensaje_texto}\n")
                archivo.write("-" * 40 + "\n")

        messagebox.showinfo("MENSAJERÍA", "Mensaje enviado correctamente")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("ERROR", "Error de autenticación. Verifica tu correo y contraseña.")
    except Exception as e:
        messagebox.showerror("ERROR", f"Error al enviar el mensaje: {e}")

# Función para habilitar/deshabilitar campo manual
def habilitar_campo_manual(*args):
    if destinatario_var.get() == "Otro":
        destinatario_manual_entry.config(state="normal")
    else:
        destinatario_manual_entry.delete(0, END)
        destinatario_manual_entry.config(state="disabled")

# Interfaz gráfica
ventana = Tk()
ventana.title("APLICACIÓN DE MENSAJERÍA")
ventana.geometry("400x550")
ventana.resizable(0, 0)
ventana.config(bd=10)

Label(ventana, text="ENVIAR CORREO ", fg="black", font=("Arial", 15, "bold"), padx=5, pady=5).grid(row=0, column=0, columnspan=2)

# Imagen
imagen_gmail = Image.open("C:/Users/Gateway/Pictures/prueba.jpg")
nueva_imagen = imagen_gmail.resize((125, 84))
render = ImageTk.PhotoImage(nueva_imagen)
label_imagen = Label(ventana, image=render)
label_imagen.image = render
label_imagen.grid(row=1, column=0, columnspan=2)

# Variables
destinatario_var = StringVar(ventana)
destinatario_var.set("Otro")  # Valor por defecto

asunto = StringVar(ventana)
guardar_copia = BooleanVar(ventana, value=False)

# Ingresar remitente
Label(ventana, text="Remitente:", fg="black", font=("Arial", 10, "bold")).grid(row=2, column=0)
remitente_entry = Entry(ventana, width=34)
remitente_entry.insert(0, "fp5328642@gmail.com")  # Correo por defecto
remitente_entry.grid(row=2, column=1)

# Selección del destinatario
Label(ventana, text="Selecciona destinatario:", fg="black", font=("Arial", 10, "bold")).grid(row=3, column=0)
OptionMenu(ventana, destinatario_var, "fjcoronati@gmail.com", "programacionsabattini@gmail.com", "francopintos2007@gmail.com", "Otro").grid(row=3, column=1)
destinatario_var.trace("w", habilitar_campo_manual)  # Detectar cambios

# Campo para destinatario manual
Label(ventana, text="Destinatario manual:", fg="black", font=("Arial", 10, "bold")).grid(row=4, column=0)
destinatario_manual_entry = Entry(ventana, width=34, state="disabled")  # Desactivado por defecto
destinatario_manual_entry.grid(row=4, column=1)

Label(ventana, text="Asunto:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=5, column=0)
Entry(ventana, textvariable=asunto, width=34).grid(row=5, column=1)

Label(ventana, text="Mensaje:", fg="black", font=("Arial", 10, "bold"), padx=5, pady=5).grid(row=6, column=0)
mensaje = Text(ventana, height=5, width=28, padx=5, pady=5)
mensaje.grid(row=6, column=1)
mensaje.config(font=("Arial", 9), padx=5, pady=5)

# Casilla de verificación para guardar copia
Checkbutton(ventana, text="Guardar copia del correo", variable=guardar_copia, font=("Arial", 10, "bold")).grid(row=7, column=0, columnspan=2)

# Botón de enviar
Button(ventana, text="ENVIAR", command=enviar_email, height=2, width=10, bg="black", fg="white", font=("Arial", 10, "bold")).grid(row=8, column=0, columnspan=2, padx=5, pady=10)

ventana.mainloop()
