import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# qpimap loads and manages the image file before it is place in a label.
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

"""
sys: This is a built-in Python module that provides access to variables and functions that interact with the Python interpreter.
PyQt5.QtWidgets: This module contains all the main GUI “widgets” such as buttons, labels, and windows.
QApplication: This class manages the GUI application itself.
QMainWindow: This class provides a main application window that you can customize.
"""

# Create a custon window:


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CMP 25-26 Year 1")
        self.setGeometry(00, 00, 500, 500)  # (x, y, width, height)
        # x: distance from the left edge of your screen
        # y: distance from the top of your screen
        self.setWindowIcon(QIcon("images/Greg.png"))
        # added - label:
        self.label = QLabel("Hello", self)
        # added- placing label:
        self.label.setFont(QFont("Arial", 40))
        self.label.setGeometry(0, 0, 500, 100)

        self.label.setStyleSheet(
            # This is CSS!
            "color: Yellow;"  # Supports HEX, RGB and ColorNames
            "background-color:red;"  # Supports HEX, RGB and ColorNames
            "border: 10px solid black;"
            "font-weight:bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        self.label.setAlignment(Qt.AlignCenter)
        self.picklabel = QLabel(self)
        self.picklabel.setGeometry(0, 100, 300, 250)
        self.pixmap = QPixmap("images/Greg.png")
        # put the image (pixmap) into the label
        self.picklabel.setPixmap(self.pixmap)
        # if image is too big or too small, we can make it fit our commit
        self.picklabel.setScaledContents(True)
        # Lets try putting Greg in the bottom right corner - we'll use MATH!
        self.picklabel.setGeometry(self.width(
        ) - self.picklabel.width(), self.height() - self.picklabel.height(), 300, 250)

        # Lets try putting Greg in the middle - we'll use MATH!
        self.picklabel.setGeometry((self.width(
        ) - self.picklabel.width()) // 2, (self.height() - self.picklabel.height()) // 2, 300, 250)


def main():
    # This creates the main application and passes in a y command line arguments
    app = QApplication(sys.argv)
    window = MainWindow()  # Instatiate our main window
    window.show()  # Makes the window visible

    # Starts the application loop. The program will keep running until you close the window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
