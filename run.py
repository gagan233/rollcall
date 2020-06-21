from PyQt5.QtWidgets import QApplication
from app import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

# For startup only
# App = QApplication(sys.argv)
# window = MainWindow()
# sys.exit(App.exec())
