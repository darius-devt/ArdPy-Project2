# # ======================
# # # IMPORTAR FICHEROS
# # ======================
# import fixed_ports as fp
# import power as pw
# import pwm_ports as pp
# import animation as ani

# # =====================================
# # IMPORTAR LIBRERÍAS NECESARIAS
# # =====================================
# import tkinter as tk
# from tkinter import *
# from PIL import ImageTk, Image
# import os 
# import sys
# from tkinter import messagebox
# import threading

# #===========================
# # CREAR PANTALLA TKINTER
# #===========================
# pantalla = tk.Tk()

# # Resolución
# screen_width = pantalla.winfo_screenwidth()
# screen_height = pantalla.winfo_screenheight()

# # Tamaño de la ventana
# window_width = 800
# window_height = screen_height

# # Centrar la ventana verticalmente
# position_left = 0
# position_top = int((screen_height - window_height) / 2)

# # Geometría de la ventana
# pantalla.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')
# pantalla.title("Arduino Board Control")
# pantalla.config(background="black")

# # ===============================
# # CARGAR ICONO DE LA APLICACIÓN
# # ===============================
# """PyInstaller extrae los archivos en una carpeta temporal (sys._MEIPASS) cuando se ejecuta el programa empaquetado.
# Por lo tanto, es necesario obtener la ruta base del proyecto para cargar la imagen del icono."""
# # Obtener la ruta base del proyecto
# if getattr(sys, 'frozen', False):  # Si está empaquetado con PyInstaller
#     BASE_DIR = sys._MEIPASS
# else:
#     BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")) # Subimos dos niveles desde src/python/ hasta raiz/

# # Construir la ruta relativa a la imagen
# icon_path = os.path.join(BASE_DIR, "resources", "images", "icon_logo.png")

# # Cargar la imagen
# icono = tk.PhotoImage(file=icon_path)
# pantalla.iconphoto(True, icono)

# # ======================
# # CARGAR IMAGEN LOGO
# # ======================

# # Cargar y redimensionar la imagen
# imagen_path = os.path.join(BASE_DIR, "resources", "images", "full_logo.png")
# imagen_original = Image.open(imagen_path) # Abrir la imagen con PIL
# imagen_redimensionada = imagen_original.resize((700, 220))  # Ajustamos al tamaño deseado
# imagen_inferior = ImageTk.PhotoImage(imagen_redimensionada)  # Convertimos para Tkinter

# # Crear el Label con la imagen de fondo
# label_imagen_inferior = tk.Label(pantalla, image=imagen_inferior, bg="black")
# label_imagen_inferior.place(x=50, y=750)  # Ajusta la imagen a la ventana

# # ====================================================
# # CREAR BOTONES ON-OFF PARA PINES DIGITALES FIJOS
# # ====================================================
# # Crear un Frame negro en la parte superior
# header_frame1 = tk.Frame(pantalla, bg="black", width=175, height=270)
# header_frame1.place(x=30, y=30)

# # Agregar el título dentro del Frame
# titulo_leds = tk.Label(
#     header_frame1, 
#     text="FIXED Pins", 
#     font=("Bahnschrift Condensed", 18, "bold"),  # Fuente negrita y subrayada
#     bg="black", 
#     fg="white"
# )
# titulo_leds.place(x=30, y=10)

# boton_d8 = tk.Button(pantalla, text="D8 - A0 ", font=("Bahnschrift Condensed", 16), bg="steel blue", width=12,
#                     command=lambda: [fp.on_off_button(fp.fixedDigitalPins[0], boton_d8), pin_states.update({0: not pin_states[0]})])
# boton_d8.place(x=60, y=90)

# boton_d9 = tk.Button(pantalla, text="D9 - A1", font=("Bahnschrift Condensed", 16), bg="steel blue", width=12, 
#                     command=lambda: [fp.on_off_button(fp.fixedDigitalPins[1], boton_d9), pin_states.update({1: not pin_states[1]})])
# boton_d9.place(x=60, y=150)

# boton_d10 = tk.Button(pantalla, text="D10 - A2", font=("Bahnschrift Condensed", 16), bg="steel blue", width=12, 
#                     command=lambda: [fp.on_off_button(fp.fixedDigitalPins[2], boton_d10), pin_states.update({2: not pin_states[2]})])
# boton_d10.place(x=60, y=210)

