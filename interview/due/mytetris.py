from PyQt5.QtWidgets import QVBoxLayout,QWidget,QMainWindow,QGroupBox,QGridLayout ,QLabel,QFrame, QPushButton, QDesktopWidget, QApplication, QHBoxLayout
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QSize
from PyQt5.QtGui import QPainter, QColor, QPalette
from enum import Enum
import sys, random


class Direct(Enum):
    Right = 1
    Down = 2
    Left = 3
    Up = 4

class Snake(QMainWindow):

    def __init__(self):
        super(Snake, self).__init__()

        self.initUI()


    def initUI(self):
        self.setFixedSize(400, 400)

        self.tboard = Board(self)

        self.setCentralWidget(self.tboard)

        self.center()
        self.setWindowTitle('Snake')        
        self.show()
        self.tboard.start()


    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)

class Board(QFrame):
    BoardWidth = 10
    BoardHeight = 10
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        self.timer = QBasicTimer()
        self.board = [(Board.BoardWidth // 2, Board.BoardHeight // 2)]
        self.direct = Direct.Left
        self.setFocusPolicy(Qt.StrongFocus)
        self.newFood()

    def start(self):
        self.timer.start(Board.Speed, self)

    def tryMove(self):
        if self.direct == Direct.Right:
            x=self.board[0][0]+1
            y=self.board[0][1]
        
        elif self.direct == Direct.Left:
            x=self.board[0][0]-1
            y=self.board[0][1]

        elif self.direct == Direct.Down:
            x=self.board[0][0]
            y=self.board[0][1]+1

        elif self.direct == Direct.Up:
            x=self.board[0][0]
            y=self.board[0][1]-1

        if x < 0 or x >= self.BoardWidth or y < 0 or y >= self.BoardHeight:
            return False

        if (x, y) in self.board:
                return False

        self.board.insert(0, (x,y))
        
        if not self.eatFood(x, y):
            self.board.pop()
        
        self.update()

        return True

    def eatFood(self, x, y):
        if self.food == (x, y):
            self.newFood()
            return True
        else:
            return False

    def newFood(self):
        self.food = (random.randint(0, Board.BoardWidth-1),
                     random.randint(0, Board.BoardHeight-1))
        
        if self.food in self.board:
            self.newFood()

    def keyPressEvent(self, event):
        '''processes key press events'''

        key = event.key()

        if key == Qt.Key_Left:
            if self.direct != Direct.Left and self.direct != Direct.Right:
                self.direct = Direct.Left
                self.tryMove()

        elif key == Qt.Key_Right:
            if self.direct != Direct.Right and self.direct != Direct.Left:
                self.direct = Direct.Right
                self.tryMove()

        elif key == Qt.Key_Down:
            if self.direct != Direct.Down and self.direct != Direct.Up:
                self.direct = Direct.Down
                self.tryMove()

        elif key == Qt.Key_Up:
            if self.direct != Direct.Up and self.direct != Direct.Down:
                self.direct = Direct.Up
                self.tryMove()

        else:
            super(Board, self).keyPressEvent(event)

    def paintEvent(self, event):
        '''paints all shapes of the game'''

        painter = QPainter(self)

        for i in range(len(self.board)):
            x = self.board[i][0]
            y = self.board[i][1]
            color = 2
            if i == 0:
                color = 3
                self.drawEllipse(painter,
                            x * self.squareWidth(),
                            y * self.squareHeight(),
                            color)
                continue
            self.drawSquare(painter,
                            x * self.squareWidth(),
                            y * self.squareHeight(),
                            color)

        self.drawSquare(painter, 
                        self.food[0] * self.squareWidth(),
                        self.food[1] * self.squareHeight(),
                        5)

    def timerEvent(self, event):
        '''handles timer event'''

        if event.timerId() == self.timer.timerId():
            self.tryMove()
        else:
            super(Board, self).timerEvent(event)

    def squareWidth(self):
        '''returns the width of one square'''

        return self.contentsRect().width() / Board.BoardWidth


    def squareHeight(self):
        '''returns the height of one square'''

        return self.contentsRect().height() / Board.BoardHeight
        # return self.squareWidth()

    def drawEllipse(self, painter, x, y, color):
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        color = QColor(colorTable[color])
        painter.setBrush(color)
        painter.setPen(color,0)
        painter.drawEllipse(x, y, self.squareWidth(), self.squareHeight())

    def drawSquare(self, painter, x, y, shape):
        '''draws a square of a shape'''  

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
            self.squareHeight() - 2, color)

        # painter.setPen(color.lighter())
        # painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        # painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        # painter.setPen(color.darker())
        # painter.drawLine(x + 1, y + self.squareHeight() - 1,
        #     x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        # painter.drawLine(x + self.squareWidth() - 1, 
        #     y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

if __name__ == '__main__':

    app = QApplication([])
    tetris = Snake()    
    sys.exit(app.exec_())