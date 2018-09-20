import sys
from PyQt5.QtWidgets import (QApplication, 
	 QWidget, QToolTip, QMessageBox, 
	 QDesktopWidget ,QPushButton)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('This is a <b>QWidget</b> widget')
		btn = QPushButton('Button', self)
		btn.clicked.connect(QCoreApplication.instance().quit)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(50, 50)
		
		self.resize(300,300)
		self.center()
		self.setWindowTitle('ToolTip')
		self.setWindowIcon(QIcon('web.png'))
		self.show()
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		
	def closeEvent(self, event):
		reply = QMessageBox.question(self,'Message',
					'Are you sure to quit?', QMessageBox.Yes | 
					QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__ == '__main__':
	app = QApplication(sys.argv)

	ex = Example()

	sys.exit(app.exec_())