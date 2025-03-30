from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QRadioButton, QGroupBox, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup
from random import shuffle




class Question():
    def __init__(self, text, right_answer, wrongs):
        self.question = text
        self.right_answer = right_answer
        self.wrongs = wrongs




q1 = Question("В каком году было крещение Руси", "988", ["1922", "788", "922"])
q2 = Question("В каком году началась Вторая мировая война", "1939", ["1928", "1941", "1945"])
q3 = Question("В каких годах правил Ашурбанапал?", "669-627гг. до н.э.", ["1470-1488 до н.э.", "853-890гг. до н.э", "532-569гг. до н.э."])
qs = [q1, q2, q3]
numberQ = 0
amountRightAnswers = 0
def showAnswer():
    radioGroup.hide()
    group_bx.show()
    if numberQ == len(qs):
        btn.setText("Завершить")
    else:
        btn.setText("Следующий вопрос")
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)




def showResult():
    questin.setText("Поздравляем!")
    result.setText("Количество верных ответов " + str(amountRightAnswers))
    btn.hide()


def showQuestion():
    radioGroup.show()
    group_bx.hide()
    btn.setText("Ответить")




def checkBtn():
    if btn.text() == "Ответить":
        checkAnswer()
        showAnswer()


    elif btn.text() == "Завершить":
        showResult()
    else:
        ask(qs[numberQ])
        showQuestion()




def ask(q):
    global right_button, numberQ
    numberQ += 1
    questin.setText(q.question)
    buttns = [rbtn1, rbtn2, rbtn3, rbtn4]
    shuffle(buttns)
    answers = q.wrongs + [q.right_answer]
    for i in range(len(answers)):
        buttns[i].setText(answers[i])
        if i == 3:
            right_button = buttns[i]




def checkAnswer():
    global right_button, amountRightAnswers
    if right_button.isChecked():
        result.setText("Правильно")
        amountRightAnswers += 1
    else:
        result.setText(f"Неверно! Верный ответ {right_button.text()}")








app = QApplication([])
main_win = QWidget()
main_win.resize(1000, 700)








radioGroup = QGroupBox("Варианты ответов")




rbtn1 = QRadioButton("1 вариант")
rbtn2 = QRadioButton("2 вариант")
rbtn3 = QRadioButton("3 вариант")
rbtn4 = QRadioButton("4 вариант")
right_button = None








RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)








layot_ans1  = QHBoxLayout()
layot_ans2  = QVBoxLayout()
layot_ans3  = QVBoxLayout()




layot_ans2.addWidget(rbtn1, alignment = Qt.AlignCenter)
layot_ans2.addWidget(rbtn2, alignment = Qt.AlignCenter)




layot_ans3.addWidget(rbtn3, alignment = Qt.AlignCenter)
layot_ans3.addWidget(rbtn4, alignment = Qt.AlignCenter)




layot_ans1.addLayout(layot_ans2)
layot_ans1.addLayout(layot_ans3)
radioGroup.setLayout(layot_ans1)
questin = QLabel("ВОПРОС?")
btn = QPushButton("Ответить")




btn.clicked.connect(checkBtn)




group_bx = QGroupBox()
layot_res = QVBoxLayout()




result = QLabel("Правильный ответ")




layot_res.addWidget(result, alignment=Qt.AlignCenter)
group_bx.setLayout(layot_res)
group_bx.hide()




layot_main = QVBoxLayout()




layot_main.addWidget(questin, alignment = Qt.AlignCenter)
layot_main.addWidget(group_bx)
layot_main.addWidget(radioGroup, alignment = Qt.AlignCenter)
layot_main.addWidget(btn, alignment = Qt.AlignCenter)




main_win.setLayout(layot_main)
ask(qs[numberQ])
main_win.show()
app.exec_()

