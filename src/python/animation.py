import tkinter as tk
from PIL import Image, ImageTk
import time

# def cargar_y_animar_gif(widget, ruta_gif, intervalo=100, ancho=None, alto=None):
#     """
#     Carga un GIF animado y lo muestra en un widget de Tkinter.
#     """

#     try:
#         gif = Image.open(ruta_gif)
#         fotogramas = []

#         try:
#             while True:
#                 frame = gif.copy().convert("RGBA")
#                 if ancho and alto:
#                     frame = frame.resize((ancho, alto), Image.Resampling.LANCZOS)
#                 fotogramas.append(ImageTk.PhotoImage(frame))
#                 gif.seek(gif.tell() + 1)
#         except EOFError:
#             pass  # Fin del GIF

#         if not fotogramas:
#             print("El GIF no contiene múltiples fotogramas.")
#             return

#         widget.fotogramas = fotogramas
#         widget.indice_gif = 0
#         widget.animacion_activa = True

#         def animar():
#             if hasattr(widget, 'animacion_activa') and widget.animacion_activa:
#                 widget.config(image=widget.fotogramas[widget.indice_gif])
#                 widget.indice_gif = (widget.indice_gif + 1) % len(widget.fotogramas)
#                 widget.after_id = widget.after(intervalo, animar)

#         def detener_animacion():
#             if hasattr(widget, 'animacion_activa'):
#                 widget.animacion_activa = False
#                 if hasattr(widget, 'after_id'):
#                     widget.after_cancel(widget.after_id)
            
#         widget.detener_animacion = detener_animacion
#         widget.after(0, animar)

#     except FileNotFoundError:
#         print(f"Error: No se encontró el archivo GIF en la ruta: {ruta_gif}")
#     except Exception as e:
#         print(f"Error al cargar el GIF: {e}")