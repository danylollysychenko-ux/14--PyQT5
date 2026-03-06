"""
Create the grid below (focusing on the layout) with any 4 pictures you like (see note below for the 5th).
Each grid cell should have a different background color. - this is to show space consumption if the picture does not take up all the space available in its cell. 

The grid must contain 3 visual columns (note the varying widths of each column).
 
In column 1, there are 2 pictures of UNIQUE heights to take up the full height of the window.
In column 2 (wider than col 1 and col 3, a single picture taking up the full height)
In column 3 (wider than col 1, but narrower than col 2): 2 pictures of UNIQUE heights to take up the full height of the window.
"""

from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow, QApplication
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Practice")
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
        label6 = QLabel("Label 6")
        label7 = QLabel("Label 7")

        # Give our labels some color:
        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: yellow")
        label4.setStyleSheet("background-color: green")
        label5.setStyleSheet("background-color: purple")
        label6.setStyleSheet("background-color: pink")
        label7.setStyleSheet("background-color: brown")

        layout = QGridLayout()
        # layout.setColumnStretch(1, 2)
        # layout.setColumnStretch(0, 1)
        # layout.setColumnStretch(2, 1)
        # label1.setFixedWidth(600)
        # label2.setFixedHeight(950)
        # label3.setFixedHeight(1900)
        # label4.setFixedWidth(650)
        layout.addWidget(label1, 0, 0, 2, 1)
        layout.addWidget(label2, 2, 0, 4, 1)
        layout.addWidget(label3, 0, 1, 6, 1)
        layout.addWidget(label4, 0, 2, 4, 1)
        layout.addWidget(label5, 4, 2, 2, 1)

        self.centralWidget.setLayout(layout)


def main():
    # This creates the main application and passes in a y command line arguments
    app = QApplication(sys.argv)
    window = MainWindow()  # Instatiate our main window
    window.show()  # Makes the window visible

    # Starts the application loop. The program will keep running until you close the window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
