"""
Layout Managers
a layout manager is a class that arranges widgets automatically in a certain pattern.
3 common LM types on PyQt5 are:
- QVBoxLayout - Stacks widgets vertically (top to bottom)
- QHBoxLayout - Places widgets horizontally
- QGridLayout - Arranges widgets in a grid of rows and columns
"""

from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Layout Example")
        self.setGeometry(700, 300, 400, 400)
        # up to this point, we did all our widget creation in the init.
        # # eventually, that gets super messy
        # Lets create some functions to pull that stuff out.
        self.initUI()

    def initUI(self):
        # Layout managers.
        # The QMainWindow already has its own layout manager that cannot be overwritten
        # So we must create widget to put layout manager in.
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        # The central widget will act as a container for all other widgets.

        # create a bunch of labels:
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")
        label4 = QLabel("Label 4")
        label5 = QLabel("Label 5")

        # Give our labels some color:
        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: yellow")
        label4.setStyleSheet("background-color: green")
        label5.setStyleSheet("background-color: purple")
        
        # Enter layout managers!
        # Horizontal - QHBoxLayout:
        hbox = QHBoxLayout()
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        self.centralWidget.setLayout(hbox)

def main():
    # This creates the main application and passes in a y command line arguments
    app = QApplication(sys.argv)
    window = MainWindow()  # Instatiate our main window
    window.show()  # Makes the window visible

    # Starts the application loop. The program will keep running until you close the window
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()