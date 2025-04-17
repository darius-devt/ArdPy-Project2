# =====================================
# IMPORTAR LIBRERÍAS NECESARIAS
# =====================================
from telemetrix import telemetrix

# ================================================
# CONECTAR LA PLACA ARDUINO MEDIANTE TELEMETRIX
# ================================================
board = telemetrix.Telemetrix()                     # Conexión física
# board = telemetrix.Telemetrix(com_port="COM4")    # COM4 para conexión con simulación virtual