# boton_d11 = tk.Button(pantalla, text="D11 - A3", font=("Bahnschrift Condensed", 16), bg="steel blue", width=12, 
#                     command=lambda: [fp.on_off_button(fp.fixedDigitalPins[3], boton_d11), pin_states.update({3: not pin_states[3]})])
# boton_d11.place(x=60, y=270)


# # ====================================================
# # CREAR BOTONES PARA PINES DIGITALES PWM
# # ====================================================

# # Crear un Frame negro en la parte superior
# header_frame2 = tk.Frame(pantalla, bg="black", width=175, height=180)
# header_frame2.place(x=235, y=30)

# # Agregar el título dentro del Frame
# titulo_rgb = tk.Label(
#     header_frame2, 
#     text="PWM Pins", 
#     font=("Bahnschrift Condensed", 18, "bold"),  # Fuente negrita y subrayada
#     bg="black", 
#     fg="white"
# )
# titulo_rgb.place(x=35, y=10)

# boton_d3 = tk.Button(pantalla, text="D3 - A4 ", font=("Bahnschrift Condensed", 16), bg="steel blue", width=12, 
#                     command=lambda: [pp.on_off_button(pp.pwmDigitalPins[0], boton_d3), pin_states.update({4: not pin_states[4]})])
# boton_d3.place(x=270, y=90)

# boton_d5 = tk.Button(pantalla, text="D5 - A5 ", font=("Bahnschrift Condensed", 16), bg="steel blue", width=12, 
#                     command=lambda: [pp.on_off_button(pp.pwmDigitalPins[1], boton_d5), pin_states.update({5: not pin_states[5]})])
# boton_d5.place(x=270, y=150)


# # =====================================================
# # CREAR LECTURAS (V-I-P) DE LOS PINES ANALÓGICOS
# # =====================================================

# # Crear un Frame negro para mostrar el voltaje y corriente
# header_frame3 = tk.Frame(pantalla, bg="black", width=175, height=300)
# header_frame3.place(x=30, y=400)

# titulo_voltage = tk.Label(
#     header_frame3, 
#     text="V", 
#     font=("Bahnschrift Condensed", 18, "bold", "italic"),
#     bg="black", 
#     fg="white"
# )
# titulo_voltage.place(x=50, y=10)

# # Frame para mostrar la corriente
# header_frame4 = tk.Frame(pantalla, bg="black", width=175, height=300)
# header_frame4.place(x=235, y=400)  

# titulo_corriente = tk.Label(
#     header_frame4, 
#     text="I (mA)", 
#     font=("Bahnschrift Condensed", 18, "bold", "italic"),
#     bg="black", 
#     fg="white")
# titulo_corriente.place(x=40, y=10)

# # Frame para mostrar la potencia
# header_frame5 = tk.Frame(pantalla, bg="black", width=175, height=300)
# header_frame5.place(x=440, y=400)  

# titulo_corriente = tk.Label(
#     header_frame5, 
#     text="P (mW)", 
#     font=("Bahnschrift Condensed", 18, "bold", "italic"),
#     bg="black", 
#     fg="white")
# titulo_corriente.place(x=30, y=10)


# # Crear diccionarios de etiquetas para almacenar voltajes, corriente y potencia
# voltage_labels = {}
# intensity_labels = {}
# power_labels = {}

# # Crear diccionarios de etiquetas PWM para almacenar voltajes, corriente y potencia 
# pwm_voltage_labels = {}
# pwm_intensity_labels = {}
# pwm_power_labels = {}

# # Crear etiquetas para cada pin analógico
# def setup_labels():
#     """Crea las etiquetas para mostrar los valores de voltaje, intensidad y potencia."""
#     global voltage_labels, intensity_labels, power_labels
#     global pwm_voltage_labels, pwm_intensity_labels, pwm_power_labels

#     # Crear etiquetas para los pines A0-A3 (fijos)
#     for i in range(4):  # A0 - A3
#         voltage_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- V", font=("Bahnschrift Condensed", 16), bg="black", fg="red2")
#         voltage_labels[f"A{i}"].place(x=80, y=460 + (i * 35))  

