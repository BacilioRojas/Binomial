import tkinter as tk
from tkinter import ttk

class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Valuador de opciones")

        # Crear un widget Notebook
        self.notebook = ttk.Notebook(self)

        # Crear páginas
        self.pagina1 = ttk.Frame(self.notebook)
        self.pagina2 = ttk.Frame(self.notebook)

        # Inicializar las páginas
        self.inicializar_pagina1()
        self.inicializar_pagina2()

        # Añadir las páginas al Notebook
        self.notebook.add(self.pagina1, text="Binomial")
        self.notebook.add(self.pagina2, text="Black and Scholes")

        # Mostrar el Notebook
        self.notebook.pack(expand=1, fill="both")

    def inicializar_pagina1(self):
        
        # Definir la función que se ejecutará cuando se haga clic en el botón
        def enviar_datos():
            pass
        
        # Crear los widgets del formulario
        # Variable de control para el menú desplegable
        vartip = tk.StringVar(self.pagina1)
        vartip.set("Call")


        tk.Label(self.pagina1, text="Tipo de opcion:").grid(row=0, column=0)
        opciones = ["Call","Put"]
        opcion = tk.OptionMenu(self.pagina1,vartip,*opciones)
        opcion.grid(row=0,column=1)

        varclase = tk.StringVar(self.pagina1)
        varclase.set("Americana")

        tk.Label(self.pagina1, text="Clase:").grid(row=1, column=0)
        opciones = ["Americana","Europea"]
        opcion = tk.OptionMenu(self.pagina1,varclase,*opciones)
        opcion.grid(row=1,column=1)

        tk.Label(self.pagina1, text="Precio ").grid(row=2, column=0)

        tk.Label(self.pagina1, text="Subyacente hoy ").grid(row=3, column=0)
        nombre = tk.Entry(self.pagina1)
        nombre.grid(row=3, column=1)
        
        tk.Label(self.pagina1, text="Ejercicio:").grid(row=4, column=0)
        edad = tk.Entry(self.pagina1)
        edad.grid(row=4, column=1)
        
        tk.Label(self.pagina1, text="Tiempo").grid(row=5, column=0)
        email = tk.Entry(self.pagina1)
        email.grid(row=5, column=1)

        varTiempo = tk.StringVar(self.pagina1)
        varTiempo.set("Meses")
        tk.Label(self.pagina1, text="Clase:").grid(row=5, column=2)
        opciones = ["Años","Meses"]
        opcion = tk.OptionMenu(self.pagina1,varTiempo,*opciones)
        opcion.grid(row=5,column=2)
        
        tk.Label(self.pagina1, text="Volatilidad:").grid(row=6, column=0)
        volatilidad = tk.Entry(self.pagina1)
        volatilidad.grid(row=6, column=1)

        tk.Label(self.pagina1, text="Tasa libre de riesgo:").grid(row=7, column=0)
        trl = tk.Entry(self.pagina1)
        trl.grid(row=7, column=1)

        tk.Label(self.pagina1, text="Ramas:").grid(row=8, column=0)
        trl = tk.Entry(self.pagina1)
        trl.grid(row=8, column=1)

        boton_enviar = tk.Button(self.pagina1, text="Enviar", command=enviar_datos)
        boton_enviar.grid(row=9, column=0, columnspan=3)



    def inicializar_pagina2(self):
        # Definir la función que se ejecutará cuando se haga clic en el botón
        def enviar_datos():
            pass
        
        # Crear los widgets del formulario
        # Variable de control para el menú desplegable
        vartip = tk.StringVar(self.pagina1)
        vartip.set("Call")


        tk.Label(self.pagina2, text="Tipo de opcion:").grid(row=0, column=0)
        opciones = ["Call","Put"]
        opcion = tk.OptionMenu(self.pagina2,vartip,*opciones)
        opcion.grid(row=0,column=1)

        varclase = tk.StringVar(self.pagina2)
        varclase.set("Americana")

        tk.Label(self.pagina2, text="Clase:").grid(row=1, column=0)
        opciones = ["Americana","Europea"]
        opcion = tk.OptionMenu(self.pagina2,varclase,*opciones)
        opcion.grid(row=1,column=1)

        tk.Label(self.pagina2, text="Precio ").grid(row=2, column=0)

        tk.Label(self.pagina2, text="Subyacente hoy ").grid(row=3, column=0)
        nombre = tk.Entry(self.pagina2)
        nombre.grid(row=3, column=1)
        
        tk.Label(self.pagina2, text="Ejercicio:").grid(row=4, column=0)
        edad = tk.Entry(self.pagina2)
        edad.grid(row=4, column=1)
        
        tk.Label(self.pagina2, text="Tiempo").grid(row=5, column=0)
        email = tk.Entry(self.pagina2)
        email.grid(row=5, column=1)

        varTiempo = tk.StringVar(self.pagina2)
        varTiempo.set("Meses")
        tk.Label(self.pagina2, text="Clase:").grid(row=5, column=2)
        opciones = ["Años","Meses"]
        opcion = tk.OptionMenu(self.pagina2,varTiempo,*opciones)
        opcion.grid(row=5,column=2)
        
        tk.Label(self.pagina2, text="Volatilidad:").grid(row=6, column=0)
        volatilidad = tk.Entry(self.pagina2)
        volatilidad.grid(row=6, column=1)

        tk.Label(self.pagina2, text="Tasa libre de riesgo:").grid(row=7, column=0)
        trl = tk.Entry(self.pagina2)
        trl.grid(row=7, column=1)

        tk.Label(self.pagina2, text="Ramas:").grid(row=8, column=0)
        trl = tk.Entry(self.pagina2)
        trl.grid(row=8, column=1)

        boton_enviar = tk.Button(self.pagina2, text="Enviar", command=enviar_datos)
        boton_enviar.grid(row=9, column=0, columnspan=3)



if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
