from random import shuffle, choice
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox
from card_layout import *
correct_answers = 0
class Question(): 
    def __init__(self, ques, cor_answer, incor_answer1, incor_answer2, incor_answer3):
        self.ques = ques
        self.cor_answer = cor_answer
        self.incor_answer1 = incor_answer1
        self.incor_answer2 = incor_answer2
        self.incor_answer3 = incor_answer3
    def show_data(self, question_lbl, radio_list, correct):
        question_lbl.setText(self.ques)
        correct.setText(self.cor_answer)
        shuffle(radio_list)
        radio_list[0].setText(self.cor_answer)
        radio_list[1].setText(self.incor_answer1)
        radio_list[2].setText(self.incor_answer2)
        radio_list[3].setText(self.incor_answer3)
        radio_list[0].setIcon(QIcon(""))
        radio_list[1].setIcon(QIcon(""))
        radio_list[2].setIcon(QIcon(""))
        radio_list[3].setIcon(QIcon(""))
    def check_result(self, radio_list, checking):
        if radio_list[0].isChecked():
            checking.setText("Правильно")
        else:
            checking.setText("Неправильно")
class Question_gui():
    def __init__(self, ques, cor_icon, incor_icon1, incor_icon2, incor_icon3, w, h):
        self.ques = ques
        self.cor_icon = cor_icon
        self.incor_icon1 = incor_icon1
        self.incor_icon2 = incor_icon2
        self.incor_icon3 = incor_icon3
        self.w = w
        self.h = h
    def show_data(self, question_lbl, radio_list, correct):
        question_lbl.setText(self.ques)
        correct.setText(f"<img src = {self.cor_icon}>")
        shuffle(radio_list)
        radio_list[0].setIcon(QIcon(self.cor_icon))
        radio_list[0].setIconSize(QSize(self.w,self.h))
        radio_list[0].setText("")
        radio_list[1].setIcon(QIcon(self.incor_icon1))
        radio_list[1].setIconSize(QSize(self.w,self.h))
        radio_list[1].setText("")
        radio_list[2].setIcon(QIcon(self.incor_icon2))
        radio_list[2].setIconSize(QSize(self.w,self.h))
        radio_list[2].setText("")
        radio_list[3].setIcon(QIcon(self.incor_icon3))
        radio_list[3].setIconSize(QSize(self.w,self.h))
        radio_list[3].setText("")
    def check_result(self, radio_list, checking):
        if radio_list[0].isChecked():
            checking.setText("Правильно")
        else:
            checking.setText("Неправильно")

class Test(Question, Question_gui):
    def __init__(self, q_list):
        self.q_list = q_list
        self.t_list = []
        for i in range(len(self.q_list)):
            self.t_list.append(self.q_list[i])
        self.q = choice(self.t_list)
    def testing(self, radio_list, checking, question_lbl, correct, win, win_menu):
        if len(self.t_list):
            if ok_btn.text() == "Відповісти":
                if radioBtnGroup.checkedButton():
                    show_result()
                    self.q.check_result(radio_list, checking)
                    self.t_list.remove(self.q)
            else:
                self.q = choice(self.t_list)
                self.q.show_data(question_lbl, radio_list, correct)
                show_question()
        else:
            for i in range(len(self.q_list)):
                self.t_list.append(self.q_list[i])
            self.q = choice(self.t_list)
            show_question()
            self.q.show_data(question_lbl, radio_list, correct)
            win.hide()
            win_menu.show()
            timer.stop()
q1 = Question("Яблуко", "apple", "classroom", "pen", "pineapple")
q2 = Question("Формула барій сульфат", "BaSO4", "I2O5", "Ba(SO4)3", "H2O")
q3 = Question("<img src = img/fernmag.jpg><br>Що за людина?</br>", "Фернан Магеллан", "Васко да Гама", "Муаммар Мухаммад Абу Миньяр аль-Каддафи", "Хамуд")
q4 = Question_gui("На якому з зображень показується Михайло Грушевський?", "img/mihalgrush.jpg", "img/simonpetlur.jpg", "img/pavloskoropad.jpg", "img/bogdchmel.jpg", 128, 128)
q5 = Question_gui("Як вірно зробити обробку винятків?", "img/tryexcept.png", "img/tryexceptnot1.png", "img/tryexceptnot2.png", "img/tryexcpetnot3.png", 256, 256)
q6 = Question_gui("На якому з зображень показується територія Ватикану?", "img/vatican.png", "img/shpicbergen.png", "img/nauru.png", "img/iceland.png", 128, 128)
q7 = Question("Формула дискримінанта", "b2 – 4ac", "a2-2ab+b2", "a2+2ab+b2", "c2=a2+b2")
q8 = Question("Формула питомої теплоємності (с)", "Q/mΔt", "s/t", "ρgV", "(mv2/2)+mgh")
q9 = Question_gui("Як вірно зробити вікно у PyQt5 з розміром 250 на 250?", "img/cor_app", "img/incor_app1","img/incor_app2", "img/incor_app3", 256, 256)
q10 = Question_gui("На якому з зображень показується прапор Грузії?", "img/cor_flag", "img/incor_flag1", "img/incor_flag2", "img/incor_flag3", 256, 256)

q_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]                                                                                                                                                                                         