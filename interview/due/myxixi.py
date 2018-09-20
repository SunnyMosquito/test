from PyQt5.QtWidgets import QVBoxLayout,QWidget,QMainWindow,QGroupBox,QGridLayout ,QLabel,QFrame, QPushButton, QDesktopWidget, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QSize
from PyQt5.QtGui import QPainter, QColor, QPalette
from enum import Enum, unique
import sys, random

@unique
class Direct(Enum):
    E = 1 # East
    S = 2 # South
    W = 3
    N = 4

class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setFixedSize(380, 480)

        self.centralwidget = QWidget(self)

        self.hbox = QHBoxLayout(self.centralwidget)

        self.tboard = Board(self)
        self.hbox.addWidget(self.tboard)

        self.slide = Slide(self)
        self.slide.setStyleSheet("QWidget{background-color: rgb(17, 19, 207)}")
        btn = QPushButton('hello', self.slide)
        self.hbox.addWidget(self.slide)

        self.hbox.setStretch(0, 6)
        self.hbox.setStretch(1, 4)

        self.setLayout(self.hbox)

        self.setCentralWidget(self.centralwidget)

        self.center()
        self.setWindowTitle('Tetris')        
        self.show()
        self.tboard.start()


    def center(self):
        '''centers the window on the screen'''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)

class Board(QFrame):
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        self.timer = QBasicTimer()
        self.board = [(Board.BoardWidth // 2, Board.BoardHeight // 2)]
        self.direct = Direct.L

    def start(self):
        self.timer.start(300, self)

    def tryMove(self):


    def paintEvent(self, event):
        '''paints all shapes of the game'''

        painter = QPainter(self)

        for x, y in self.board:
            self.drawSquare(painter,
                x * self.squareWidth(),
                y * self.squareHeight())

    def timerEvent(self, event):
        '''handles timer event'''

        if event.timerId() == self.timer.timerId():
            self.tryMove()
        else:
            super(Board, self).timerEvent(event)

    def squareWidth(self):
        '''returns the width of one square'''

        return self.contentsRect().width() // Board.BoardWidth


    def squareHeight(self):
        '''returns the height of one square'''

        return self.contentsRect().height() // Board.BoardHeight

    def drawSquare(self, painter, x, y):
        '''draws a square of a shape'''  

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[2])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
            self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, 
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

class Slide(QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.initSlide()

    def initSlide(self):
        pass

if __name__ == '__main__':

    app = QApplication([])
    tetris = Tetris()    
    sys.exit(app.exec_())