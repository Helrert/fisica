import tkinter as tk # ejecutar "sudo apt-get install python3-tk" si hay problemas con la importac
from tkinter import ttk
import numpy as np
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as mpl
from matplotlib import collections  as mc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

class Interface:
    def __init__(self):
        # Valores Iniciales
        self.gravedad = 9.8
        self.velocidad_iniciacl = 2
        self.angulo = np.radians(45)
        self.x0 = 0
        self.y0 = 0
        self.velocidad_inicial = 10
        self.z0 = 0
        self.window = tk.Tk()
        self.window.title("Fisica")
        self.window.minsize(800, 600)
        self.window.maxsize(1280, 960)
        self.entrada_posicion_x0 = ttk.Entry()
        self.entrada_posicion_y0 = ttk.Entry()
        self.entrada_angulo_inicial = ttk.Entry()
        self.entrada_aceleracion_inicial = ttk.Entry()
        self.deslizador_posicion_x0 = ttk.Scale()
        self.deslizador_posicion_y0 = ttk.Scale()
        self.deslizador_angulo_inicial = ttk.Scale()
        self.deslizador_aceleracion_inicial = ttk.Scale()

        self.pestañas = ttk.Notebook(self.window)
        self.tab_ideal = ttk.Frame(self.pestañas)
        self.opciones = ttk.Frame(self.tab_ideal)
        self.graphics = ttk.LabelFrame(self.tab_ideal, text="Gráfica")

        self.figura = Figure(figsize=(4, 3), dpi=100)  # define la proporcion del gráfico
        self.ecuacion = np.arange(0, 10, .01)
        self.figura.add_subplot(111).plot(self.ecuacion, self.ecuacion * self.ecuacion)
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.graphics)
        self.canvas.draw()
        self.canvas = self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


        # Inicializar los botones de la interfaz
        self.boton_posicion = ttk.Button(self.opciones, text="Posición", width=10, command=lambda: self.boton_posicionf())
        self.boton_velocidad = ttk.Button(self.opciones, text="Velocidad", width=10, command=lambda: self.boton_velocidadf())
        self.boton_aceleracion = ttk.Button(self.opciones, text="Aceleración", width=10, command=lambda: self.boton_aceleracionf())
        self.boton_alcance_horizontal = ttk.Button(self.opciones, text="Alcance Horizontal", width=10, command=lambda: self.boton_alcance_horizontalf())
        self.boton_altura_maxima = ttk.Button(self.opciones, text="Altura Màxima", width=10, command=lambda: self.boton_altura_maximaf())
        self.boton_camino_recorrido = ttk.Button(self.opciones, text="Camino Recorrido", width=10, command=lambda: self.boton_camino_recorridof())
        self.boton_radio_y_centro_de_curvatura_circulo_obsculador = ttk.Button(self.opciones, text="Radio y Centro de Curvatura y Circulo Obsculador", width=10, command=lambda: self.boton_radio_y_centro_de_curvatura_circulo_obsculadorf)
        self.boton_aceleracion_normal_y_tangencial = ttk.Button(self.opciones, text="A. normal y tangencial", width=10, command=lambda: self.boton_aceleracion_normal_y_tangencialf())
        self.boton_vector_normal = ttk.Button(self.opciones, text="Vector normal", width=10,
                                              command=lambda: self.boton_vector_normalf())
        #self.boton_circulo_osculador = ttk.Button(self.opciones, text="Circulo Osculador", width=10,
                                              #command=lambda: self.boton_circulo_osculadorf())

        self.create_widgets()

    def create_widgets(self):

        def f_posicion_x0(event):
            print(posicion_x0.get())

        def f_posicion_y0(event):
            print(posicion_y0.get())

        def f_angulo_inicial(event):
            print(angulo_inicial.get())

        def f_Rapidez_inicial(event):
            print(Rapidez_inicial.get())

        # Limpia Entry iniciales, de modo que al hacer click estos se vacian
        def limpiar_entrada_x0(event):
            if self.entrada_posicion_x0.get() == "X0":
                self.entrada_posicion_x0.delete(0,'end')

        def update_x0(event):
            # todo ecuacion que se actualiza automatricamente
            input_x0 = self.entrada_posicion_x0.get()
            if input_x0 == '':
                input_x0 = 0
                self.actualizar_grafico(self.ecuacion * float(5),8,8,8)
            self.actualizar_grafico(self.ecuacion * float(5),8,8,8)

        def limpiar_entrada_y0(event):
            if self.entrada_posicion_y0.get() == "Y0":
                self.entrada_posicion_y0.delete(0,'end')

        def limpiar_entrada_angulo(event):
            if self.entrada_angulo_inicial.get() == "Angulo":
                self.entrada_angulo_inicial.delete(0,'end')

        def limpiar_entrada_Rapidez(event):
            if self.entrada_Rapidez_inicial.get() == "Rapidez Inicial":
                self.entrada_Rapidez_inicial.delete(0,'end')




        # Variables de los deslizadores
        posicion_x0 = tk.IntVar()
        posicion_y0 = tk.IntVar()
        angulo_inicial = tk.IntVar()
        Rapidez_inicial = tk.IntVar()
        self.pestañas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, ipadx=10, ipady=10)

        tab_balistica = tk.Frame(self.pestañas)
        tab_seguridad = tk.Frame(self.pestañas)

        self.pestañas.add(self.tab_ideal, text="Movimiento Ideal", compound=tk.TOP)
        self.pestañas.add(tab_seguridad, text="Parabola de Seguridad", compound=tk.TOP)
        self.pestañas.add(tab_balistica, text="Movimiento Balistico", compound=tk.TOP)


        # tutorial = ttk.LabelFrame(self.window, text="Instrucciones")
        # tutorial.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=10, pady=10)

        self.opciones.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=5, pady=5)

        self.boton_posicion.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_velocidad.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_aceleracion.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_alcance_horizontal.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_altura_maxima.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_camino_recorrido.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_radio_y_centro_de_curvatura_circulo_obsculador.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_aceleracion_normal_y_tangencial.pack(side=tk.TOP, padx=10, pady=10)
        self.boton_vector_normal.pack(side=tk.TOP, padx=10, pady=10)
        #self.boton_circulo_osculador.pack(side=tk.TOP, padx=10, pady=10)


        self.graphics.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        separador = ttk.Separator(self.tab_ideal, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)

        variables = ttk.LabelFrame(self.tab_ideal, text="Controles")
        variables.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        # Contenedores de los controles
        posicion = ttk.Frame(variables)
        posicion.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        Rapidez = ttk.Frame(variables)
        Rapidez.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        angulo = ttk.Frame(variables)
        angulo.pack(side=tk.LEFT, expand=True, padx=5, pady=5)


        #todo añadir titulos
        self.entrada_posicion_x0 = ttk.Entry(posicion, justify=tk.CENTER)
        self.entrada_posicion_x0.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_posicion_x0.insert(tk.END, "0")
        self.entrada_posicion_x0.bind("<Button-1>", limpiar_entrada_x0)
        self.entrada_posicion_x0.bind("<Key>", update_x0)

        self.entrada_posicion_y0 = ttk.Entry(posicion, justify=tk.CENTER)
        self.entrada_posicion_y0.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_posicion_y0.insert(tk.END, "0")
        self.entrada_posicion_y0.bind("<Button-1>", limpiar_entrada_y0)

        # todo titulos para rapidez inicial
        self.entrada_Rapidez_inicial = ttk.Entry(Rapidez, justify=tk.CENTER)
        self.entrada_Rapidez_inicial.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_Rapidez_inicial.insert(tk.END, "Rapidez Inicial")
        self.entrada_Rapidez_inicial.bind("<Button-1>", limpiar_entrada_Rapidez)

        # todo titulos para angulo inicial
        self.entrada_angulo_inicial = ttk.Entry(angulo, justify=tk.CENTER)
        self.entrada_angulo_inicial.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entrada_angulo_inicial.insert(tk.END, "Angulo Inicial")
        self.entrada_angulo_inicial.bind("<Button-1>", limpiar_entrada_angulo)


        # Añadir elementos deslizadores para actualizar datos
        self.deslizador_posicion_x0 = ttk.Scale(posicion, variable=posicion_x0,  from_=0, to=100, orient=tk.HORIZONTAL)
        self.deslizador_posicion_x0.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_posicion_x0.set(50)
        self.deslizador_posicion_x0.bind("<B1-Motion>", f_posicion_x0)
        self.deslizador_posicion_x0.bind("<ButtonRelease-1>", f_posicion_x0)

        self.deslizador_posicion_y0 = ttk.Scale(posicion, variable=posicion_y0, from_=0, to=100, orient=tk.HORIZONTAL)
        self.deslizador_posicion_y0.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_posicion_y0.set(50)
        self.deslizador_posicion_y0.bind("<B1-Motion>", f_posicion_y0)
        self.deslizador_posicion_y0.bind("<ButtonRelease-1>", f_posicion_y0)

        self.deslizador_angulo_inicial = ttk.Scale(angulo, variable=angulo_inicial, from_=0, to=90, orient=tk.HORIZONTAL)
        self.deslizador_angulo_inicial.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_angulo_inicial.set(180)
        self.deslizador_angulo_inicial.bind("<B1-Motion>", f_angulo_inicial)

        self.deslizador_Rapidez_inicial = ttk.Scale(Rapidez, variable=Rapidez_inicial, from_=0, to=100, orient=tk.HORIZONTAL)
        self.deslizador_Rapidez_inicial.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.deslizador_Rapidez_inicial.set(50)
        self.deslizador_Rapidez_inicial.bind("<B1-Motion>", f_Rapidez_inicial)
        self.deslizador_Rapidez_inicial.bind("<ButtonRelease-1>", f_Rapidez_inicial)

        #Insercion Grafico en la zona indicada


    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_position_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_angle_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_acceleration_value(self):
        self.entrada_posicion_x0.insert(tk.END, self.entrada_posicion_x0.get())
    # Declaracion de botones0
    def boton_posicionf(self):
        alcanze_horizontal = self.x0 + ((self.velocidad_inicial*sin(2*self.angulo))/(2*self.gravedad)) + \
                             ((self.velocidad_inicial*cos(self.angulo)) /
                              (self.gravedad))*sqrt(((self.velocidad_inicial*sin(self.angulo))**2) + 2*self.y0*self.gravedad)
        x = linspace(0, alcanze_horizontal, 601)

        ecuacion_parametrica_x = (self.x0 + self.velocidad_inicial*cos(self.angulo)*x)
        ecuacion_parametrica_y = (self.y0 + self.velocidad_inicial*sin(self.angulo)*x-(self.gravedad/2)*x**2)
        self.actualizar_grafico(ecuacion_parametrica_x,ecuacion_parametrica_y)
        # Metodo para almacenar datos de las entradas de datos
        def copiar_valores(event):
            self.tiempo_datos[0] = entrada_tiempo.get()

            master.destroy()

        # Metodo para validar la entrada de datos (Solo Numeros por ahora)
        def check(v, p):
            if p.isdigit():
                return True
            elif p is "":
                return True
            else:
                return False
        # Datos Iniciales

        #  inicializa la ventana popup
        master = tk.Tk()
        master.title("Posicion")
        # Crea un frame contenedor para la izquierda y la derecha
        frame_arriba = ttk.Frame(master)
        frame_centro = ttk.Frame(master)
        frame_abajo = ttk.Frame(master)
        frame_aceptar = ttk.Frame(master)
        validacion_tiempo = (frame_abajo.register(check), '%v', '%P')
        #validacion_y = (frame_derecha.register(check), '%v', '%P')

        frame_arriba.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_centro.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_abajo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_aceptar.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Crea las titulos de la entrada de datos
        tiempo = ttk.Label(frame_abajo, text="Tiempo: ")
        aceptar = ttk.Button(frame_aceptar, text="ACEPTAR")
        tiempo_init = ttk.Label(frame_arriba, text="Intervalo de tiempo")
        tiempo_init_x = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init_y = ttk.Entry(frame_arriba, state='readonly')
        tiempo_init.pack(side=tk.TOP)
        tiempo_init_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init_x.configure(state='normal')
        tiempo_init_x.delete(0,'end')
        tiempo_init_x.insert(0,"0")
        tiempo_init_x.configure(state='readonly')
        # inicializa el punto de interseccion del eje Y
        tiempo_init_y.configure(state='normal')
        tiempo_init_y.delete(0, 'end')
        tiempo_init_y.insert(0, "0")
        tiempo_init_y.configure(state='readonly')

        #Separador de datos
        separador = ttk.Separator(frame_centro, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)
        # Crea formularios para entrada de datos
        entrada_tiempo = ttk.Entry(frame_abajo, validate="key", validatecommand=validacion_tiempo)
        #entrada_y = ttk.Entry(frame_derecha, validate="key", validatecommand=validacion_y)

        tiempo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        #posicion_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        entrada_tiempo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
       # entrada_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        aceptar.pack(fill=tk.BOTH, expand=1)
        aceptar.bind("<Button-1>", copiar_valores)

    def boton_velocidadf(self):
        #  inicializa la ventana popup
        master = tk.Tk()
        master.title("Velocidad")
        L1 = tk.Label(Pop_Up, text="Eliga Tiempo a Evaluar")
        E1 = tk.Entry(Pop_Up, bd=5)
        E1.pack()
        L1.pack()
        label = tk.Label(Pop_Up)
        label.pack()

        button = ttk.Button(Pop_Up, text='Evaluar', width=10, command=Pop_Up.destroy)

        button.pack(side=tk.BOTTOM)

        def seno(Grado):
            # funcion para calcualar el seno de un angulo
            # transforma el angulo a radianes para la funcion sin
            return math.sin(math.radians(Grado))

        def coseno(Grado):
            # funcion para calcualar el seno de un angulo
            # transforma el angulo a radianes para la funcion sin
            return math.cos(math.radians(Grado))

        def Ingreso_De_Datos():
            # funcion que recibe y retorna los valores para reemplazar en la ecuacion.
            V_inicial = int(input("Velocidad inicial: "))
            Angulo = int(input("Angulo de inclinación:"))
            Aceleracion = int(input("Aceleracion: "))
            Tiempo = int(input("Tiempo: "))
            # retorn de los datos leidos  por teclado.
            return V_inicial, Angulo, Aceleracion, Tiempo

        def Vector_Velocidad(v0, O, a, t):
            # funcion que calcula el vector velocidad
            # como parametro recibe los valores de velocidad,angulo,aceleracion y tiempo.
            Vt = []
            Vx = v0 * (coseno(O))
            Vy = v0 * (seno(O)) - a * t
            # se añaden la velocidad en X e Y al vector Vt.
            Vt.append(Vx)
            Vt.append(Vy)
            return Vt

        def Grafica_Velocidad(Vt):
            # funcion para graficar el vector velocidad.
            plt.plot(Vt, "r-")
            plt.show()

        def Mostrar_Vector(Vt):
            # muestra el vector velocidad por consola.
            print(Vt[0], ",", Vt[1])

        if __name__ == "__main__":
            V_Inicial, Angulo, Aceleracion, Tiempo = Ingreso_De_Datos()
            Velocidad = Vector_Velocidad(V_Inicial, Angulo, Aceleracion, Tiempo)
            Mostrar_Vector(Velocidad)
            Grafica_Velocidad(Velocidad)


        pass

    def boton_aceleracionf(self):

            #funcion para la obtencion de tiempo impacto final
        def time_impact(self):
            t = ((self.velocidad_inicial*sin(self.angulo))/(2* self.gravedad))+ ((1/self.gravedad)*(sqrt(((self.velocidad_inicial*sin(self.angulo))**2)+(2*self.y0*self.gravedad))))
            print(t)
            return t

            # funcion para el calculo de la coordenada horizontal
        def cord_x(self, t):
            x = self.x0 + ((self.velocidad_inicial * cos(self.angulo)) * t)
            return x

            # funcion para el calculo de la coordenada vertical
        def cord_y(self, t):
            y = self.y0 + (((self.velocidad_inicial * (cos(self.angulo))) * t) - ((self.gravedad / 2) * (t ** 2)))
            return y

            # funcion altura maxima para graficar
        def altura_max(self):
            r = self.y0+ (((self.velocidad_inicial * (sin(self.angulo)))**2)/(2*self.gravedad))
            return r

            # funcion alcance maximo para graficar
        def alcance_max(self):
            alc = self.x0 + ((self.velocidad_inicial*sin(2*self.angulo))/(2*self.gravedad)) + \
                             ((self.velocidad_inicial*cos(self.angulo)) /
                              (self.gravedad))*sqrt(((self.velocidad_inicial*sin(self.angulo))**2) + 2*self.y0*self.gravedad)
            return alc

            # generamiento de la grafica
        def GraficarFuncion(self,entrada_tiempo):

            # generacion de la grafica del tiempo ingresado
            time = np.arange(0, entrada_tiempo, 0.01)
            x = cord_x(self, time)
            y = cord_y(self, time)

            # grafica completa del lanzamiento
            time_complete = np.arange(0, time_impact(self) + 4, 0.01)
            x2 = cord_x(self, time_complete)
            y2 = cord_y(self, time_complete)

            # generacion del punto de posicion a medir
            x3 = cord_x(self, entrada_tiempo)
            y3 = cord_y(self, entrada_tiempo)

            # estetica de la grafica
            mpl.title("Aceleracion")
            mpl.xlim(0, alcance_max(self) + self.x0)
            mpl.ylim(0, altura_max(self) + self.y0)
            mpl.xlabel("-Distancia-")
            mpl.ylabel("-Altura-")

            # generamiento de las curvas
            mpl.plot(self.x0, self.y0, "k-o")  # punto pos inicial
            mpl.plot(x, y, "y-")  # curva del usuario
            mpl.plot(x2, y2, "k--")  # lanzamiento completo
            mpl.plot(x3, y3, "r-o")  # punto del usuario
            mpl.grid()  # cuadriculado

            # generacion del vector con origen en el punto de posicion
            mpl.plot(x3, y3 - time_impact(self), "g-o")

            mpl.show()
            return 0

        # pop up de ingreso de datos
        def copiar_valores(event):
            self.tiempo_datos[0] = entrada_tiempo.get()

            master.destroy()

        # Metodo para validar la entrada de datos (Solo Numeros por ahora)
        def check(v, p):
            if p.isdigit():
                return True
            elif p is "":
                return True
            else:
                return False

        # Datos Iniciales

        #  inicializa la ventana popup
        master = tk.Tk()
        master.title("Posicion")
        # Crea un frame contenedor para la izquierda y la derecha
        frame_arriba = ttk.Frame(master)
        frame_centro = ttk.Frame(master)
        frame_abajo = ttk.Frame(master)
        frame_aceptar = ttk.Frame(master)
        validacion_tiempo = (frame_abajo.register(check), '%v', '%P')
        # validacion_y = (frame_derecha.register(check), '%v', '%P')

        frame_arriba.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_centro.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_abajo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_aceptar.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Crea las titulos de la entrada de datos
        tiempo = ttk.Label(frame_abajo, text="Tiempo: ")
        tiempo_init = ttk.Label(frame_arriba, text="Intervalo de tiempo")
        tiempo_init_x = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init_y = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init.pack(side=tk.TOP)
        tiempo_init_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init_x.configure(state='normal')
        tiempo_init_x.delete(0, 'end')
        tiempo_init_x.insert(0, "0")
        tiempo_init_x.configure(state='readonly')
        # inicializa el punto de interseccion del eje Y
        tiempo_init_y.configure(state='normal')
        tiempo_init_y.delete(0, 'end')
        tiempo_init_y.insert(0, time_impact(self))
        tiempo_init_y.configure(state='readonly')

        # Separador de datos
        separador = ttk.Separator(frame_centro, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)
        # Crea formularios para entrada de datos
        entrada_tiempo = ttk.Entry(frame_abajo, validate="key", validatecommand=validacion_tiempo)
        # entrada_y = ttk.Entry(frame_derecha, validate="key", validatecommand=validacion_y)

        tiempo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # posicion_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        entrada_tiempo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        # entrada_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        aceptar = ttk.Button(frame_aceptar, text="ACEPTAR")
        aceptar.pack(fill=tk.BOTH, expand=1)
        aceptar.bind("<Button-1>", copiar_valores)


        #posible desplazamiento con
        pass

    def boton_alcance_horizontalf(self):
        pass

    def boton_altura_maximaf(self):
        pass
    def boton_camino_recorridof(self):
        pass

    @property
    def boton_radio_y_centro_de_curvatura_circulo_obsculadorf(self):
        def check(v, p):
            if p.isdigit():
                return True
            elif p is "":
                return True
            else:
                return False
        def time_impact(self):
            t = ((self.velocidad_inicial * sin(self.angulo)) / (self.gravedad)) + ((1 / self.gravedad) * (
            sqrt(((self.velocidad_inicial * sin(self.angulo)) ** 2) + (2 * self.y0 * self.gravedad))))
            return round(t,2)
        def validarIntervaloTiempo(valor):
            return (valor>0 &valor<=time_impact(self))
        """def radioButtons():
            print(v.get())
            return v.get()
        """
        def copiarTiempo(event):
            self.tiempo_datos[0] = tiempoUsuarioEntry.get()
            popup.destroy()

        # DATOS DE PRUEBA

        ang=np.pi/3 # REEMPLAZAR POR self.angulo_inicial ?
        g = 10  # Constante
        t = 1   # Este parametro se toma desde la ventana generada
        v0=150  # REEMPLAZAR POR self.velocidad_inicial ?
        x0=10   # ---------^
        y0=20   #
        x=0     # Este parametro se toma desde la ventana generada
        y=0     # ---------^

        ##################
        # ECUACIONES

        curvatura_pos = (np.abs(-g/(np.power(v0*np.cos(ang),2)))/(np.power(1+np.power(np.tan(ang)-g/np.power(v0*np.cos(ang),2)*(x-x0),2),3/2)))
        curvatura_t = (np.abs(-(g)/np.power(v0*np.cos(ang),2))/np.power(1+np.power(np.tan(ang)-(g/v0*np.cos(ang)*t),2),3/2))
        r_curvatura_pos = ((np.power(1+np.power(np.tan(ang)-g/(np.power(v0*np.cos(ang),2)*(x-x0)),2),3/2))/(np.abs(-g/np.power(v0*np.cos(ang),2))))
        r_curvatura_t = ((np.power(1+np.power(np.tan(ang)-g/v0*np.tan(ang)*t,2),3/2))/(np.abs(-g/np.power(v0*np.cos(ang),2))))
        centro_curvatura_x=x-(((np.tan(ang)-(g/np.power(v0*np.cos(ang),2))*(x-x0))*(1+np.power(np.tan(ang)-(g/np.power(v0*np.cos(ang)*(x-x0),2)),2)))/(-g/np.power(v0*np.cos(ang),2)))
        #centro_curvatura_y=
        centro_curvatura_xt= x0+v0*cos(ang)*t + (((1+tan(ang)-(g/v0*cos(ang))*t)*(1+np.power(tan(ang)- (g/v0*cos(ang))*t,2))) / (g/np.power(v0*cos(ang),2)))
        centro_curvatura_yt=y0+v0*sin(ang)*t-(1+np.power(tan(ang)-(g/v0*cos(ang))*t,2)*np.power(v0*cos(ang),2)/g)

        """
        print("Curvatura en tiempo X: "+str(curvatura_t))
        print("Curvatura en posicion: "+str(curvatura_pos))
        print("Radio en posicion: "+str(r_curvatura_pos))
        print("Radio en tiempo X:"+str(r_curvatura_t))
        print("Centro de curvatura pos x:" +str(centro_curvatura_x))
        print("Centro de curvatura X en T1:" + str(centro_curvatura_xt))
        print("Centro de curvatura Y en T1" + str(centro_curvatura_yt))
        """
        ##################

        # Crear POPUP NUEVO #

        popup = tk.Tk()
        popup.title("Radio y centro de curvatura")
        frame_top = ttk.Frame(popup)
        frame_mid = ttk.Frame(popup)
        frame_bot = ttk.Frame(popup)
        frame_top.pack(side=tk.TOP,fill=tk.BOTH,expand=True, padx=5, pady=5)
        frame_mid.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_bot.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        validacion_tiempo = (frame_bot.register(check), '%v', '%P')
        intervaloLabel = ttk.Label(frame_top, text="Intervalo de tiempo").pack(side=tk.TOP,expand=True)
        tiempoInicioEntry = ttk.Entry(frame_top, justify='center')
        tiempoFinalEntry = ttk.Entry(frame_top, justify='center')
        tiempoLabel = ttk.Label(frame_bot, text="Tiempo: ").pack(side=tk.LEFT,fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempoInicioEntry.insert(0,"0")
        tiempoInicioEntry.configure(state='readonly')
        tiempoInicioEntry.pack(side=tk.LEFT,expand=True,padx=5,pady=5)
        tiempoFinalEntry.insert(0,time_impact(self))
        tiempoFinalEntry.configure(state='readonly')
        tiempoFinalEntry.pack(side=tk.LEFT,expand=True,padx=5,pady=5)
        tiempoUsuarioEntry = ttk.Entry(frame_bot,validate="key",validatecommand=validacion_tiempo)
        tiempoUsuarioEntry.pack(side=tk.LEFT,expand=True)
        botonAceptar = ttk.Button(frame_bot,text="Aceptar")
        botonAceptar.pack(side=tk.BOTTOM,expand=1,fill=tk.BOTH)
        botonAceptar.bind("<Button-1>",copiarTiempo)




        """
        ########## RADIO BUTTONS

        v = tk.IntVar()
        radioB1 = tk.Radiobutton(popup, text="Tiempo", variable=v, value=1, command=radioButtons())
        radioB2 = tk.Radiobutton(popup, text="Posicion", variable=v, value=2, command=radioButtons())
        ## PACK RADIOB
        radioB1.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=5 , pady=5)
        radioB2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, padx=5, pady=5)

        #tiempo = ttk.Label(frame_top)
        ########################
        """
        pass

    def boton_aceleracion_normal_y_tangencialf(self):
        # Ecuaciones para el calculo de la aceleracion normal y tangencial

        # Ecuacion aceleracion tangencial
        def a_tangencial(self):
            at = (((((self.velocidad_inicial * (cos(self.angulo)))) ** 2) + (
                    (((self.velocidad_inicial * (sin(self.angulo)))))
                    - self.gravedad * time_impact(self)) ** 2) / (
                          (sqrt(self.velocidad_inicial * cos(self.velocidad_inicial)) ** 2) +
                          (self.velocidad_inicial * sin(self.angulo) - (self.gravedad * time_impact(self)))))
            print(at)
            return at

        # Ecuacion aceleracion normal
        def a_normal(self):
            an = ((((self.velocidad_inicial * sin(self.angulo)) - (self.gravedad * time_impact(self))) / (
                    1 + (tan(self.angulo)
                         - ((self.gravedad) / self.velocidad_inicial * cos(self.angulo) * time_impact(
                        self)))) ** 3)) / abs((self.gravedad) /
                                              (self.velocidad_inicial * cos(self.angulo)) ** 2)
            print(an)
            return an

        # Pop up
        Pop_Up = tk.Tk()
        Pop_Up.title("Tiempo")
        Pop_Up.minsize(400, 300)

    def boton_vector_normalf(self):
        
        velocidad = int(self.entrada_Rapidez_inicial.get())
        angulo_inicial = int(self.entrada_angulo_inicial.get())
        nose=(self.gravedad*int(self.entrada_posicion_y0.get())/math.pow(velocidad,2))
        tiempo_maximov1=(velocidad/self.gravedad)*((math.sin(math.radians(angulo_inicial)))+math.sqrt(math.pow(math.sin(math.radians(angulo_inicial)),2)+2*nose))
        tiempo_maximo=tiempo_maximov1
        print (tiempo_maximov1)
        
        label = tk.Label(Pop_Up)
        label.pack()

        # Crea un cuadro que contiene los datos

        # Organiza los datos
        separador = ttk.Separator(Pop_Up, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)

        # Tiempo Impacto
        def time_impact(self):
            t = ((self.velocidad_inicial * sin(self.angulo)) / (2 * self.gravedad)) + ((1 / self.gravedad) * (
                sqrt(((self.velocidad_inicial * sin(self.angulo)) ** 2) + (2 * self.y0 * self.gravedad))))
            print(t)
            return t

            # Coordenada X

        def cord_x(self, t):
            x = self.x0 + ((self.velocidad_inicial * cos(self.angulo)) * t)
            return x

            # # Coordenada Y

        def cord_y(self, t):
            y = self.y0 + (((self.velocidad_inicial * (cos(self.angulo))) * t) - ((self.gravedad / 2) * (t ** 2)))
            return y

            # Altura máxima gráfica

        def altura_max(self):
            r = self.y0 + (((self.velocidad_inicial * (sin(self.angulo))) ** 2) / (self.gravedad))
            return r

            # Alcance maximo gráfica

        def alcance_max(self):
            alc = self.x0 + ((self.velocidad_inicial * sin(2 * self.angulo)) / (self.gravedad)) + \
                  ((self.velocidad_inicial * cos(self.angulo)) /
                   (self.gravedad)) * sqrt(
                ((self.velocidad_inicial * sin(self.angulo)) ** 2) + 2 * self.y0 * self.gravedad)
            return alc

        time_usuario = 1  # Tiempo ingresado(arreglar)

        # Grafica del tiempo ingresado
        time = np.arange(0, time_usuario, 0.01)
        x = cord_x(self, time)
        y = cord_y(self, time)

        # Grafica completa lanzamiento
        time_complete = np.arange(0, time_impact(self) + 4, 0.01)
        x2 = cord_x(self, time_complete)
        y2 = cord_y(self, time_complete)

        # Punto de posicion a medir
        x3 = cord_x(self, time_usuario)
        y3 = cord_y(self, time_usuario)

        # Detalles gráfica
        mpl.title("Aceleracion normal y tangencial")
        mpl.xlim(0, alcance_max(self) + self.x0)
        mpl.ylim(0, altura_max(self) + self.y0)
        mpl.xlabel("Distancia")
        mpl.ylabel("Altura")

        # Generación curvas
        mpl.plot(self.x0, self.y0, "k-o")  # Posición inicial
        mpl.plot(x, y, "y-")  # Curva
        mpl.plot(x2, y2, "k--")  # Lanzamiento
        # mpl.plot(x3, y3, "r-o")  # Punto ingresado  #Punto rojo de altura maxima
        mpl.grid()  # Cuadriculacion del grafico

        # Generación de las flechas para aceleración normal y tangencial
        # >>>>Genera bien las flechas y texto, pero tira un warning. Falta arreglar<<<<
        ax = mpl.axes()
        ax1 = mpl.axes()
        ax.text(15.4, 10.8, 'an', fontsize=9)  # Texto aceleracion normal
        ax.arrow(x3, y3, 0, -4, head_width=0.5, head_length=1, fc='k', ec='k')  # Flecha de aceleracion normal
        ax.text(18.7, 13.7, 'at', fontsize=9)  # Texto aceleracion tangencial
        ax1.arrow(x3, y3, 5, 0, head_width=0.5, head_length=1, fc='k', ec='k')  # Flecha de aceleracion tangencial

        # Muestra el grafico
        mpl.plot()
        mpl.show()
        pass

    def boton_vector_normalf(self):
        Pop_Up = tk.Tk()
        Pop_Up.title("Rango Tiempo")
        Pop_Up.minsize(400, 300)
        L1 = tk.Label(Pop_Up, text="Eliga Tiempo a Evaluar")
        posicion = ttk.Frame(L1)
        posicion.pack(side=tk.LEFT, expand=True, padx=5, pady=5)
        E1 = ttk.Entry(posicion, justify=tk.CENTER)
        E1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        E1.insert(tk.END, "5")
        L1.pack()
        label = tk.Label(Pop_Up)
        label.pack()
        frame_arriba = ttk.Frame(Pop_Up)
        hola = round(tiempo_maximov1,2)
        strhola= str(hola)
        inter = "Intervalo de tiempo= [0, "
        suma=inter+strhola+"]"

        frame_arriba.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init = ttk.Label(frame_arriba, text=suma)
        tiempo_init.pack(side=tk.TOP)
        tiempo_init_x = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init_x.insert(0, "0")
        button = ttk.Button(Pop_Up, text='Evaluar', width=10, command=Pop_Up.destroy)

        button.pack(side=tk.BOTTOM)



        #  inicializa la ventana popup
        tiempofinal= 20
        xo = int(self.entrada_posicion_x0.get())
        yo = int(self.entrada_posicion_y0.get())
        vxo = 15
        vyo = 90
        angulo_inicial =self.entrada_angulo_inicial.get()
        mpl.title("Vector Normal")
        mpl.xlabel("-X-")
        mpl.ylabel("-Y-")
        x = np.arange(0, tiempofinal, 0.001)
        print(E1.get())
        x1 = 5
        h = math.sin(math.degrees(angulo_inicial))
        j = math.cos(math.degrees(angulo_inicial))
        print (h)
        x1=2
        y = yo + vyo * x + (1 / 2) * -9.8 * x ** 2
        z = xo + vxo * x + (1 / 2) * 0 * x ** 2
        y1 = yo + vyo * x1 + (1 / 2) * -9.8 * x1 ** 2
        z1 = xo + vxo * x1 + (1 / 2) * 0 * x1 ** 2


        vector_velocidadx= (vxo*x1)
        vector_velocidady = (vyo * h-(9.8*x1))
        mpl.plot(z, y,"-")
        mpl.plot(vector_velocidadx+z1, vector_velocidady+y1, "-o")
        mpl.plot((vector_velocidady+z1), (vector_velocidadx), "-o")
        mpl.plot(z1, y1, "-o")
        mpl.show()
        pass
    def actualizar_grafico(self,ecuacion_x,ecuacion_y):
        self.figura.clear() # Refresca el gráfico
        self.figura.add_subplot(111).plot(ecuacion_x,ecuacion_y, "--")
        # self.figura.add_subplot(111).plot(x0, y0, 'r.')
        self.figura.canvas.draw()

    #
    # def actualizar_grafico(self):
    #     self.figura.clear() # Refresca el gráfico
    #     s = np.cos(2)
    #     self.figura.add_subplot(111).plot(self.ecuacion, self.ecuacion)
    #     self.figura.canvas.draw()

    # Lista de almacenado de datos
    tiempo_datos = [0, 0]
