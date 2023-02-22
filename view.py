from PyQt6.QtWidgets import *
from PyQt6 import QtGui
#from PyQt6 import uic
from client import Client
import json

class View(QMainWindow):
    def __init__(self, c: Client):
        super().__init__()
        self.controller = c

        self.base_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.center_layout = QVBoxLayout()
        self.bot_layout = QHBoxLayout()

        self.base_widget = QWidget()
        self.top_widget = QWidget()
        self.center_widget = QWidget()
        self.bot_widget = QWidget()

        self.input_label = QLabel('Please provide your text here:')
        self.output_label = QLabel('Here is your result:')

        self.input_textedit = QTextEdit()
        self.output_textedit = QTextEdit()
        self.output_textedit.setDisabled(True)

        self.check_pushbutton = QPushButton('check')
        self.reset_pushbutton = QPushButton('reset')
        self.close_pushbutton = QPushButton('close')

        self.check_pushbutton.clicked.connect(self.check)
        self.reset_pushbutton.clicked.connect(self.controller.reset_view)
        self.close_pushbutton.clicked.connect(self.controller.exit_view)

        self.setWindowTitle('My language tool')

        self.top_layout.addWidget(self.input_label)
        self.top_layout.addWidget(self.input_textedit)
        self.top_widget.setLayout(self.top_layout)
        self.center_layout.addWidget(self.output_label)
        self.center_layout.addWidget(self.output_textedit)
        self.center_widget.setLayout(self.center_layout)
        self.bot_layout.addWidget(self.check_pushbutton)
        self.bot_layout.addWidget(self.reset_pushbutton)
        self.bot_layout.addWidget(self.close_pushbutton)
        self.bot_widget.setLayout(self.bot_layout)



        self.base_layout.addWidget(self.top_widget)
        self.base_layout.addWidget(self.center_widget)
        self.base_layout.addWidget(self.bot_widget)
        self.base_widget.setLayout(self.base_layout)

        self.setCentralWidget(self.base_widget)


    def exit(self):

        # close the application
        self.close()

    def reset(self):

        # reset the in/output
        self.input_textedit.clear()
        self.output_textedit.clear()

        # clear statusbar
        self.statusBar().showMessage('')

    def check(self):
        
        # clear statusbar
        self.statusBar().showMessage('')

        # get inputtext
        source = self.input_textedit.toPlainText()

        # check if input is empty
        if source != '':

            # get response
            response = self.controller.detect_language(source)
            # print(type(response))
            # response = dict(json.loads(response))
            # print(type(response))
            if response is None:
                self.statusBar().showMessage('Error - make sure the service is running')
            else:
                self.output_textedit.setText(self.dict_to_text(response))
        else:
            self.statusBar().showMessage('Error - make sure the input is not empty')

    def dict_to_text(self, input: dict):
        if type(input) != dict:
            return 'input was not a dictionary'
        output = str()
        # output += str(input['betrag']) + ' ' + input['src'] + ' entsprechen' + '\n'
        for key in input:
            output += key + ': ' + str(input[key]) + '\n'
        return output