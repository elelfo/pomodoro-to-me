"""
Pomodoro Timer Application.

Una aplicación de escritorio que implementa la técnica Pomodoro para mejorar
la productividad mediante ciclos de trabajo y descanso.

Módulos:
    tkinter: Para crear la interfaz gráfica
    messagebox: Para mostrar diálogos de notificación
    winsound: Para reproducir sonidos de alarma
    threading: Para ejecutar el temporizador sin bloquear la interfaz

Ejemplo:
    >>> root = tk.Tk()
    >>> app = PomodoroApp(root)
    >>> root.mainloop()
"""

import tkinter as tk
from tkinter import messagebox
import winsound
import threading


class PomodoroApp:
    """
    Aplicación del Pomodoro Timer con interfaz gráfica.

    Esta clase gestiona la creación y funcionamiento de una aplicación
    Pomodoro interactiva usando Tkinter. Permite configurar tiempos de
    trabajo y descanso, pausar/reanudar sesiones y ajustar tiempos en tiempo real.

    Atributos:
        trabajo (int): Duración de las sesiones de trabajo en minutos (default: 25).
        descanso_corto (int): Duración del descanso corto en minutos (default: 5).
        descanso_largo (int): Duración del descanso largo en minutos (default: 15).
        ciclos_antes_largo (int): Número de ciclos antes del descanso largo (default: 4).
        tiempo_restante (int): Tiempo restante en segundos.
        ejecutando (bool): Indica si el temporizador está activo.
        sesiones_completadas (int): Contador de sesiones completadas.
        modo_sesion (str): Modo actual ('trabajo' o 'descanso').
        config_expandida (bool): Estado de la sección de configuración.

    Métodos públicos:
        crear_interfaz(): Crea todos los elementos visuales de la aplicación.
        iniciar(): Inicia el temporizador.
        pausar(): Pausa el temporizador.
        reset(): Reinicia el temporizador a valores por defecto.
    """
    def __init__(self, root):
        """
        Inicializa la aplicación Pomodoro.

        Args:
            root (tk.Tk): Ventana raíz de Tkinter.
        """
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("550x600")
        self.root.configure(bg="#1a1a1a")
        self.root.resizable(False, False)
        
        # Configuración
        self.trabajo = 25
        self.descanso_corto = 5
        self.descanso_largo = 15
        self.ciclos_antes_largo = 4
        
        # Estado
        self.tiempo_restante = self.trabajo * 60
        self.ejecutando = False
        self.sesiones_completadas = 0
        self.modo_sesion = "trabajo"
        self.config_expandida = False
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """
        Crea la interfaz gráfica de la aplicación.

        Configura todos los elementos visuales incluyendo:
        - Título y mostrador de tiempo
        - Barra de progreso
        - Botones de control (Iniciar, Pausa, Reset)
        - Botones de ajuste de tiempo
        - Sección desplegable de configuración
        - Contador de sesiones
        """
        
        # Título
        titulo = tk.Label(
            self.root,
            text="🍅 POMODORO",
            font=("Arial", 24, "bold"),
            bg="#1a1a1a",
            fg="#ff6b6b"
        )
        titulo.pack(pady=20)
        
        # Mostrador de tiempo
        self.etiqueta_tiempo = tk.Label(
            self.root,
            text="25:00",
            font=("Arial", 80, "bold"),
            bg="#1a1a1a",
            fg="#fff"
        )
        self.etiqueta_tiempo.pack(pady=10)
        
        # Etiqueta de estado
        self.etiqueta_estado = tk.Label(
            self.root,
            text="TRABAJO",
            font=("Arial", 14),
            bg="#1a1a1a",
            fg="#888"
        )
        self.etiqueta_estado.pack(pady=5)
        
        # Barra de progreso
        self.canvas_progreso = tk.Canvas(
            self.root,
            width=350,
            height=10,
            bg="#1a1a1a",
            highlightthickness=0
        )
        self.canvas_progreso.pack(pady=15)
        self.rect_progreso = self.canvas_progreso.create_rectangle(
            0, 0, 0, 10, fill="#ff6b6b", outline="#ff6b6b"
        )
        
        # Frame de botones principales
        frame_botones = tk.Frame(self.root, bg="#1a1a1a")
        frame_botones.pack(pady=15)
        
        self.boton_inicio = tk.Button(
            frame_botones,
            text="▶ Iniciar",
            font=("Arial", 11, "bold"),
            bg="#ff6b6b",
            fg="#fff",
            border=0,
            padx=18,
            pady=8,
            command=self.iniciar,
            cursor="hand2"
        )
        self.boton_inicio.grid(row=0, column=0, padx=5)
        
        self.boton_pausa = tk.Button(
            frame_botones,
            text="⏸ Pausa",
            font=("Arial", 11, "bold"),
            bg="#4ecdc4",
            fg="#fff",
            border=0,
            padx=18,
            pady=8,
            command=self.pausar,
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.boton_pausa.grid(row=0, column=1, padx=5)
        
        self.boton_reset = tk.Button(
            frame_botones,
            text="🔄 Reset",
            font=("Arial", 11, "bold"),
            bg="#888",
            fg="#fff",
            border=0,
            padx=18,
            pady=8,
            command=self.reset,
            cursor="hand2"
        )
        self.boton_reset.grid(row=0, column=2, padx=5)
        
        # Frame de ajuste de tiempo
        frame_tiempo = tk.Frame(self.root, bg="#1a1a1a")
        frame_tiempo.pack(pady=10)
        
        tk.Label(
            frame_tiempo,
            text="Ajustar tiempo:",
            font=("Arial", 9),
            bg="#1a1a1a",
            fg="#888"
        ).grid(row=0, column=0, columnspan=4, pady=(0, 8))
        
        tk.Button(
            frame_tiempo,
            text="➖ -1 min",
            font=("Arial", 10, "bold"),
            bg="#555",
            fg="#fff",
            border=0,
            padx=10,
            pady=6,
            command=self.restar_minuto,
            cursor="hand2"
        ).grid(row=1, column=0, padx=3)
        
        tk.Button(
            frame_tiempo,
            text="➖ -5 min",
            font=("Arial", 10, "bold"),
            bg="#555",
            fg="#fff",
            border=0,
            padx=10,
            pady=6,
            command=self.restar_cinco_min,
            cursor="hand2"
        ).grid(row=1, column=1, padx=3)
        
        tk.Button(
            frame_tiempo,
            text="➕ +1 min",
            font=("Arial", 10, "bold"),
            bg="#555",
            fg="#fff",
            border=0,
            padx=10,
            pady=6,
            command=self.sumar_minuto,
            cursor="hand2"
        ).grid(row=1, column=2, padx=3)
        
        tk.Button(
            frame_tiempo,
            text="➕ +5 min",
            font=("Arial", 10, "bold"),
            bg="#555",
            fg="#fff",
            border=0,
            padx=10,
            pady=6,
            command=self.sumar_cinco_min,
            cursor="hand2"
        ).grid(row=1, column=3, padx=3)
        
        # Sesiones
        self.etiqueta_sesiones = tk.Label(
            self.root,
            text="Sesiones: 0",
            font=("Arial", 10),
            bg="#1a1a1a",
            fg="#888"
        )
        self.etiqueta_sesiones.pack(pady=8)
        
        # Frame de configuración desplegable
        frame_config = tk.Frame(self.root, bg="#1a1a1a")
        frame_config.pack(pady=10, padx=20, fill=tk.X)
        
        # Header desplegable
        frame_header = tk.Frame(frame_config, bg="#1a1a1a", cursor="hand2")
        frame_header.pack(fill=tk.X)
        frame_header.bind("<Button-1>", lambda e: self.toggle_config())
        
        self.triangulo = tk.Label(
            frame_header,
            text="▶",
            font=("Arial", 10, "bold"),
            bg="#1a1a1a",
            fg="#888",
            cursor="hand2"
        )
        self.triangulo.pack(side=tk.LEFT, padx=(0, 10))
        self.triangulo.bind("<Button-1>", lambda e: self.toggle_config())
        
        titulo_config = tk.Label(
            frame_header,
            text="⚙️ Configuración",
            font=("Arial", 10, "bold"),
            bg="#1a1a1a",
            fg="#888",
            cursor="hand2"
        )
        titulo_config.pack(side=tk.LEFT)
        titulo_config.bind("<Button-1>", lambda e: self.toggle_config())
        
        # Frame de opciones (oculto inicialmente)
        self.frame_opciones = tk.Frame(frame_config, bg="#1a1a1a")
        
        # Trabajo
        frame_trabajo = tk.Frame(self.frame_opciones, bg="#1a1a1a")
        frame_trabajo.pack(fill=tk.X, pady=5)
        tk.Label(frame_trabajo, text="Trabajo:", font=("Arial", 9), bg="#1a1a1a", fg="#fff").pack(side=tk.LEFT, padx=(0, 20))
        self.entrada_trabajo = tk.Entry(frame_trabajo, font=("Arial", 9), width=5, bg="#333", fg="#fff", border=1)
        self.entrada_trabajo.insert(0, "25")
        self.entrada_trabajo.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(frame_trabajo, text="min", font=("Arial", 9), bg="#1a1a1a", fg="#888").pack(side=tk.LEFT)
        
        # Descanso corto
        frame_corto = tk.Frame(self.frame_opciones, bg="#1a1a1a")
        frame_corto.pack(fill=tk.X, pady=5)
        tk.Label(frame_corto, text="Descanso corto:", font=("Arial", 9), bg="#1a1a1a", fg="#fff").pack(side=tk.LEFT, padx=(0, 10))
        self.entrada_corto = tk.Entry(frame_corto, font=("Arial", 9), width=5, bg="#333", fg="#fff", border=1)
        self.entrada_corto.insert(0, "5")
        self.entrada_corto.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(frame_corto, text="min", font=("Arial", 9), bg="#1a1a1a", fg="#888").pack(side=tk.LEFT)
        
        # Descanso largo
        frame_largo = tk.Frame(self.frame_opciones, bg="#1a1a1a")
        frame_largo.pack(fill=tk.X, pady=5)
        tk.Label(frame_largo, text="Descanso largo:", font=("Arial", 9), bg="#1a1a1a", fg="#fff").pack(side=tk.LEFT, padx=(0, 10))
        self.entrada_largo = tk.Entry(frame_largo, font=("Arial", 9), width=5, bg="#333", fg="#fff", border=1)
        self.entrada_largo.insert(0, "15")
        self.entrada_largo.pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(frame_largo, text="min", font=("Arial", 9), bg="#1a1a1a", fg="#888").pack(side=tk.LEFT)
        
        # Botón guardar
        tk.Button(
            self.frame_opciones,
            text="💾 Guardar configuración",
            font=("Arial", 9, "bold"),
            bg="#4ecdc4",
            fg="#fff",
            border=0,
            padx=15,
            pady=7,
            command=self.guardar_config,
            cursor="hand2"
        ).pack(pady=(10, 0))
    
    def actualizar_pantalla(self):
        """
        Actualiza la pantalla con el tiempo actual y progreso.

        Recalcula el tiempo mostrado, actualiza el color y texto del estado,
        y ajusta la barra de progreso según el tiempo restante.
        """
        minutos = self.tiempo_restante // 60
        segundos = self.tiempo_restante % 60
        self.etiqueta_tiempo.config(text=f"{minutos:02d}:{segundos:02d}")
        
        if self.modo_sesion == "trabajo":
            self.etiqueta_estado.config(text="TRABAJO", fg="#ff6b6b")
            tiempo_total = self.trabajo * 60
        else:
            self.etiqueta_estado.config(text="DESCANSO", fg="#4ecdc4")
            if self.sesiones_completadas % self.ciclos_antes_largo == 0:
                tiempo_total = self.descanso_largo * 60
            else:
                tiempo_total = self.descanso_corto * 60
        
        progreso = (tiempo_total - self.tiempo_restante) / tiempo_total * 350
        self.canvas_progreso.coords(self.rect_progreso, 0, 0, progreso, 10)
        self.etiqueta_sesiones.config(text=f"Sesiones: {self.sesiones_completadas}")
    
    def temporizador_loop(self):
        """
        Ejecuta el loop principal del temporizador.

        Se ejecuta recursivamente cada 1000ms (1 segundo) mientras
        ejecutando sea True. Decrementa el tiempo y actualiza la pantalla.
        Cuando el tiempo llega a 0, llama a tiempo_terminado().
        """
        if self.ejecutando and self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.actualizar_pantalla()
            self.root.after(1000, self.temporizador_loop)
        elif self.ejecutando and self.tiempo_restante == 0:
            self.tiempo_terminado()
    
    def tiempo_terminado(self):
        """
        Se ejecuta cuando el temporizador llega a cero.

        Reproduce un sonido, incrementa el contador de sesiones si es necesario,
        muestra una notificación, cambia entre modo trabajo y descanso, y
        establece el tiempo para la siguiente sesión.
        """
        self.ejecutando = False
        self.reproducir_sonido()
        
        if self.modo_sesion == "trabajo":
            self.sesiones_completadas += 1
            messagebox.showinfo("¡Tiempo!", "¡Sesión de trabajo completada!\n¡A descansar!")
            self.modo_sesion = "descanso"
            
            if self.sesiones_completadas % self.ciclos_antes_largo == 0:
                self.tiempo_restante = self.descanso_largo * 60
            else:
                self.tiempo_restante = self.descanso_corto * 60
        else:
            messagebox.showinfo("¡Tiempo!", "¡Descanso completado!\n¡A trabajar de nuevo!")
            self.modo_sesion = "trabajo"
            self.tiempo_restante = self.trabajo * 60
        
        self.actualizar_pantalla()
        self.boton_inicio.config(state=tk.NORMAL)
        self.boton_pausa.config(state=tk.DISABLED)
    
    def iniciar(self):
        """
        Inicia el temporizador.

        Cambia el estado del temporizador a activo y actualiza los estados
        de los botones. Llama a temporizador_loop() para comenzar el countdown.
        """
        if not self.ejecutando:
            self.ejecutando = True
            self.boton_inicio.config(state=tk.DISABLED)
            self.boton_pausa.config(state=tk.NORMAL)
            self.temporizador_loop()
    
    def pausar(self):
        """
        Pausa el temporizador sin perder el progreso.

        Cambia el estado ejecutando a False y actualiza los estados de los
        botones para permitir reanudar la sesión.
        """
        self.ejecutando = False
        self.boton_inicio.config(state=tk.NORMAL)
        self.boton_pausa.config(state=tk.DISABLED)
    
    def reset(self):
        self.ejecutando = False
        self.tiempo_restante = self.trabajo * 60
        self.modo_sesion = "trabajo"
        self.sesiones_completadas = 0
        self.actualizar_pantalla()
        self.boton_inicio.config(state=tk.NORMAL)
        self.boton_pausa.config(state=tk.DISABLED)
    
    def sumar_minuto(self):
        if not self.ejecutando:
            self.tiempo_restante += 60
            self.actualizar_pantalla()
    
    def sumar_cinco_min(self):
        if not self.ejecutando:
            self.tiempo_restante += 300
            self.actualizar_pantalla()
    
    def restar_minuto(self):
        if not self.ejecutando and self.tiempo_restante > 60:
            self.tiempo_restante -= 60
            self.actualizar_pantalla()
    
    def restar_cinco_min(self):
        if not self.ejecutando and self.tiempo_restante > 300:
            self.tiempo_restante -= 300
            self.actualizar_pantalla()
    
    def toggle_config(self):
        if self.config_expandida:
            self.frame_opciones.pack_forget()
            self.triangulo.config(text="▶")
            self.root.geometry("550x600")
            self.config_expandida = False
        else:
            self.frame_opciones.pack(fill=tk.X, pady=(10, 0))
            self.triangulo.config(text="▼")
            self.root.geometry("550x750")
            self.config_expandida = True
    
    def guardar_config(self):
        try:
            nuevo_trabajo = int(self.entrada_trabajo.get())
            nuevo_corto = int(self.entrada_corto.get())
            nuevo_largo = int(self.entrada_largo.get())
            
            if nuevo_trabajo <= 0 or nuevo_corto <= 0 or nuevo_largo <= 0:
                messagebox.showerror("Error", "Los tiempos deben ser mayores a 0")
                return
            
            self.trabajo = nuevo_trabajo
            self.descanso_corto = nuevo_corto
            self.descanso_largo = nuevo_largo
            
            self.reset()
            messagebox.showinfo("Éxito", "Configuración actualizada")
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos")
    
    def reproducir_sonido(self):
        try:
            winsound.Beep(1000, 500)
        except:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
