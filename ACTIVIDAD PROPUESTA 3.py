import tkinter as tk 
# Debes escribir un usuario y contraseña
USUARIO = "Pamela_Olivo"
PASSWORD = "09011960"

# Funciones
def capturar_credenciales():
  usuario = input_usuario.get()
  password = input_password.get()

  # El método config admite argumento foreground="" con el cuál podemos especificar el color del texto
  if usuario == USUARIO and password == PASSWORD: 
    mensaje.config(text="Acceso correcto", foreground="green")
  else:
    mensaje.config(text="Usuario o contraseña incorrectos", foreground="red") 
  
  mensaje.pack()

# Ventana principal
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Mi primera app con Tkinter")
icon = tk.PhotoImage(file="pudin.png")
ventana.iconphoto(True, icon)

# Widgets
etiqueta_usuario = tk.Label(ventana, text="Usuario")
etiqueta_usuario.pack()


input_usuario = tk.Entry(ventana)
input_usuario.pack()

etiqueta_password = tk.Label(ventana, text="Password")
etiqueta_password.pack()

input_password = tk.Entry(ventana)
input_password.pack()

mensaje = tk.Label(ventana)

boton = tk.Button(ventana, text="Haz click aquí", command=capturar_credenciales)
boton.pack()


etiqueta_autor = tk.Label(ventana, text="Por: Olkys Pamela Olivo Garrido")
etiqueta_autor.pack()

etiqueta_matricula = tk.Label(ventana, text="Matricula: LR-2024-02080")
etiqueta_matricula.pack()


ventana.mainloop()