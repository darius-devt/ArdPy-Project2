### CALIBRACIÓN DE LECTURAS DE POTENCIA Y CORRIENTE ###

import time
import power as pw
import fixed_ports as fp
from arduino_board import board

V_ENTRADA = 12.0  # Voltaje de entrada fijo (V)

def main():
    print("=== Calibration Tool (D8 y A2) ===")
    print("Solo se usará el pin digital D8 y el analógico A2.")
    print("Conecta una carga conocida (5W, 21W, 26W) a tu circuito.")
    print("Puedes encender/apagar D8 escribiendo 'on' o 'off' y pulsando ENTER.")
    print("Cuando veas un valor estable, pulsa ENTER para registrar el voltaje y la etiqueta (ej: 5W).")
    print("Pulsa Ctrl+C para salir.\n")

    # Inicializa solo el pin digital D8 y el analógico A2
    fp.board.set_pin_mode_digital_output(8)
    fp.board.digital_write(8, 0)
    pw.initialize_analog_pins(board)

    analog_pin = 2
    analog_key = f"A{analog_pin}"
    registros = []

    try:
        while True:
            voltajes = pw.update_voltage()
            voltage = voltajes.get(analog_key, 0.0)
            print(f"\rA2: {voltage:.4f} V  |  D8: {'ON' if fp.states[8] else 'OFF'}", end="", flush=True)
            entrada = input()
            if entrada.strip().lower() == "on":
                fp.toggle_pin(8)
                continue
            elif entrada.strip().lower() == "off":
                if fp.states[8]:  # Solo apaga si está encendido
                    fp.toggle_pin(8)
                continue
            elif entrada.strip().lower() == "d":
                estado = "ON" if fp.states[8] else "OFF"
                print(f"D8 está actualmente {estado}. Escribe 'on' o 'off' para cambiarlo.")
                continue

            etiqueta = input("Etiqueta para este valor (ej: 5W): ")
            try:
                potencia = float(etiqueta.replace("W", "").strip())
                corriente = potencia / V_ENTRADA
                resistencia = voltage / corriente if corriente > 0 else 0
                print(f"Estimación: Corriente = {corriente:.4f} A | Resistencia = {resistencia:.4f} Ω")
            except Exception:
                resistencia = None
                print("No se pudo calcular la resistencia (etiqueta no numérica).")

            registros.append((analog_key, voltage, etiqueta, resistencia))
            print(f"Registrado: A2 = {voltage:.4f} V -> {etiqueta}")
            print("Puedes cambiar la carga y repetir, o Ctrl+C para salir. ('on'/'off' para D8)")

    except KeyboardInterrupt:
        print("\n\n=== Resultados de calibración ===")
        for reg in registros:
            print(f"{reg[0]}: {reg[1]:.4f} V -> {reg[2]} | R_shunt estimada: {reg[3]:.4f} Ω" if reg[3] else f"{reg[0]}: {reg[1]:.4f} V -> {reg[2]}")
        print("\nPuedes copiar estos valores y usarlos para ajustar los rangos o la resistencia en power.py.")

if __name__ == "__main__":
    main()