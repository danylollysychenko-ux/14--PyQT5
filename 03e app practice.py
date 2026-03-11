"""
Create the grid below (focusing on the layout) with any 4 pictures you like (see note below for the 5th).
Each grid cell should have a different background color. - this is to show space consumption if the picture does not take up all the space available in its cell. 

The grid must contain 3 visual columns (note the varying widths of each column).
 
In column 1, there are 2 pictures of UNIQUE heights to take up the full height of the window.
In column 2 (wider than col 1 and col 3, a single picture taking up the full height)
In column 3 (wider than col 1, but narrower than col 2): 2 pictures of UNIQUE heights to take up the full height of the window.
"""

from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow, QApplication
from PyQt5.QtCore import Qt
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

        label1 = QLabel()
        image_path = r"C:\Users\CMP_DaLysychenko\Desktop\Python\14  PyQT5\images\python.png"
        pixmap = QPixmap(image_path)
        label1.setPixmap(pixmap)
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        label1.setScaledContents(True)
        label1.setFixedSize(250, 400)
        
        pixmap = QPixmap(pixmap)

        if pixmap.isNull():
            print("Still not loading!")
        else:
            print("Image loaded!")

        label2 = QLabel()
        image_path = r"C:\Users\CMP_DaLysychenko\Desktop\Python\14  PyQT5\images\boi.png"
        pixmap = QPixmap(image_path)
        label2.setPixmap(pixmap)
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        label2.setScaledContents(True)
        label2.setFixedSize(250, 580)
        
        pixmap = QPixmap(pixmap)

        if pixmap.isNull():
            print("Still not loading!")
        else:
            print("Image loaded!")

        label3 = QLabel()
        image_path = r"C:\Users\CMP_DaLysychenko\Desktop\Python\14  PyQT5\images\cat.png"
        pixmap = QPixmap(image_path)
        label3.setPixmap(pixmap)
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        label3.setScaledContents(True)
        
        pixmap = QPixmap(pixmap)

        if pixmap.isNull():
            print("Still not loading!")
        else:
            print("Image loaded!")

        label4 = QLabel()
        image_path = r"C:\Users\CMP_DaLysychenko\Desktop\Python\14  PyQT5\images\dog.png"
        pixmap = QPixmap(image_path)
        label4.setPixmap(pixmap)
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        label4.setScaledContents(True)
        
        pixmap = QPixmap(pixmap)

        if pixmap.isNull():
            print("Still not loading!")
        else:
            print("Image loaded!")

        label5 = QLabel()
        image_path = r"C:\Users\CMP_DaLysychenko\Desktop\Python\14  PyQT5\images\whatisthis.png"
        pixmap = QPixmap(image_path)
        label5.setPixmap(pixmap)
        label5.setFixedSize(300, 300)
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        label5.setScaledContents(True)
        
        pixmap = QPixmap(pixmap)

        if pixmap.isNull():
            print("Still not loading!")
        else:
            print("Image loaded!")

        layout = QGridLayout()

        layout.addWidget(label1, 0, 0, 2, 1)
        layout.addWidget(label2, 2, 0, 4, 1)
        layout.addWidget(label3, 0, 1, 6, 1)
        layout.addWidget(label4, 0, 3, 5, 1)
        layout.addWidget(label5, 5, 3, 1, 1)

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