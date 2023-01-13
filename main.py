# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2 import QtCore
from PySide2.QtCore import Signal, Property
from time import strftime, localtime


class HammingCode(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.m_dataWord = ''
        self.m_codeWord = ''
        self.m_k = 0
        self.m_errPos = 0

    # Setter and Getter functions
    @QtCore.Slot('QString')
    def setDataWord(self, data):
        self.m_dataWord = data

    @QtCore.Property('QString')
    def getDataWord(self):
        return self.m_dataWord

    @QtCore.Slot('QString')
    def setCodeWord(self, data):
        self.m_codeWord = data

    @QtCore.Property('QString')
    def getCodeWord(self):
        return self.m_codeWord

    @QtCore.Slot('int')
    def setK(self, data):
        self.m_k = data

    @QtCore.Property('int')
    def getK(self):
        return self.m_k

    @QtCore.Slot('int')
    def setErrPos(self, data):
        self.m_errPos = data

    @QtCore.Property('int')
    def getErrPos(self):
        return self.m_errPos

    @QtCore.Slot('QString')
    def printText(self, text):
        print (text)
    ############################

    # Member functions that claculate hamming code
    @QtCore.Slot('int')
    def calcRedundantBits(self, n):
        for k in range(n):
            if(n <= 2**k - k - 1):
                self.m_k = k
                return

    @QtCore.Slot('QString')
    def posRedundantBits(self, data):
        n = len(data)
        k = self.m_k

        m = n + k

        j = 0
        l = 0
        res = ''
        for i in range(1, m + 1):
            if(i == 2**j):
                res += 'p'
                j += 1
            else:
                res += data[l]
                l += 1

        self.m_codeWord = res


    @QtCore.Slot()
    def calcParityBits(self):
        m = len(self.m_codeWord)
        k = self.m_k

        for i in range(k):
            val = 0
            for j in range(1, m + 1):
                if((j & (2**i) == (2**i)) and (j != 2**i)):
                    val = val ^ int(self.m_codeWord[j - 1])
            self.m_codeWord = self.m_codeWord[:(2**i) - 1] + self.m_codeWord[(2**i):]
            self.m_codeWord = self.m_codeWord[:(2**i) - 1] + str(val) + self.m_codeWord[(2**i) - 1:]
    ####################################################################################################

    # Member function that check error in hamming code
    @QtCore.Slot('QString')
    def detectError(self, data):
        m = len(data)
        k = self.m_k

        res = ''
        for i in range(k):
            val = 0
            for j in range(1, m + 1):
                if(j & (2**i) == (2**i)):
                    val = val ^ int(data[j - 1])

            res += str(val)

        res = res[::-1]
        self.m_errPos = int(res, 2)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    hamming = HammingCode()
    engine.rootContext().setContextProperty('hamming', hamming)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
