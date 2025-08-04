import tkinter as tk
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop
from PIL import Image, ImageTk

#lista de usuario
usuarios = {"gabriel": "1234"}

#lista de preguntas
preguntas = [
    {
        "pregunta": '¿Qué significa "Chamo"?',
        "opciones": ["Abuelo", "Joven o niño", "Perro callejero", "Tipo de comida"],
        "correcta": "b"
    },
    {
        "pregunta": '¿"¡Épale!" se usa para: ?',
        "opciones": ["Saludar o expresar sorpresa", "Pedir dinero", "Insultar a alguien", "Llamar a un gato"],
        "correcta": "a"
    },
    {
        "pregunta": 'Si alguien te dice "Está arrecho", puede significar:',
        "opciones": ["Está feliz", "Está enojado o es difícil", "Está dormido", "Está perdido"],
        "correcta": "b"
    },
    {
        "pregunta": '¿"Pana" es sinónimo de: ?',
        "opciones": ["Camisa", "Amigo", "Comida rápida", "Autobús"],
        "correcta": "b"
    },
    {
        "pregunta": '¿Qué es un "catire"?',
        "opciones": ["Un animal salvaje", "Una persona rubia o de piel clara", "Un tipo de árbol", "Un plato típico"],
        "correcta": "b"
    },
    {
        "pregunta": '"Autobús" significa:',
        "opciones": ['"Camionetica"', '"Buseta"', '"Transporte público"', '"Combi"'],
        "correcta": "a"
    },
    {
        "pregunta": 'Si te ofrecen un "cambur", ¿qué es?',
        "opciones": ["Un refresco", "Un plátano o banano", "Un dulce de leche", "Un tipo de pan"],
        "correcta": "b"
    },
    {
        "pregunta": '¿"Vergación" se usa para expresar: ?',
        "opciones": ["Alegría", "Asombro o frustración", "Hambre", "Sueño"],
        "correcta": "b"
    },
    {
        "pregunta": '¿Qué significa "jalar"?',
        "opciones": ["Dormir profundamente", "Irse o marcharse", "Comer mucho", "Bailar"],
        "correcta": "b"
    },
    {
        "pregunta": '¿"Chévere" es sinónimo de: ?',
        "opciones": ["Aburrido", "Genial o cool", "Caro", "Pequeño"],
        "correcta": "b"
    },
    {
        "pregunta": '¿"Un pelo\'e loco" es: ?',
        "opciones": ["Un peinado extravagante", "Alguien un poco alocado", "Un tipo de insecto", "Un postre"],
        "correcta": "a"
    },
    {
        "pregunta": '¿Qué es una "yuca"?',
        "opciones": ["Un tubérculo similar a la papa", "Un animal parecido a un conejo", "Un objeto para cocinar", "Un insulto"],
        "correcta": "a"
    },
    {
        "pregunta": '"Echar un palo" significa:',
        "opciones": ["Ayudar o hacer un favor", "Golpear a alguien", "Plantar un árbol", "Comprar algo"],
        "correcta": "a"
    },
    {
        "pregunta": '¿"Churupos" son: ?',
        "opciones": ["Dinero (de manera informal)", "Zapatos deportivos", "Juguetes antiguos", "Dulces típicos"],
        "correcta": "a"
    },
    {
        "pregunta": '"Marico" en contexto amistoso se usa para:',
        "opciones": ["Llamar a un amigo (sin ofender)", "Insultar gravemente", "Nombrar un pájaro", "Pedir comida"],
        "correcta": "a"
    },
    {
        "pregunta": '¿"¡Qué vaina!" expresa: ?',
        "opciones": ["Frustración o sorpresa", "Alegría desbordada", "Hambre", "Que algo es caro"],
        "correcta": "a"
    },
    {
        "pregunta": '"Pavo" se refiere a:',
        "opciones": ["Un animal de granja", "Algo aburrido o mediocre", "Un tipo de música", "Un postre"],
        "correcta": "b"
    },
    {
        "pregunta": '"Mamar gallo" es:',
        "opciones": ["Bromear o hacer chistes", "Beber alcohol", "Cuidar animales", "Dormir en el día"],
        "correcta": "a"
    },
    {
        "pregunta": '"Burda" significa:',
        "opciones": ["Mucho o demasiado", "Poco", "Rápido", "Desordenado"],
        "correcta": "a"
    },
    {
        "pregunta": '"Fiesta" significa:',
        "opciones": ["Parranda", "Joda", "Rumba", "Guaquete"],
        "correcta": "c"
    }
]

