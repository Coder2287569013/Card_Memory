from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QWidget, QMessageBox
import os
path_img = os.path.join(os.path.abspath(__file__+'\..'), "Resources")
def aboutMG():
    os.startfile(os.path.join(path_img, "aboutMG.mp4"))
def aboutCh():
    os.startfile(os.path.join(path_img, "aboutChemistry.mp4"))
def aboutFM():
    fernan = QMessageBox()
    fernan.setWindowTitle("Про Фернана Магеллана")
    fernan.setText("<img src = img/fernmag.jpg><br>Ферна́н (Ферна́ндо) Магелла́н (порт. Fernão de Magalhães, ісп. Fernando (Hernando) de Magallanes; 1480 — 27 квітня 1521) — португальський мореплавець на іспанській службі. Керував першою успішною навколосвітньою експедицією, під час якої сам Магеллан загинув. Дав назву західному океанові «Тихий океан».</br>")
    fernan.exec_()
def aboutFrEn():
    english = QMessageBox()
    english.setWindowTitle("Про назву фруктів на английськії мові")
    english.setText("apricot – абрикос<br>avocado – авокадо</br><br>pineapple – ананас</br><br>apple – яблоко</br><br>banana – банан</br><br>bergamot – бергамот</br><br>durian – дуриан</br><br>grapefruit – грейпфрут</br>")
    english.exec_()
def aboutExPy():
    os.startfile(os.path.join(path_img, "aboutExPy.mp4"))
def aboutHoly():
    os.startfile(os.path.join(path_img, "aboutVatikan.mp4"))
def aboutMath():
    math = QMessageBox()
    math.setWindowTitle("Про алгебру")
    math.setText("a3 - b3 = (a+b)(a2 + ab + b2), <br>D = b2 − 4ac</br>, <br>(a+b)2 = a2 + 2ab + b2</br>, <br>(a-b)2 = a2 - 2ab + b2</br>,<br>a2 - b2 = (a - b)(a + b)</br>, <br>a3 + b3 = (a+b)(a2 - ab + b2)</br>")
    math.exec_()
def aboutPh():
    os.startfile(os.path.join(path_img, "aboutPhy.docx"))
def aboutPyQt():
    pyqt = QMessageBox()
    pyqt.setWindowTitle("Про створення порожнього екрану на PyQt5")
    pyqt.setText("<img src = img/cor_app.png>")
    pyqt.exec_()
def aboutGeorgia():
    os.startfile(os.path.join(path_img, "aboutGeorgia.mp4"))

win_wiki = QWidget()
win_wiki.resize(250,250)
win_wiki.setWindowTitle("Довідник")

wiki_aboutEn = QPushButton("Дізнатися про тему 'фрукти' на английській мові")
wiki_aboutCh = QPushButton("Дізнатися про формули середній солей та їх назви")
wiki_aboutF = QPushButton("Дізнатся про Фернана Магеллана")
wiki_aboutM = QPushButton("Дізнатися про Михайло Грушевського")
wiki_aboutExPy = QPushButton("Дізнатися про обробку винятків у Python")
wiki_aboutHoly = QPushButton("Дізнатися про Ватикан")
wiki_aboutMath = QPushButton("Дізнатися про формули з алгебри 7-8 клас")
wiki_aboutPh = QPushButton("Дізнатися про формули з фізики 8 клас за I семестр")
wiki_aboutPyQt = QPushButton("Дізнатися про створення порожнього екрану в PyQt5")
wiki_aboutGeorgia = QPushButton("Дізнатися про прапор Грузії")

wiki_layout = QVBoxLayout()
wiki_line1 = QHBoxLayout()
wiki_line2 = QHBoxLayout()
wiki_line3 = QHBoxLayout()
wiki_line4 = QHBoxLayout()
wiki_line5 = QHBoxLayout()
wiki_line6 = QHBoxLayout()
wiki_line7 = QHBoxLayout()
wiki_line8 = QHBoxLayout()
wiki_line9 = QHBoxLayout()
wiki_line10 = QHBoxLayout()

wiki_line1.addStretch(0.5)
wiki_line1.addWidget(wiki_aboutM, stretch= 4)
wiki_line1.addStretch(0.5)

wiki_line2.addStretch(0.5)
wiki_line2.addWidget(wiki_aboutF, stretch= 4)
wiki_line2.addStretch(0.5)

wiki_line3.addStretch(0.5)
wiki_line3.addWidget(wiki_aboutCh, stretch= 4)
wiki_line3.addStretch(0.5)

wiki_line4.addStretch(0.5)
wiki_line4.addWidget(wiki_aboutEn, stretch= 4)
wiki_line4.addStretch(0.5)

wiki_line5.addStretch(0.5)
wiki_line5.addWidget(wiki_aboutExPy, stretch= 4)
wiki_line5.addStretch(0.5)

wiki_line6.addStretch(0.5)
wiki_line6.addWidget(wiki_aboutHoly, stretch= 4)
wiki_line6.addStretch(0.5)

wiki_line7.addStretch(0.5)
wiki_line7.addWidget(wiki_aboutMath, stretch= 4)
wiki_line7.addStretch(0.5)

wiki_line8.addStretch(0.5)
wiki_line8.addWidget(wiki_aboutPh, stretch= 4)
wiki_line8.addStretch(0.5)

wiki_line9.addStretch(0.5)
wiki_line9.addWidget(wiki_aboutPyQt, stretch= 4)
wiki_line9.addStretch(0.5)

wiki_line10.addStretch(0.5)
wiki_line10.addWidget(wiki_aboutGeorgia, stretch= 4)
wiki_line10.addStretch(0.5)

wiki_layout.addLayout(wiki_line1)
wiki_layout.addLayout(wiki_line2)
wiki_layout.addLayout(wiki_line3)
wiki_layout.addLayout(wiki_line4)
wiki_layout.addLayout(wiki_line5)
wiki_layout.addLayout(wiki_line6)
wiki_layout.addLayout(wiki_line7)
wiki_layout.addLayout(wiki_line8)
wiki_layout.addLayout(wiki_line9)
wiki_layout.addLayout(wiki_line10)

win_wiki.setLayout(wiki_layout)

wiki_aboutM.clicked.connect(aboutMG)
wiki_aboutCh.clicked.connect(aboutCh)
wiki_aboutF.clicked.connect(aboutFM)
wiki_aboutEn.clicked.connect(aboutFrEn)
wiki_aboutExPy.clicked.connect(aboutExPy)
wiki_aboutHoly.clicked.connect(aboutHoly)
wiki_aboutMath.clicked.connect(aboutMath)
wiki_aboutPh.clicked.connect(aboutPh)
wiki_aboutPyQt.clicked.connect(aboutPyQt)
wiki_aboutGeorgia.clicked.connect(aboutGeorgia)