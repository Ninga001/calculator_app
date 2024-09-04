#import
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget ,QFileDialog, QGridLayout, QLabel, QProgressBar, QPushButton, QVBoxLayout,QLineEdit , QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from random import choice
from time import sleep

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        #App settings
        self.setWindowTitle("Calculator App")
        self.resize(420,500)

        #all object/widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica ", 12))
        self.grid = QGridLayout()

        self.buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","+",
            "-","0","^",".",
            "(","%",")","="
            
        ]   
            
        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_clicked)
            button.setStyleSheet("""
                QPushButton {
                    font: 25pt Conic Sans MS;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #ccc; /* change the background color on hover */
                    color: #333; /* change the text color on hover */
                }
            """)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.clear.setStyleSheet("""              
            QPushButton {
                font: 25pt Conic Sans MS;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #22DE73AA;                 
                color: #333; 
                }
        """)
        self.delete = QPushButton("Del")
        self.delete.setStyleSheet("""
            QPushButton {
                font: 25pt Conic Sans MS;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF0000;
                color: #333;
            }
        """)
        
        
         #Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)       

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25,25,25,25)

        #Show/run
        self.setLayout(master_layout)
        self.clear.clicked.connect(self.button_clicked)
        self.delete.clicked.connect(self.button_clicked)


    def button_clicked(self):
        button = app.sender()
        text = button.text()
        
        if text == "=":
            symbol = self.text_box.text()
            symbol = symbol.replace('^','**')
            symbol = symbol.replace('%', '/100')
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
                
            except Exception as e:
                print("Error :",e)
                
        elif text == "Clear":
            self.text_box.clear()
            
        elif text == "Del":
            current_value = self.text_box.text()
            self.text_box.setText(current_value[:-1])
            
        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)
                
   
if __name__ in "__main__": 
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color: #D5D7CEF2 }")
    main_window.show()
    app.exec_()