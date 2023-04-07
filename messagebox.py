import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Fast Exit Window')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', 
            'Are you sure you want to quit?', QMessageBox.Yes |
             QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