#         intensity_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- mA", font=("Bahnschrift Condensed", 16), bg="black", fg="DarkOrange1")
#         intensity_labels[f"A{i}"].place(x=275, y=460 + (i * 35))  

#         power_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- mW", font=("Bahnschrift Condensed", 16), bg="black", fg="purple1")
#         power_labels[f"A{i}"].place(x=470, y=460 + (i * 35))

#     # Crear etiquetas para los pines A4 y A5
#     for i in [4, 5]:  # A4 - A5
#         pwm_voltage_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- V", font=("Bahnschrift Condensed", 16), bg="black", fg="red2")
#         pwm_voltage_labels[f"A{i}"].place(x=80, y=600 + ((i-4) * 35))  

#         pwm_intensity_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- mA", font=("Bahnschrift Condensed", 16), bg="black", fg="DarkOrange1")
#         pwm_intensity_labels[f"A{i}"].place(x=275, y=600 + ((i-4) * 35))  

#         pwm_power_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- mW", font=("Bahnschrift Condensed", 16), bg="black", fg="purple1")
#         pwm_power_labels[f"A{i}"].place(x=470, y=600 + ((i-4) * 35))

# setup_labels()            # Llamar a la función para inicializar las etiquetas al inicio


# # =====================================================================
# #  CREAR DICCIONARIO PARA ALMACENAR EL ESTADO DE LOS PINES APAGADOS
# # ====================================================================
# # Inicializar el estado de los pines como apagado (False)
# # Se inicializan los pines fijos (A0-A3) y los pines PWM (A4-A5) como apagados
# pin_states = {}
# for pin in fp.fixedAnalogPins:
#     pin_states[pin] = False

# for pin in [4, 5]:
#     pin_states[pin] = False

    
# #=====================================================
# # FUNCIONES DE VERIFICACIÓN DE CONEXIÓN
# #=====================================================
# # Crear etiqueta para el estado de la conexión
# conexion_label = tk.Label(pantalla, text="Connecting...", font=("Bahnschrift Condensed", 12), bg="white")
# conexion_label.place(x=650, y=30)

# conexion_activa = True              # Variable para verificar el estado de la conexión
# estado_conexion_anterior = False    # Inicializar a False

# def verificar_conexion():
#     global conexion_activa, estado_conexion_anterior
#     try:
#         # Comprobar la conexión con los puertos
#         pw.board.set_pin_mode_analog_input(fp.fixedAnalogPins[0])   # Intentar configurar un pin analógico
#         pw.board.set_pin_mode_analog_input(fp.fixedAnalogPins[1])   # Intentar configurar un pin analógico
#         pw.board.set_pin_mode_analog_input(fp.fixedAnalogPins[2])   # Intentar configurar un pin analógico
#         pw.board.set_pin_mode_analog_input(fp.fixedAnalogPins[3])   # Intentar configurar un pin analógico
#         pw.board.set_pin_mode_digital_output(pp.pwmDigitalPins[0])  # Configurar como salida digital
#         pw.board.set_pin_mode_digital_output(pp.pwmDigitalPins[1])  # Configurar como salida digital

#         if not conexion_activa:
#             # Si no se lanza ninguna excepción, la conexión es exitosa
#             conexion_label.config(text="Connection established", fg="green")
#             conexion_activa = True
#             # (MOSFET) Apagar leds establecer la conexión ****
#             print("Conexión establecida. Apagando LEDs...")
#             for pin in fp.fixedDigitalPins:
#                 pw.board.digital_write(pin, 0)  # Asegurar apagado de pines digitales fijos
#             for pin in pp.pwmDigitalPins:
#                 pw.board.digital_write(pin, 0)   # Asegurar apagado de pines PWM
#             # Fin de la adición MOSFET ****
#         estado_conexion_actual = True
#     except Exception:  # Capturar la excepción genérica
#         if conexion_activa:
#             # Si se lanza una excepción, la conexión ha fallado
#             conexion_label.config(text=f"Connection lost", fg="red")
#             conexion_activa = False
#             # Mostrar mensaje de error en una ventana emergente
#             messagebox.showerror("Hardware error", f"Communication hardware lost: Please contact supplier at it-support@bn-support.com.")
#         estado_conexion_actual = False
    
