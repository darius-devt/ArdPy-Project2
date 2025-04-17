# ======================
# # IMPORTAR FICHEROS
# ======================
import fixed_ports as fp
import power as pw
import pwm_ports as pp

# =====================================
# IMPORTAR LIBRERÍAS NECESARIAS
# =====================================
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os 
import sys

#===========================
# CREAR PANTALLA TKINTER
#===========================
pantalla = tk.Tk()

# Resolución
screen_width = pantalla.winfo_screenwidth()
screen_height = pantalla.winfo_screenheight()

# Tamaño de la ventana
window_width = 800
window_height = screen_height

# Centrar la ventana verticalmente
position_left = 0
position_top = int((screen_height - window_height) / 2)

# Geometría de la ventana
pantalla.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')
pantalla.title("Arduino Board Control")
pantalla.config(background="white")

# ===============================
# CARGAR ICONO DE LA APLICACIÓN
# ===============================
"""PyInstaller extrae los archivos en una carpeta temporal (sys._MEIPASS) cuando se ejecuta el programa empaquetado.
Por lo tanto, es necesario obtener la ruta base del proyecto para cargar la imagen del icono."""
# Obtener la ruta base del proyecto
if getattr(sys, 'frozen', False):  # Si está empaquetado con PyInstaller
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")) # Subimos dos niveles desde src/python/ hasta raiz/

# Construir la ruta relativa a la imagen
icon_path = os.path.join(BASE_DIR, "resources", "images", "NIT.png")

# Cargar la imagen
icono = tk.PhotoImage(file=icon_path)
pantalla.iconphoto(True, icono)

# =========================
# CARGAR IMAGEN DE FONDO
# =========================

# Cargar y redimensionar la imagen
imagen_path = os.path.join(BASE_DIR, "resources", "images", "NIT.png")
imagen_original = Image.open(imagen_path) # Abrir la imagen con PIL
imagen_redimensionada = imagen_original.resize((1550, 800))  # Ajustamos al tamaño deseado
fondo = ImageTk.PhotoImage(imagen_redimensionada)  # Convertimos para Tkinter

