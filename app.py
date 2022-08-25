from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = Ui_MainWindow()
    w = QMainWindow()
    window.setupUi(w)
    w.show()
    app.exec()
