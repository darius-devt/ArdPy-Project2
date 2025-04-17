import tkinter as tk
from PIL import Image, ImageTk
import time

def cargar_y_animar_gif(widget, ruta_gif, intervalo=100):
    """
    Carga un GIF animado y lo muestra en un widget de Tkinter.

    Args:
        widget: El widget de Tkinter (Label o Canvas) donde se mostrará el GIF.
        ruta_gif: La ruta al archivo GIF.
        intervalo: El intervalo en milisegundos entre fotogramas (controla la velocidad de la animación).
    """
    try:
        gif = Image.open(ruta_gif)
        fotogramas = []
        try:
            while True:
                fotograma = ImageTk.PhotoImage(gif.copy())
                fotogramas.append(fotograma)
                gif.seek(gif.tell() + 1)
        except EOFError:
            pass  # Se llega al final del GIF

        # Almacenar el ID de la imagen como atributo del widget
        widget.fotogramas = fotogramas  # Guardar referencia a los fotogramas

        def actualizar_fotograma(indice):
            if fotogramas:
                nuevo_indice = (indice + 1) % len(fotogramas)
                if isinstance(widget, tk.Label):
                    widget.config(image=fotogramas[indice])
                else:
                    widget.itemconfig(widget.image_id, image=fotogramas[indice])
                widget.after(intervalo, actualizar_fotograma, nuevo_indice)

        if fotogramas:
            if isinstance(widget, tk.Label):
                widget.config(image=fotogramas[0])
            widget.after(intervalo, actualizar_fotograma, 1)

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo GIF en la ruta: {ruta_gif}")
    except Exception as e:
        print(f"Error al cargar el GIF: {e}")