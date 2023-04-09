from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Викторина')
main_win.move(480,200)
main_win.resize(400, 50)

question = QLabel('В КАКОМ ГОДУ БЫЛ СОЗДАН BRAWL STARS???')
btn_answer1 = QRadioButton('2018')
btn_answer2 = QRadioButton('2016')
btn_answer3 = QRadioButton('2019')
btn_answer4 = QRadioButton('2020')
layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer4, alignment = Qt.AlignCenter)

layoutH1 = QVBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Верно!')
    victory_win.exec_()
def show_lose():
    victory_lose = QMessageBox()
    victory_lose.setText('Неверно!')
    victory_lose.exec_()

btn_answer1.clicked.connect(show_win)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec_()