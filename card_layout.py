#подключение библиотек 
from PyQt5.Qt import Qt, QTimer
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QApplication, QGroupBox, QButtonGroup, QSpinBox, QMessageBox
from random import shuffle
seconds = 60
seconds2 = 60
app = QApplication([])
#создание application'а
def show_result():
    group_box.hide()
    group_box2.show()
    ok_btn.setText("Наступне запитання")

def show_question():
    radioBtnGroup.setExclusive(False)
    for rb in radio_list:
        rb.setChecked(False)
    radioBtnGroup.setExclusive(True)
    group_box.show()
    group_box2.hide()
    ok_btn.setText("Відповісти")
#создание ВАЖНЫХ виджетов для программы-опросника
menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")
rest_spin = QSpinBox()
rest_spin.setValue(30)
question_lbl = QLabel("")
timer_lbl = QLabel("")
radio_list = []

timer = QTimer()
#групп-боксы
group_box = QGroupBox("Варіанти відповідей")
group_box2 = QGroupBox("Результат теста")

#сгруппирование радио-кнопок
radioBtnGroup = QButtonGroup()
for i in range(4):
    radio_btn = QRadioButton()
    radio_list.append(radio_btn)
    radioBtnGroup.addButton(radio_btn)

#кнопка "ответить" и спрятанная кнопка "следующий вопрос"
ok_btn = QPushButton("Відповісти")

#правиряющий и отвечающий
correct = QLabel("")
checking = QLabel("")

#создание лайаута с радио-кнопками
layout_group = QHBoxLayout()
line1_group = QVBoxLayout()
line2_group = QVBoxLayout()
line1_group.addWidget(radio_list[0], alignment = Qt.AlignLeft)
line1_group.addWidget(radio_list[1], alignment = Qt.AlignLeft)
line2_group.addWidget(radio_list[2])
line2_group.addWidget(radio_list[3])
layout_group.addLayout(line1_group)
layout_group.addLayout(line2_group)

#добавление лайаута с радио-кнопками в групп-бокс
group_box.setLayout(layout_group)

#спрятанные елементы
layout_group2 = QHBoxLayout()
line3_group = QVBoxLayout()
line3_group.addWidget(checking, alignment = Qt.AlignTop | Qt.AlignLeft)
line3_group.addStretch(1)
line3_group.addWidget(correct, alignment = Qt.AlignHCenter)
line3_group.addStretch(1)
layout_group2.addLayout(line3_group)
group_box2.setLayout(layout_group2)

#создание лайаутов
main_layout = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

#верхняя строка
main_layout.addLayout(line1)
line1.addWidget(menu_btn, alignment = Qt.AlignLeft | Qt.AlignTop)
line1.addWidget(timer_lbl, alignment = Qt.AlignLeft | Qt.AlignTop)
line1.addStretch(2)
line1.addWidget(rest_btn, alignment = Qt.AlignTop)
line1.addWidget(rest_spin, alignment = Qt.AlignTop)
line1.addWidget(QLabel("хвилин"), alignment = Qt.AlignTop)

#вопрос и варианты ответа
main_layout.addStretch(1)
main_layout.addWidget(question_lbl, alignment= Qt.AlignCenter)
main_layout.addStretch(1)
main_layout.addWidget(group_box, stretch = 3)
main_layout.addWidget(group_box2, stretch = 3)
group_box2.hide()
main_layout.addStretch(1)

#добавление в лайаут кнопки "ответить" и спрятанной кнопки "следующий вопрос"
main_layout.addLayout(line2)
line2.addStretch(1)
line2.addWidget(ok_btn, stretch = 2)
line2.addStretch(1)