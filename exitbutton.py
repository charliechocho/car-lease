import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        QToolTip.setFont(QFont('Calibri', 20))
        btn = QPushButton('Quit', self)
        btn.setToolTip('This Button Exits The Application')
        btn.clicked.connect(QApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Fast Exit Window')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