#     if estado_conexion_actual != estado_conexion_anterior:
#       if estado_conexion_actual:
#         conexion_label.config(text=f"Connection established", fg="green")
#       else:
#         conexion_label.config(text=f"Connection lost", fg="red")

#     estado_conexion_anterior = estado_conexion_actual
#     return conexion_activa

# # Llamar a la función al inicio
# verificar_conexion()

# # Lectturas fixed (V-I-P) de los pines analógicos
# def actualizar_lecturas():
#     if conexion_activa:
#         voltages = pw.update_voltage()         
#         intensities = pw.update_intensity()    
#         powers = pw.update_power()   

#         for pin in fp.fixedAnalogPins:
#             if pin_states[pin]:  # Si el pin está encendido
#                 voltage = voltages.get(f"A{pin}", 0.00)
#                 intensity = intensities.get(f"A{pin}", 0.00)
#                 power = powers.get(f"A{pin}", 0.00)
#             else:  # Si el pin está apagado
#                 voltage, intensity, power = 0.00, 0.00, 0.00

#             voltage_labels[f"A{pin}"].config(text=f"A{pin}: {voltage:.2f} V")
#             intensity_labels[f"A{pin}"].config(text=f"A{pin}: {intensity:.2f} mA")
#             power_labels[f"A{pin}"].config(text=f"A{pin}: {power:.2f} mW")

#     else: # Si la conexión está inactiva
#         for pin in fp.fixedAnalogPins:
#             voltage_labels[f"A{pin}"].config(text=f"A{pin}: 0.00 V")
#             intensity_labels[f"A{pin}"].config(text=f"A{pin}: 0.00 mA")
#             power_labels[f"A{pin}"].config(text=f"A{pin}: 0.00 mW")

#     pantalla.after(2000, actualizar_lecturas)  

# actualizar_lecturas()     # Llamar a la función cuando se inicie la GUI


# # Lectturas PWM (V-I-P) de los pines analógicos
# def actualizar_lecturas_cicloT():
#     if conexion_activa:
#         pwm_lectura = pw.update_lectura_pwm()  # Obtener las lecturas actualizadas de los pines PWM
        
#         for pin in [4, 5]:      # A4 y A5 son los pines PWM
#             if pin_states[pin]: # Si el pin está encendido
                
#                 # Actualizar la interfaz con los valores de los pines PWM (A4, A5)            
#                 voltage_pwm = pwm_lectura.get(f"A{pin}", {}).get("V", 0.00)
#                 intensity_pwm = pwm_lectura.get(f"A{pin}", {}).get("I", 0.00)
#                 power_pwm = pwm_lectura.get(f"A{pin}", {}).get("P", 0.00)
#             else:
#                 # Si el pin está apagado, mostrar 0.00 V, 0.00 mA y 0.00 mW
#                 voltage_pwm, intensity_pwm, power_pwm = 0.00, 0.00, 0.00

#             pwm_voltage_labels[f"A{pin}"].config(text=f"A{pin}: {voltage_pwm:.2f} V")
#             pwm_intensity_labels[f"A{pin}"].config(text=f"A{pin}: {intensity_pwm:.2f} mA")
#             pwm_power_labels[f"A{pin}"].config(text=f"A{pin}: {power_pwm:.2f} mW")

#     else:  
#         for pin in [4, 5]:
#             pwm_voltage_labels[f"A{pin}"].config(text=f"A{pin}: 0.00 V")
#             pwm_intensity_labels[f"A{pin}"].config(text=f"A{pin}: 0.00 mA")
#             pwm_power_labels[f"A{pin}"].config(text=f"A{pin}: 0.00 mW")
            
#     pantalla.after(2000, actualizar_lecturas_cicloT)  # Actualizar cada 2 segundos

# actualizar_lecturas_cicloT()                # Llamar a la función cuando se inicie la GUI
      

# # =======================================================
# # INICIALIZAR LOS PINES PWM CON EL CALLBACK PARA LECTURA
# # =======================================================
# pw.initialize_pwm_analog_pins(pp.board)     # *no leia la función en pwm_ports.py por eso no estaba leyendo los valores de los pines PWM


