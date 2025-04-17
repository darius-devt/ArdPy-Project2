# ======================
# IMPORTAR FICHEROS
# ======================
from arduino_board import board

# =========================================
# DECLARAR PINES ANALOGICOS Y DIGITALES
# =========================================
pwmAnalogPins = [4,5]
pwmDigitalPins = [3,5] 

# Configurar los pines PWM como salida
def setup_pwm_pins():
    """Configurar los pines digitales PWM como salida con control de ciclo de trabajo."""
    for pin in pwmDigitalPins:
        board.set_pin_mode_digital_output(pin)  # Configurar pines digitales como salida PWM
    

# Función para establecer el ciclo de trabajo desde el slider
def set_pwm_slider(pin, slider_value):
    """
    Ajusta el ciclo de trabajo del pin PWM en función del valor del slider (0-100%).
    
    :param pin: Pin digital en el que se configura el PWM.
    :param slider_value: Valor del slider (0-100%).
    """
    # Convertir el valor del slider a un rango de 0 a 255 para el PWM
    pwm_value = int(slider_value * 255 / 100)