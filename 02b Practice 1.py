# Try to make an application that is 600px tall and 800px wide, and put 3 labels and 3 pictures on it.
# Make them all visible.

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
# qpimap loads and manages the image file before it is place in a label.
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Memes")
        self.setGeometry(00, 00, 800, 600)  # (x, y, width, height)
        self.setWindowIcon(QIcon("images/python.png"))
        # added - label:
        self.label = QLabel("MeOW", self)
        # added- placing label:
        self.label.setFont(QFont("Arial", 40))
        self.label.setGeometry(0, 0, 500, 100)

        self.label.setStyleSheet(
            # This is CSS!
            "color: Yellow;"  # Supports HEX, RGB and ColorNames
            "background-color:blue;"  # Supports HEX, RGB and ColorNames
            "border: 10px solid black;"
            "font-weight:bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        self.label.setAlignment(Qt.AlignCenter)
        self.picklabel = QLabel(self)
        self.picklabel.setGeometry(250, 250, 300, 250)
        self.pixmap = QPixmap("images/Skyler.png")
        # put the image (pixmap) into the label
        self.picklabel.setPixmap(self.pixmap)
        # if image is too big or too small, we can make it fit our commit
        self.picklabel.setScaledContents(True)
        # Lets try putting Greg in the bottom right corner - we'll use MATH!
        self.picklabel.setGeometry(550, 550, 300, 250)

        # ---------------------------------------------------------------------

        #self.setWindowIcon(QIcon("images/cat.png"))
        # added - label:
        self.label = QLabel("Skyler white yo", self)
        # added- placing label:
        self.label.setFont(QFont("Arial", 40))
        self.label.setGeometry(450, 450, 500, 100)

        self.label.setStyleSheet(
            # This is CSS!
            "color: Yellow;"  # Supports HEX, RGB and ColorNames
            "background-color:blue;"  # Supports HEX, RGB and ColorNames
            "border: 10px solid black;"
            "font-weight:bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        self.label.setAlignment(Qt.AlignCenter)
        self.picklabel = QLabel(self)
        self.picklabel.setGeometry(0, 100, 300, 250)
        self.pixmap = QPixmap("images/cat.png")
        # put the image (pixmap) into the label
        self.picklabel.setPixmap(self.pixmap)
        # if image is too big or too small, we can make it fit our commit
        self.picklabel.setScaledContents(True)
        # Lets try putting Greg in the bottom right corner - we'll use MATH!
        self.picklabel.setGeometry(100, 100, 300, 250)

        # ---------------------------------------------------------------------

        #self.setWindowIcon(QIcon("images/boi.png"))
        # added - label:
        self.label = QLabel("Hehe Boi", self)
        # added- placing label:
        self.label.setFont(QFont("Arial", 40))
        self.label.setGeometry(1000, 0, 500, 100)

        self.label.setStyleSheet(
            # This is CSS!
            "color: Yellow;"  # Supports HEX, RGB and ColorNames
            "background-color:blue;"  # Supports HEX, RGB and ColorNames
            "border: 10px solid black;"
            "font-weight:bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        self.label.setAlignment(Qt.AlignCenter)
        self.picklabel = QLabel(self)
        self.picklabel.setGeometry(0, 100, 300, 250)
        self.pixmap = QPixmap("images/boi.png")
        # put the image (pixmap) into the label
        self.picklabel.setPixmap(self.pixmap)
        # if image is too big or too small, we can make it fit our commit
        self.picklabel.setScaledContents(True)
        # Lets try putting Greg in the bottom right corner - we'll use MATH!
        self.picklabel.setGeometry(1100, 100, 300, 250)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()  # Instatiate our main window
    window.show()  # Makes the window visible

    # Starts the application loop. The program will keep running until you close the window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()