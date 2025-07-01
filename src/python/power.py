# # ======================
# # IMPORTAR FICHEROS
# # ======================
# import threading
# import fixed_ports as fp
# import pwm_ports as pp
# from arduino_board import board

# =========================================
# MEDIR CORRIENTE FIXED_PORTS (V,I,R,P)
# =========================================

# vcc = 60.0 # Voltaje de alimentación
# resistencia = 220

# # Diccionarios para almacenar los voltajes y las etiquetas de corriente
# voltajes = {}


# # Función de callback para leer los valores de los pines analógicos
# def analog_callback(data):
#     """Callback para leer el valor de los pines analógicos."""
#     global voltajes
#     pin = data[1]  # El número del pin
#     valor = data[2]  # El valor leído del ADC (0-1023)

#     # Convertir el valor ADC a voltaje (asumimos un rango de 5V)
#     voltaje = (valor / 1023.0) * vcc  # Valor en voltios

#     # Almacenar el voltaje en el diccionario global
#     voltajes[f"A{pin}"] = voltaje

# # Funciones para actualizar los datos de voltaje, intensidad y potencia
# def update_voltage():
#     return voltajes

# def update_intensity():
#     intensities = {}
#     for pin, voltage in voltajes.items():
#         intensities[pin] = (voltage / resistencia) * 1000  # mA
#     return intensities

# def update_power():
#     intensities = update_intensity()
#     powers = {}
#     for pin, voltage in voltajes.items():
#         powers[pin] = voltage * (intensities[pin] / 1000) * 1000  # mW
#     return powers

# # Función para inicializar los pines analógicos fijos
# def initialize_analog_pins(board):
#     """Configurar los pines analógicos A0 a A3 con el callback para lectura."""
#     for pin in fp.fixedAnalogPins:
#         board.set_pin_mode_analog_input(pin, callback=analog_callback)


# # =========================================
# # MEDIR CORRIENTE PWM_PORTS (V,I,R,P)
# # =========================================

# pwm_lecturas = {}  # Diccionario para almacenar las lecturas de V en los pines PWM

# # Función de callback para leer los valores de los pines PWM analógicos
# def pwm_analog_callback(data):
#     """Callback para leer el valor de los pines analógicos PWM."""
#     global pwm_lecturas
#     pin = data[1]   # El número del pin
#     valor = data[2]  # El valor leído del ADC (0-1023)
    
#     # Convierte el valor ADC (0-1023) a un voltaje
#     voltaje_pwm = (valor / 1023.0) * vcc            # Voltaje proporcional (suponiendo un rango de 0-5V)
    
#     # Almacenar el valor en el diccionario de lecturas de los pines PWM
#     pwm_lecturas[f"A{pin}"] = {"V": voltaje_pwm}    # Solo actualizamos voltaje por ahora

# def update_lectura_pwm():
#     """Actualizar mediciones de voltaje, intensidad y potencia según el ciclo de trabajo."""
#     lecturas = {}
    
#     for pin in pp.pwmAnalogPins:        
#         # Usar el voltaje real leído por el callback
#         voltaje_pwm = pwm_lecturas.get(f"A{pin}", {}).get("V", 0.00)  
        
#         # Calcular la corriente (en mA) usando la Ley de Ohm
#         intensidad_pwm = (voltaje_pwm / resistencia) * 1000 
        
#         # Calcular la potencia (en mW)
#         potencia_pwm = voltaje_pwm * (intensidad_pwm/ 1000) * 1000   # Convertir la potencia a mW
        
#         # Guardar los resultados en un diccionario
#         lecturas[f"A{pin}"] = {"V": voltaje_pwm, "I": intensidad_pwm, "P": potencia_pwm}
#     return lecturas

# # Función para inicializar los pines PWM analógicos (A4 y A5)
# def initialize_pwm_analog_pins(board):
#     """Configurar los pines analógicos PWM A4 y A5 con el callback para lectura."""
#     for pin in pp.pwmAnalogPins:  # Itera sobre los pines PWM definidos (A4, A5)
#         board.set_pin_mode_analog_input(pin, callback=pwm_analog_callback)


# # ===============================================
# # Función para iniciar el parpadeo de los LEDs
# # ===============================================
# parpadeando_temperatura = False  # Variable global para controlar el parpadeo de los LEDs
# parpadeando_humedad = False
# lock = threading.Lock()


###############
### PYSIDE6 ###
###############

import threading
import fixed_ports as fp
from arduino_board import board

V_ENTRADA = 12.0  # Voltaje de entrada fijo (V)
R_SHUNT = 0.2205  # Resistencia media del shunt en ohmios (calculada por calibración en calibration.py)

voltajes = {}

def analog_callback(data):
    """Callback para leer el valor de los pines analógicos."""
    global voltajes
    pin = data[1]  # El número del pin
    valor = data[2]  # El valor leído del ADC (0-1023)
    voltaje = (valor / 1023.0) * V_ENTRADA
    voltajes[f"A{pin}"] = voltaje

def update_voltage():
    """Devuelve el voltaje leído en cada pin analógico."""
    return voltajes

def update_current():
    """Devuelve la corriente estimada en cada pin analógico (I = Vshunt / Rshunt)."""
    corrientes = {}
    for pin, voltage in voltajes.items():
        corrientes[pin] = voltage / R_SHUNT
    return corrientes

def update_power():
    """Devuelve la potencia estimada en cada pin analógico (P = V_entrada * I_shunt)."""
    powers = {}
    corrientes = update_current()
    for pin, corriente in corrientes.items():
        powers[pin] = V_ENTRADA * corriente
    return powers

def initialize_analog_pins(board):
    """Configura los pines analógicos A0 a A3 con el callback para lectura."""
    for pin in fp.fixedAnalogPins:
        board.set_pin_mode_analog_input(pin, callback=analog_callback)

# Si no necesitas parpadeo, puedes eliminar estas variables
parpadeando_temperatura = False
parpadeando_humedad = False
lock = threading.Lock()