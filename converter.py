import sys
from urllib.request import urlopen
from lxml import etree

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)

class Course(QObject):
    CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    def get(self):
        with urlopen(self.CBR_URL) as r:
            tree = etree.parse(r)
            value = tree.xpath('*[@ID="R01235"]/Value')[0].text
            return float(value.replace(',', '.'))

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initLayouts()
        self.initSignals()


    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)
        #self.resultAmount.setReadOnly(True)

        self.convertBtn = QPushButton('Перевести', self)
        self.convertBtn.setDisabled(True)

        self.clearBtn = QPushButton('Сбросить', self)


    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClickConvertBtn)
        self.clearBtn.clicked.connect(self.onClickClearBtn)
        self.srcAmount.valueChanged.connect(self.setButtonAvailability)
        self.resultAmount.valueChanged.connect(self.setButtonAvailability)


    def initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)

        self.setCentralWidget(w)


    def onClickConvertBtn(self):
        value = self.srcAmount.value()
        result_value = self.resultAmount.value()

        if value:
            self.resultAmount.setValue(value / Course().get())
        elif result_value:
            self.srcAmount.setValue(result_value * Course().get())


    def onClickClearBtn(self):
        self.resultAmount.setValue(0)
        self.srcAmount.setValue(0)


    def setButtonAvailability(self):
        value = self.srcAmount.value()
        result_value = self.resultAmount.value()

        if value and result_value or not value and not result_value:
            self.convertBtn.setDisabled(True)
        else:
            self.convertBtn.setDisabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
	
    converter = MainWindow()
    converter.show()

    sys.exit(app.exec_())