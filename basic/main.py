from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget ,QFileDialog, QGridLayout, QLabel, QProgressBar, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice
from time import sleep


#app settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Displaying Random words")
main_window.resize(300,200)

#create all objects/ widgets below here
title = QLabel("Random keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")

my_words = ["kamau", "omondi", "recently", "application","python", "matplotlib", "process", "yet", "slow", "Whereas", "decision", " tree", "fast", "operates", "easily", "large", " data", "sets", "especially","linear", "one"]

master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

# create function
def test_function():
    
    print("this button is working")


def random_word3():
    #text1.setText(my_words[random.randint(0, len(my_words)-1)])
    word = choice(my_words)
    text3.setText(word)

def random_word2():
    #text1.setText(my_words[random.randint(0, len(my_words)-1)])
    word = choice(my_words)
    text2.setText(word)

#event
button3.clicked.connect(random_word2)
button2.clicked.connect(test_function)
button1.clicked.connect(random_word3)


main_window.setLayout(master_layout)
main_window.show()
app.exec_()