# #=============================================
# # VERIFICAR CONEXIÓN CON EL BOARD
# # ============================================
# def verificacion_periodica():
#     verificar_conexion()
#     pantalla.after(5000, verificacion_periodica)  # Verifica cada 5 segundos

# verificacion_periodica()  # Inicia la verificación periódica

# # ===========================================================
# # CREAR UN INPUT PARA INTRODUCIR LA TEMPERATURA Y HUMEDAD 
# # ===========================================================
# #
# # Crear un Frame negro en la parte superior
# label_input = tk.Frame(pantalla, bg="black", width=350, height=180)
# label_input.place(x=440, y=80)

# # =========================
# # CARGAR Y ANIMAR GIF
# # =========================

# # Crear el Label para la animación dentro del Frame
# label_animacion = tk.Label(label_input, bg="black", width=350, height=180)
# label_animacion.place(x=0, y=0)  # Dentro del Frame, sin desplazamiento


# # Cargar el GIF y animarlo
# ruta_del_gif = os.path.join(BASE_DIR, "resources", "videos", "gif_p.gif") # Añadir ruta de la carpeta de recurso mediante os.path.join
# ani.cargar_y_animar_gif(label_animacion, ruta_del_gif, intervalo=100, ancho=300, alto=180 ) # Ajusta el intervalo si es necesario

# # # Agregar el título dentro del Frame
# # titulo_TemHum = tk.Label(
# #     label_input, 
# #     text="Input Temperature and Humidity", 
# #     font=("Arial", 10, "bold", "underline"),  # Fuente negrita y subrayada
# #     bg=None,  # Color de fondo del Frame
# #     fg="white"
# # )
# # titulo_TemHum.place(x=50, y=10)

# # Campos de entrada para temperatura y humedad
# etiqueta_temperatura = tk.Label(label_input, text="Temperature (°C):", bg="black", fg="white", font=("Bahnschrift Condensed", 12))
# etiqueta_temperatura.place(x=30, y=10)
# entrada_temperatura = tk.Entry(label_input, bg="dark goldenrod", width=4)
# entrada_temperatura.place(x=30, y=40)

# etiqueta_humedad = tk.Label(label_input, text="Humidity (%):", bg="black", fg="white", font=("Bahnschrift Condensed", 12))
# etiqueta_humedad.place(x=30, y=70)
# entrada_humedad = tk.Entry(label_input, bg="dark goldenrod", width=4)
# entrada_humedad.place(x=30, y=100)

# lock = threading.Lock()

# # Función para obtener los valores ingresados
# def obtener_valores():
#     try:
#         temperatura = float(entrada_temperatura.get())
#         humedad = float(entrada_humedad.get())
#         assert 0 <= temperatura <= 55, "Temperature must be between 0 and 55 °C"
#         assert 0 <= humedad <= 100, "Humidity must be between 0 and 100 %"

#         with pw.lock:
#             if not (15 <= temperatura <= 30 and 40 <= humedad <= 50):
#                 pw.parpadeando_temperatura = (temperatura < 15 or temperatura > 30)
#                 pw.parpadeando_humedad = (humedad > 50)
#                 print(f"Parpadeo activado: Temp={pw.parpadeando_temperatura}, Hum={pw.parpadeando_humedad}")
#             else:
#                 pw.parpadeando_temperatura = False
#                 pw.parpadeando_humedad = False
#                 pw.board.analog_write(pp.pwmDigitalPins[0], 0)
#                 pw.board.analog_write(pp.pwmDigitalPins[1], 0)
#                 boton_d3.config(bg="steel blue")
#                 boton_d5.config(bg="steel blue")
#                 print(f"Temperatura ingresada: {temperatura} °C, Humedad ingresada: {humedad} %")
#     except AssertionError as e:
#         messagebox.showerror("Error", str(e))
#         pass

# # Botón para obtener los valores
# boton_obtener = tk.Button(label_input, text="Get values", font=("Bahnschrift Condensed", 14), width=12, bg="DarkGoldenrod4", fg="white", command=obtener_valores)
# boton_obtener.place(x=30, y=130)

