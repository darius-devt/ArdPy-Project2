# ======================
# IMPORTAR FICHEROS
# ======================
from arduino_board import board

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

# ======================
# DEFINIR pinOnOFF PWM
# ======================
# Función para encender o apagar los pines PWM con un efecto gradual
"""Usando steps = 50 y incrementos de 5, llegamos justo a 255."""
"""Para evitar el parpadeo, el valor de delay se calcula como duration / steps."""
def pinPWM(pin, turn_on, duration=3):

    def transicion_pwm():                           # esta función se ejecuta en un hilo separado, para evitar bloqueos
        steps = 50                                  # Número de pasos para la transición suave
        delay = duration / steps                    # Tiempo de espera entre cada cambio de brillo

        
        if turn_on:
            for value in range(0, 256, 5):          # Aumenta el brillo de 0 a 255
                board.analog_write(pin, value)
                time.sleep(delay)
        else:
            for value in range(255, -1, -5):        # Reduce el brillo de 255 a 0
                board.analog_write(pin, value)
                time.sleep(delay)
            board.analog_write(pin, 0)              # Apagar completamente
                
        
    
    # Crear un hilo para ejecutar la función sin bloquear el programa
    """Esto permite que la GUI siga siendo receptiva mientras se realiza el fade y no se congela la interfaz gráfica"""
    thread = threading.Thread(target=transicion_pwm)
    thread.start()

# ==============================
# CONTROL DE BOTÓN ON/OFF PWM
# ==============================

# Diccionario para almacenar el estado de cada pin (encendido/apagado)
states = {}

def on_off_button(pin, button):

    if pin not in states:
        states[pin] = False             # Si el pin no está en states, lo inicializamos en False

    if states[pin]:
        button.config(bg="gray")        # Cambiar color del botón a apagado
        states[pin] = False
        pinPWM(pin, False, 3)    # Apagar el PWM con efecto gradual
    else:
        button.config(bg="blue")        # Cambiar color del botón al color azul
        states[pin] = True
        pinPWM(pin, True, 3)     # Encender el PWM con efecto gradual