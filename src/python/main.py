# # ======================
# # IMPORTAR FICHEROS
# # ======================
# import gui as g

# # =====================================
# # IMPORTAR LIBRERÍAS NECESARIAS
# # =====================================
# from tkinter import *


# g.iniciar_gui()


###############
### PYSIDE6 ###
###############

from PySide6.QtWidgets import QApplication
import sys

from gui import ArduinoGUI

# EXECUTE GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArduinoGUI()
    window.show()
    sys.exit(app.exec())