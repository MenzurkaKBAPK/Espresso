from PyQt5 import QtWidgets, QtCore
from PyQt5 import uic

import sys
import sqlite3


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.load_table()

    def load_table(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        result = cur.execute('''SELECT
        coffee.id, coffee.name, coffee.roasting, type.type, taste.feedback, coffee.price, coffee.weight
        FROM coffee
        JOIN type ON coffee.type = type.id
        JOIN taste ON coffee.taste = taste.id''').fetchall()

        con.close()

        if result:
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))

            for i in range(len(result)):
                for j in range(len(result[0])):
                    elem = result[i][j]
                    if elem:
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(elem)))


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
