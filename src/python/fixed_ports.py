# # ======================
# # IMPORTAR FICHEROS
# # ======================
# import power as pw
# from arduino_board import board
# import time

# #=========================================
# #DECLARAR PINES ANALOGICOS Y DIGITALES
# #=========================================
# fixedAnalogPins = [0, 1, 2, 3]
# fixedDigitalPins = [8, 9, 10, 11] 

# # ======================
# # DEFINIR pinOnOFF
# # ======================
# # Función para encender o apagar los pines digitales
# def pinOnOFF(board, pin, value):
#     if pin in fixedDigitalPins:
#         board.digital_write(pin, value)  # Encender (1) o Apagar (0) el LED

# states = {}

# def on_off_button(pin, button):

#     if pin not in states:
#         states[pin] = False       # Si el pin no está en states, lo inicializamos en False

#     if states[pin]:
#         button.config(bg="steel blue")  # Cambiar color del botón a apagado
#         states[pin] = False
#         pinOnOFF(board, pin, 0)
#     else:
#         button.config(bg="green")  # Cambiar color del botón al color azul
#         states[pin] = True
#         pinOnOFF(board, pin, 1)

# # ===========================================
# # Configurar cada pin digital como salida
# # ===========================================
# for pin in fixedDigitalPins:
#     board.set_pin_mode_digital_output(pin)

# # =====================================================================
# # Configurar los pines analógicos A0 a A3 con el callback para lectura
# # =====================================================================
# pw.initialize_analog_pins(board)

# # Esperar un poco para que las lecturas se realicen
# time.sleep(1)


###############
### PYSIDE6 ###
###############

import power as pw
from arduino_board import board

fixedAnalogPins = [0, 1, 2, 3]
fixedDigitalPins = [8, 9, 10, 11]

# Diccionario para guardar el estado de los pines digitales
states = {pin: False for pin in fixedDigitalPins}

def pinOnOFF(pin, value):
    """Enciende o apaga el pin digital especificado."""
    if pin in fixedDigitalPins:
        board.digital_write(pin, value)
        states[pin] = bool(value)

def toggle_pin(pin):
    """Alterna el estado del pin digital y devuelve el nuevo estado (True=ON, False=OFF)."""
    new_state = not states[pin]
    pinOnOFF(pin, int(new_state))
    return new_state

def setup_pins():
    """Configura los pines digitales como salida y los analógicos para lectura."""
    for pin in fixedDigitalPins:
        board.set_pin_mode_digital_output(pin)
        pinOnOFF(pin, 0)  # Asegura que todos los pines estén apagados al inicio
    pw.initialize_analog_pins(board)