# Crear el Label con la imagen de fondo
label_fondo = tk.Label(pantalla, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Ajusta la imagen a la ventana

# ====================================================
# CREAR BOTONES ON-OFF PARA PINES DIGITALES FIJOS
# ====================================================

# Crear un Frame negro en la parte superior
header_frame1 = tk.Frame(pantalla, bg="black", width=175, height=270)
header_frame1.place(x=30, y=30)

# Agregar el título dentro del Frame
titulo_leds = tk.Label(
    header_frame1, 
    text="Fixed Pins", 
    font=("Arial", 14, "bold", "underline"),  # Fuente negrita y subrayada
    bg="black", 
    fg="white"
)
titulo_leds.place(x=35, y=10)

boton_d8 = tk.Button(pantalla, text="D8 - A0 ", font=("Arial", 12), bg="gray", width=12, 
                     command=lambda: fp.on_off_button(fp.fixedDigitalPins[0], boton_d8))
boton_d8.place(x=60, y=90)

boton_d9 = tk.Button(pantalla, text="D9 - A1", font=("Arial", 12), bg="gray", width=12, 
                     command=lambda: fp.on_off_button(fp.fixedDigitalPins[1], boton_d9))
boton_d9.place(x=60, y=140)

boton_d10 = tk.Button(pantalla, text="D10 - A2", font=("Arial", 12), bg="gray", width=12, 
                     command=lambda: fp.on_off_button(fp.fixedDigitalPins[2], boton_d10))
boton_d10.place(x=60, y=190)

boton_d11 = tk.Button(pantalla, text="D11 - A3", font=("Arial", 12), bg="gray", width=12, 
                     command=lambda: fp.on_off_button(fp.fixedDigitalPins[3], boton_d11))
boton_d11.place(x=60, y=240)


# ====================================================
# CREAR BOTONES SLIDERS PARA PINES DIGITALES PWM
# ====================================================

# Crear un Frame negro en la parte superior
header_frame2 = tk.Frame(pantalla, bg="black", width=175, height=270)
header_frame2.place(x=235, y=30)

# Agregar el título dentro del Frame
titulo_rgb = tk.Label(
    header_frame2, 
    text="PWM Pins", 
    font=("Arial", 14, "bold", "underline"),  # Fuente negrita y subrayada
    bg="black", 
    fg="white"
)
titulo_rgb.place(x=40, y=10)

slider_d3 = tk.Scale(pantalla, from_=0, to=255, orient="horizontal", label="D3 - A4", 
                      font=("Arial", 10, "bold"), bg="blue", fg="white", width=10, 
                      command=lambda val: pw.regular_slider(pp.pwmDigitalPins[0], val))
slider_d3.place(x=270, y=80)
slider_d5 = tk.Scale(pantalla, from_=0, to=255, orient="horizontal", label="D5 - A5", 
                        font=("Arial", 10, "bold"), bg="blue", fg="white", width=10, 
                        command=lambda val: pw.regular_slider(pp.pwmDigitalPins[1], val))
slider_d5.place(x=270, y=150)


# =====================================================
# CREAR LECTURAS (V-I-P) DE LOS PINES ANALÓGICOS
# =====================================================

# Crear un Frame negro para mostrar el voltaje y corriente
header_frame3 = tk.Frame(pantalla, bg="black", width=175, height=300)
header_frame3.place(x=30, y=400)

titulo_voltage = tk.Label(
    header_frame3, 
    text="V", 
    font=("Arial", 14, "bold", "underline", "italic"),
    bg="black", 
    fg="white"
)
titulo_voltage.place(x=80, y=10)

# Frame para mostrar la corriente
header_frame4 = tk.Frame(pantalla, bg="black", width=175, height=300)
header_frame4.place(x=235, y=400)  

titulo_corriente = tk.Label(
    header_frame4, 
    text="I (mA)", 
    font=("Arial", 14, "bold", "underline", "italic"),
    bg="black", 
    fg="white")
titulo_corriente.place(x=60, y=10)

# Frame para mostrar la potencia
header_frame5 = tk.Frame(pantalla, bg="black", width=175, height=300)
header_frame5.place(x=440, y=400)  

titulo_corriente = tk.Label(
    header_frame5, 
    text="P (mW)", 
    font=("Arial", 14, "bold", "underline", "italic"),
    bg="black", 
    fg="white")
titulo_corriente.place(x=50, y=10)


# Crear diccionarios de etiquetas para almacenar voltajes, corriente y potencia
voltage_labels = {}
intensity_labels = {}
power_labels = {}

# Crear diccionarios de etiquetas PWM para almacenar voltajes, corriente y potencia 
pwm_voltage_labels = {}
pwm_intensity_labels = {}
pwm_power_labels = {}

# Crear etiquetas para cada pin analógico
def setup_labels():
    """Crea las etiquetas para mostrar los valores de voltaje, intensidad y potencia."""
    global voltage_labels, intensity_labels, power_labels
    global pwm_voltage_labels, pwm_intensity_labels, pwm_power_labels

    # Crear etiquetas para los pines A0-A3 (fijos)
    for i in range(4):  # A0 - A3
        voltage_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- V", font=("Arial", 12))
        voltage_labels[f"A{i}"].place(x=80, y=460 + (i * 35))  

        intensity_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- mA", font=("Arial", 12))
        intensity_labels[f"A{i}"].place(x=275, y=460 + (i * 35))  

        power_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- mW", font=("Arial", 12))
        power_labels[f"A{i}"].place(x=470, y=460 + (i * 35))

    # Crear etiquetas para los pines A4 y A5
    for i in [4, 5]:  # A4 - A5
        pwm_voltage_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- V", font=("Arial", 12))
        pwm_voltage_labels[f"A{i}"].place(x=80, y=600 + ((i-4) * 35))  

        pwm_intensity_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- mA", font=("Arial", 12))
        pwm_intensity_labels[f"A{i}"].place(x=275, y=600 + ((i-4) * 35))  

        pwm_power_labels[f"A{i}"] = tk.Label(pantalla, text=f"A{i}: --- mW", font=("Arial", 12))
        pwm_power_labels[f"A{i}"].place(x=470, y=600 + ((i-4) * 35))

setup_labels()            # Llamar a la función para inicializar las etiquetas al inicio


# Lectturas fixed (V-I-P) de los pines analógicos
def actualizar_lecturas():
    voltages = pw.update_voltage()         
    intensities = pw.update_intensity()    
    powers = pw.update_power()   

    for pin in fp.fixedAnalogPins:
        voltage = voltages.get(f"A{pin}", 0.00)
        intensity = intensities.get(f"A{pin}", 0.00)
        power = powers.get(f"A{pin}", 0.00)

        voltage_labels[f"A{pin}"].config(text=f"A{pin}: {voltage:.2f} V")
        intensity_labels[f"A{pin}"].config(text=f"A{pin}: {intensity:.2f} mA")
        power_labels[f"A{pin}"].config(text=f"A{pin}: {power:.2f} mW")

    pantalla.after(2000, actualizar_lecturas)  

actualizar_lecturas()     # Llamar a la función cuando se inicie la GUI


# Lectturas PWM (V-I-P) de los pines analógicos
def actualizar_lecturas_cicloT():
    pwm_lectura = pw.update_lectura_pwm()  # Obtener las lecturas actualizadas de los pines PWM
    
    # Actualizar la interfaz con los valores de los pines PWM (A4, A5)
    for pin in [4, 5]:  # A4 y A5 son los pines PWM
        voltage_pwm = pwm_lectura.get(f"A{pin}", {}).get("V", 0.00)
        intensity_pwm = pwm_lectura.get(f"A{pin}", {}).get("I", 0.00)
        power_pwm = pwm_lectura.get(f"A{pin}", {}).get("P", 0.00)

        pwm_voltage_labels[f"A{pin}"].config(text=f"A{pin}: {voltage_pwm:.2f} V")
        pwm_intensity_labels[f"A{pin}"].config(text=f"A{pin}: {intensity_pwm:.2f} mA")
        pwm_power_labels[f"A{pin}"].config(text=f"A{pin}: {power_pwm:.2f} mW")

    pantalla.after(2000, actualizar_lecturas_cicloT)  # Actualizar cada 2 segundos

actualizar_lecturas_cicloT()                # Llamar a la función cuando se inicie la GUI

# =======================================================
# INICIALIZAR LOS PINES PWM CON EL CALLBACK PARA LECTURA
# =======================================================
pw.initialize_pwm_analog_pins(pw.board)     # *no leia la función en pwm_ports.py por eso no estaba leyendo los valores de los pines PWM

# ====================
# INICIAR LA GUI
# ====================
def iniciar_gui():
    pantalla.mainloop()