#trivia completa
class Venezolario_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x700")
        self.root.title("VenezolarioLite")
        self.usuario = None
        self.centrar_ventana(400,700)


        fondo = "#34B4BA"

        #parte del frmae
        self.frame_superior = Frame(self.root)
        self.frame_superior.configure(bg=fondo)
        self.frame_superior.pack(fill="both", expand = True)

        self.frame_inferior = Frame(self.root)
        self.frame_inferior.configure(bg=fondo)
        self.frame_inferior.pack(fill="both", expand = True)

        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)

        #parte de titulo
        self.titulo = Label(self.frame_superior, text = "¡Bienvenido!", font= ("Calisto MT", 36, "bold"), bg = fondo)
        self.titulo.pack(side = "top", pady = 20)

        self.descripcion = Label(self.frame_superior, text = "Por favor coloque el usuario y la contraseña para acceder al juego", font= ("Calisto MT", 10, "bold"), bg = fondo)
        self.descripcion.pack(pady = 0)

        #parte de la imagen
        self.img = Image.open("img/usuario.png")
        self.img = self.img.resize((250,265))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image = self.render, bg = fondo)
        self.fondo.pack(expand = True, fill = "both", side = "top")

        #parte de los datos
        self.label_usuario = Label(self.frame_inferior, text = "Usuario:", font = ("Arial", 18), bg = fondo, fg = "black")
        self.label_usuario.grid(row = 0, column = 0, padx = 10, sticky="e")

        self.entrada_usuario = Entry(self.frame_inferior, bd = 0, width = 14, font = ("Arial", 18))
        self.entrada_usuario.grid(row = 0, column = 1, columnspan = 3, padx = 5, sticky="w")

        self.label_contraseña = Label(self.frame_inferior, text = "Contraseña:", font = ("Arial", 18), bg = fondo, fg = "black")
        self.label_contraseña.grid(row = 1, column = 0, padx = 10, sticky="e")

        self.entrada_contraseña = Entry(self.frame_inferior, bd = 0, width = 14, font = ("Arial", 18), show = "*")
        self.entrada_contraseña.grid(row = 1, column = 1, columnspan = 3, padx = 5, sticky="w")

        self.boton_ingresar = Button(self.frame_inferior, text ="Ingresar", width=16, font=("Arial", 12), command = self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=35)

    #funcion para entrar
    def entrar(self):
        nombre = self.entrada_usuario.get()
        clave = self.entrada_contraseña.get()

        if nombre in usuarios and usuarios[nombre] == clave:
            self.usuario = nombre
            messagebox.showinfo("Login exitoso", f"¡Bienvenido {self.usuario}!")
            self.limpiar_ventana()
            self.mostrar_menu()
        else:
            messagebox.showerror("Error", "Usuario contraseña incorrecta, por favor verfique los datos")

    #funcion para limpiar la ventana
    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    #menu
    def mostrar_menu(self):
        self.limpiar_ventana()
        fondo = "#34B4BA"
        self.root.geometry("400x700")
        self.root.configure(bg = fondo)
        

        #titulo del menu
        titulo_menu = Label(self.root, text = "VenezolarioLite", font=("Calisto MT",24, "bold"), bg = fondo, fg="black")
        titulo_menu.pack(pady=30)

        #imagen del venezolario
        self.img = Image.open("img/logo.png")
        self.img = self.img.resize((250,265))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.root, image = self.render, bg = fondo)
        self.fondo.pack(expand = True, fill = "both", side="top")

        #botones del menu
        boton_jugar = Button(self.root, text="Comenzar a Jugar", font=("Arial", 14), width=20, command=self.comenzar_a_jugar)
        boton_jugar.pack(pady=10)

        boton_instrucciones = Button(self.root, text="Instrucciones", font=("Arial", 14), width=20, command=self.mostrar_instrucciones)
        boton_instrucciones.pack(pady=10)

        boton_creditos = Button(self.root, text="Créditos", font=("Arial", 14), width=20, command=self.mostrar_creditos)
        boton_creditos.pack(pady=10)

        boton_salir = Button(self.root, text="Salir", font=("Arial", 14), width=20, command=self.root.quit)
        boton_salir.pack(pady=10)

        
    #funciones de los botones
    
    #funcion para comenzar a jugar
    def comenzar_a_jugar(self):
        self.puntaje = 0
        self.indice_pregunta = 0
        self.respuesta_var = tk.StringVar(value="")
        self.respuesta_var.set("")
        self.mostrar_pregunta()

    #mostar las preguntas
    def mostrar_pregunta(self):
        self.limpiar_ventana()
        self.root.geometry("600x400")

        fondo = "#34B4BA"
        self.root.configure(bg=fondo)
        

        if self.indice_pregunta < len(preguntas):
            pregunta_actual = preguntas[self.indice_pregunta]

            letras = ['a', 'b', 'c', 'd']

            # Mostrar la pregunta
            lbl_pregunta = tk.Label(self.root, text=pregunta_actual["pregunta"], 
            font=("Arial", 16, "bold"), bg=fondo, fg="black", wraplength=550)
            lbl_pregunta.pack(pady=20)

            # Resetear variable para las opciones
            self.respuesta_var.set("")

            # Mostrar las opciones como radiobuttons
            for i, opcion in enumerate(pregunta_actual["opciones"]):
                rb = tk.Radiobutton(
                    self.root,
                    text=f"{letras[i]}) {opcion}",
                    variable=self.respuesta_var,
                    value=letras[i],
                    font=("Arial", 14),
                    bg=fondo,
                    fg="black",
                    selectcolor="#E8F7F8",
                    anchor="w",
                    justify="left",
                    wraplength=500
                )
                rb.pack(fill="x", padx=40, pady=3)

            boton_responder = tk.Button(self.root, text="Responder", font=("Arial", 14), command=self.verificar_respuesta)
            boton_responder.pack(pady=20)
        else:
            self.mostrar_resultados()

    def verificar_respuesta(self):
        seleccion = self.respuesta_var.get()
        if not seleccion :
            messagebox.showwarning("Atención", "Por favor, selecciona una opción.")
            return

        correcta = preguntas[self.indice_pregunta]["correcta"]

        if seleccion == correcta:
            self.puntaje += 1

        self.indice_pregunta += 1
        self.mostrar_pregunta()

    def mostrar_resultados(self):
        self.limpiar_ventana()
        self.root.geometry("600x400")
        fondo = "#34B4BA"
        self.root.configure(bg=fondo)

        tk.Label(self.root, text="¡Trivia finalizada!", font=("Arial", 22, "bold"), bg=fondo, fg="white").pack(pady=20)
        tk.Label(self.root, text=f"Puntaje final: {self.puntaje} de {len(preguntas)}", font=("Arial", 18), bg=fondo, fg="white").pack(pady=12)

        # Mensaje según puntaje
        if self.puntaje == len(preguntas):
            mensaje = "¡Eres un venezolano auténtico! ¡Nivel maestro!"
        elif self.puntaje >= len(preguntas) * 0.7:
            mensaje = "¡Muy bien! Tienes buen dominio del venezolano."
        elif self.puntaje >= len(preguntas) * 0.4:
            mensaje = "¡No está mal, puedes mejorar!"
        else:
            mensaje = "¡Te falta práctica, inténtalo otra vez!"

        tk.Label(self.root, text=mensaje, font=("Arial", 14), bg=fondo, fg="white").pack(pady=15)

        btn_volver_menu = tk.Button(self.root, text="Volver al menú", font=("Arial", 14), command=self.mostrar_menu)
        btn_volver_menu.pack(pady=10)
        

    def mostrar_instrucciones(self):
        instrucciones = (
            "Instrucciones del Venezolario:\n\n"
            "1. Selecciona la opción correcta para cada palabra.\n"
            "2. Contesta todas las preguntas.\n"
            "3. Al final se mostrará tu puntaje.\n"
            "¡Diviértete!"
        )
        messagebox.showinfo("Instrucciones", instrucciones)

    def mostrar_creditos(self):
        creditos = (
            "Créditos del VenezolarioLite:\n\n"
            "Creado por: Gabriel Rivero\n"
            "Proyecto 2025\n"
        )
        messagebox.showinfo("Créditos", creditos)

    #para centrar la ventana    
    def centrar_ventana(self, ancho, alto):
        # Calcula coordenadas para centrar ventana
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (ancho // 2)
        y = (screen_height // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Venezolario_app(root)
    root.mainloop()