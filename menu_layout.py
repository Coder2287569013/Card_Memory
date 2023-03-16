from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QWidget

win_menu = QWidget()
win_menu.resize(300,200)
win_menu.move(0,0)
win_menu.setWindowTitle("Меню")
win_menu.show()

menu_btn_start = QPushButton("Розпочати тестування")
menu_btn_addq = QPushButton("Створити запитання")
menu_btn_wiki = QPushButton("Довідник")
menu_btn_about = QPushButton("Про додаток")
menu_btn_quit = QPushButton("Вийти")

menu_layout = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()

menu_layout.addWidget(QLabel("<font size = 5><b>Вікторина!</b></font>"), alignment = Qt.AlignTop | Qt.AlignCenter)

line1.addStretch(1)
line1.addWidget(menu_btn_start, stretch = 4, alignment= Qt.AlignTop)
line1.addStretch(1)

line2.addStretch(1)
line2.addWidget(menu_btn_addq, stretch = 4, alignment= Qt.AlignTop)
line2.addStretch(1)

line3.addStretch(1)
line3.addWidget(menu_btn_wiki, stretch = 4, alignment= Qt.AlignTop)
line3.addStretch(1)

line4.addStretch(1)
line4.addWidget(menu_btn_about, stretch = 4, alignment= Qt.AlignTop)
line4.addStretch(1)

line5.addStretch(1)
line5.addWidget(menu_btn_quit, stretch = 4, alignment= Qt.AlignTop)
line5.addStretch(1)

menu_layout.addLayout(line1)
menu_layout.addLayout(line2)
menu_layout.addLayout(line3)
menu_layout.addLayout(line4)
menu_layout.addLayout(line5)

win_menu.setLayout(menu_layout)