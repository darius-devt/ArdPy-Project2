# ======================
# IMPORTAR FICHEROS
# ======================
from arduino_board import board
import power as pw

# =====================================
# IMPORTAR LIBRERÍAS NECESARIAS
# =====================================
import time
import threading

# =========================================
# DECLARAR PINES ANALOGICOS Y DIGITALES
# =========================================
pwmAnalogPins = [4,5]
pwmDigitalPins = [3,5] 

# =========================================
# CONFIGURAR LOS PINES PWM como salida 
# =========================================
def setup_pwm_pins():
    for pin in pwmDigitalPins:
        board.set_pin_mode_digital_output(pin)  # Configurar pines digitales como salida

# ==============================
# CONTROL DE BOTÓN ON/OFF PWM
# ==============================

# Diccionario para almacenar el estado de cada pin (encendido/apagado)
states = {}

def on_off_button(pin, button, color_on="blue"):
    if pin not in states:
        states[pin] = False

    if states[pin]:
        button.config(bg="gray")
        states[pin] = False
        board.analog_write(pin, 0)
    else:
        button.config(bg=color_on)
        states[pin] = True
        board.analog_write(pin, 255)


# =======================================================================================
# Función para hacer parpadear los LEDs según los rangos de temperatura y humedad
# =======================================================================================
def parpadear_led_temperatura(pin, boton, color):
    while True:
        with pw.lock:
            if pw.parpadeando_temperatura:
                board.analog_write(pin, 255)
                boton.config(bg=color)
            else:
                board.analog_write(pin, 0)
                boton.config(bg="gray")
        if pw.parpadeando_temperatura:
            time.sleep(3)
            with pw.lock:
                board.analog_write(pin, 0)
                boton.config(bg="gray")
            time.sleep(2)
        else:
            time.sleep(0.1)

def parpadear_led_humedad(pin, boton, color):
    while True:
        with pw.lock:
            if pw.parpadeando_humedad:
                board.analog_write(pin, 255)
                boton.config(bg=color)
            else:
                board.analog_write(pin, 0)
                boton.config(bg="gray")
        if pw.parpadeando_humedad:
            time.sleep(3)
            with pw.lock:
                board.analog_write(pin, 0)
                boton.config(bg="gray")
            time.sleep(2)
        else:
            time.sleep(0.1)