# # Iniciar los hilos de parpadeo al inicio
# threading.Thread(target=pp.parpadear_led_temperatura, args=(pp.pwmDigitalPins[0], boton_d3, "red"), daemon=True).start()
# threading.Thread(target=pp.parpadear_led_humedad, args=(pp.pwmDigitalPins[1], boton_d5, "blue"), daemon=True).start()


# # =======================================================
# # DESCONECTAR EL BOARD AL CERRAR LA VENTANA
# # =======================================================
# def cerrar_ventana():
#     try:
#         # Apagar pines 
#         for pin in fp.fixedDigitalPins:
#             pw.board.digital_write(pin, 0)  # Apagar pines digitales fijos
#         for pin in pp.pwmDigitalPins:
#             pw.board.analog_write(pin, 0)  # Apagar pines PWM

#         pw.board.shutdown()  # Enviar mensaje de "stop streaming"
#     except Exception:
#         messagebox.showerror(f"Error al cerrar la conexión:")
#     finally:
#         pantalla.destroy()  # Cerrar la ventana de la GUI   

# pantalla.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Llamar a la función al cerrar la ventana (debe colocarse antes "pantalla.mainloop()" para que funcione correctamente)")


# # ====================
# # INICIAR LA GUI
# # ====================
# def iniciar_gui():
#     pantalla.mainloop()




###############
### PYSIDE6 ###
###############

# IMPORTAR LIBRERÍAS

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGridLayout, QListWidget, QListWidgetItem
from PySide6.QtCore import QTimer
import sys

import fixed_ports as fp
import power as pw

class ArduinoGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Board Control 3.0.0")
        self.setStyleSheet("background-color: black; color: white;")
        self.resize(700, 500)

        # Inicializa los pines al arrancar la GUI
        fp.setup_pins()

        main_layout = QVBoxLayout()

        # Pines digitales
        digital_label = QLabel("Digital Pins")
        digital_label.setStyleSheet("font-size: 18px; color: #FFD700;")
        main_layout.addWidget(digital_label)

        digital_grid = QGridLayout()
        self.digital_buttons = {}
        for idx, pin in enumerate(fp.fixedDigitalPins):
            btn = QPushButton(f"D{pin}: OFF")
            btn.setCheckable(True)
            btn.setStyleSheet("background-color: #444; color: white; font-size: 16px;")
            btn.clicked.connect(lambda checked, p=pin: self.toggle_digital_pin(p))
            self.digital_buttons[pin] = btn
            digital_grid.addWidget(btn, idx // 4, idx % 4)
        main_layout.addLayout(digital_grid)

        # Pines analógicos
        analog_label = QLabel("Analog Pins (Readings)")
        analog_label.setStyleSheet("font-size: 18px; color: #00BFFF;")
        main_layout.addWidget(analog_label)

        self.analog_list = QListWidget()
        self.analog_list.setStyleSheet("background-color: #222; color: white; font-size: 15px;")
        main_layout.addWidget(self.analog_list)

        self.setLayout(main_layout)

        # Timer para actualizar lecturas
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_analog_readings)
        self.timer.start(1500)

    def toggle_digital_pin(self, pin):
        new_state = fp.toggle_pin(pin)
        btn = self.digital_buttons[pin]
        if new_state:
            btn.setText(f"D{pin}: ON")
            btn.setStyleSheet("background-color: #228B22; color: white; font-size: 16px;")
        else:
            btn.setText(f"D{pin}: OFF")
            btn.setStyleSheet("background-color: #444; color: white; font-size: 16px;")

    def update_analog_readings(self):
        voltajes = pw.update_voltage()
        try:
            powers = pw.update_power()
        except Exception:
            powers = {}
        self.analog_list.clear()
        for pin in fp.fixedAnalogPins:
            voltage = voltajes.get(f"A{pin}", 0.0)
            power = powers.get(f"A{pin}", 0.0)
            item_text = f"A{pin}: {voltage:.2f} V | {power:.2f} W"
            item = QListWidgetItem(item_text)
            self.analog_list.addItem(item)

# # EXECUTE GUI  -------------------------- TRASLADADO A MAIN
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ArduinoGUI()
#     window.show()
#     sys.exit(app.exec())