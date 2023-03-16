# -*- coding: utf-8 -*-
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QObjectCleanupHandler
from PyQt5.QtWidgets import QWidget, QMessageBox
from card_layout import *
from data import *
from memo_edit_layout import *
from menu_layout import *
from random import shuffle, choice
from memo_wiki import *
ques_num = 0
questions_dict = {}
#app = QApplication([])
card_width, card_height = 600,500
test = Test(q_list) 
def ok_btn_clk():
    test.testing(radio_list, checking, question_lbl, correct, win, win_menu)
def showMenu():
    timer.stop()
    win.hide()
    win_menu.show()
def start_quiz(): 
    global test
    global seconds
    seconds = 60
    timer_lbl.setText(f"<font size = 4><b>Час: {str(seconds)}</b></text>")
    win_menu.hide()
    win.show() 
    timer.start()
    test = Test(q_list)    
    test.q.show_data(question_lbl, radio_list, correct)
def start_add_q():
    window_e.show()
def start_wiki():
    win_wiki.show()
def start_quit():
    app.quit()
def start_aboutApp():
    about = QMessageBox()
    about.setWindowTitle("Про додаток")
    about.setText("Цей додаток-вікторина був створений на мові программування Python з використовуванням бібліотеки PyQt5. <br></br><br>Як користуватися: У додатку вже є 10 запитань, які можна пройти для тестування себе. Також можна додавати запитання, для цього в меню є кнопка - Створити запитання. Для створення запитання потрібно спочатку обрати тип запитання(із зображеннями або ні). Question означає що варіанти відповіді будуть без зображень, але можна буде додати зображення в запитання. Question_gui це як Question тільки навпаки, також можна додавати зображення в запитання, але тепер можна додати іх і у варіанти відповіді.</br><br></br> <br>Творець додатку: Яровенко Володимир</br>")
    about.exec_()
def add_question_in():
    global ques_num
    global questions_dict
    if radio_btn_ques.isChecked():
        questions_dict[f"q{ques_num}_text"] = [question_form.text(), correct_answer_form.text(), incorrect_answer_form1.text(), incorrect_answer_form2.text(), incorrect_answer_form3.text()]
        questions_dict[f"q{ques_num}"] = Question(questions_dict[f"q{ques_num}_text"][0],questions_dict[f"q{ques_num}_text"][1],questions_dict[f"q{ques_num}_text"][2],questions_dict[f"q{ques_num}_text"][3],questions_dict[f"q{ques_num}_text"][4])
    if radio_btn_quesGui.isChecked():
        questions_dict[f"q{ques_num}_text"] = [question_form.text(), correct_answer_form.text(), incorrect_answer_form1.text(), incorrect_answer_form2.text(), incorrect_answer_form3.text(), width_form.text(), height_form.text()]
        questions_dict[f"q{ques_num}"] = Question_gui(questions_dict[f"q{ques_num}_text"][0],questions_dict[f"q{ques_num}_text"][1],questions_dict[f"q{ques_num}_text"][2],questions_dict[f"q{ques_num}_text"][3],questions_dict[f"q{ques_num}_text"][4], questions_dict[f"q{ques_num}_text"][5], questions_dict[f"q{ques_num}_text"][6])
    q_list.append(questions_dict[f"q{ques_num}"])
    print(q_list)
    text = ", ".join(questions_dict[f"q{ques_num}_text"])
    ques_num += 1
    listQ.addItem(text)
def counter():
    global seconds
    seconds -= 1
    timer_lbl.setText(f"<font size = 4><b>Час: {str(seconds)}</b></text>")
    if seconds <= 0:
        timer.stop()
        win.hide()
        enough = QMessageBox()
        enough.setText("<font size = 4><b>Час вичерпано!</b></text>")
        enough.exec_()
        app.exit()
def start_trening():
    global test
    global seconds
    seconds = 60
    timer_lbl.setText(f"<font size = 4><b>Час: {str(seconds)}</b></text>")
    win_menu.hide()
    window_e.hide()
    win.show()
    timer.start()
    test = Test(q_list)    
    test.q.show_data(question_lbl, radio_list, correct)
def counter2():
    global seconds2
    seconds2 -= 1
    if seconds2 <= 0:
        timer2.stop()
        timer.start()
def rest():
    global seconds2
    seconds2 = int(rest_spin.value())
    timer2.start()
    rest_msg = QMessageBox()
    rest_msg.setText("<b>Тобі треба відпочити</b>")
    rest_msg.exec_()

win = QWidget()
win.resize(card_width,card_height)
win.setWindowTitle("Memory Card")
win.move(0,0)
win.setLayout(main_layout)

timer.setInterval(1000)
timer.timeout.connect(counter)
timer2.setInterval(1000)
timer2.timeout.connect(counter2)

app.setStyleSheet("QWidget {background-image:url(img/back.jpg);}")

ok_btn.clicked.connect(ok_btn_clk)
menu_btn.clicked.connect(showMenu)
menu_btn_start.clicked.connect(start_quiz)
menu_btn_addq.clicked.connect(start_add_q)
menu_btn_wiki.clicked.connect(start_wiki)
menu_btn_quit.clicked.connect(start_quit)
menu_btn_about.clicked.connect(start_aboutApp)
add_btn.clicked.connect(add_question_in)
startTren_btn.clicked.connect(start_trening)
rest_btn.clicked.connect(rest)

app.exec_()