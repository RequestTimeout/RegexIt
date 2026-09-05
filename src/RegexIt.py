from PyQt5 import QtCore, QtGui, QtWidgets
import re


class RegexItUI(object):
    def __init__(self, RegexIt):
        RegexIt.setObjectName("RegexIt")
        RegexIt.resize(560, 680)
        RegexIt.setMinimumSize(QtCore.QSize(420, 480))
        RegexIt.setStyleSheet("QWidget#RegexIt {\n"
                              "    background-color: #1e1e2e;\n"
                              "}\n"
                              "\n"
                              "QLabel {\n"
                              "    color: #cdd6f4;\n"
                              "    font-size: 13px;\n"
                              "    padding-top: 2px;\n"
                              "}\n"
                              "\n"
                              "QLineEdit, QPlainTextEdit {\n"
                              "    background-color: #282a3d;\n"
                              "    color: #e6e6f0;\n"
                              "    border: 1px solid #3b3d54;\n"
                              "    border-radius: 6px;\n"
                              "    padding: 8px;\n"
                              "    selection-background-color: #89b4fa;\n"
                              "    selection-color: #1e1e2e;\n"
                              "}\n"
                              "\n"
                              "QLineEdit:focus, QPlainTextEdit:focus {\n"
                              "    border: 1px solid #89b4fa;\n"
                              "}\n"
                              "\n"
                              "QLineEdit::placeholder, QPlainTextEdit {\n"
                              "    color: #6c7086;\n"
                              "}\n"
                              "\n"
                              "QLineEdit#regexInput {\n"
                              "    border-left: 3px solid #f38ba8;\n"
                              "}\n"
                              "\n"
                              "QPlainTextEdit#textInput {\n"
                              "    border-left: 3px solid #89b4fa;\n"
                              "}\n"
                              "\n"
                              "QPlainTextEdit#resultOutput {\n"
                              "    background-color: #232437;\n"
                              "    border-left: 3px solid #a6e3a1;\n"
                              "    color: #d6f5d6;\n"
                              "}\n"
                              "\n"
                              "QScrollBar:vertical {\n"
                              "    background: #1e1e2e;\n"
                              "    width: 10px;\n"
                              "    margin: 0px;\n"
                              "}\n"
                              "\n"
                              "QScrollBar::handle:vertical {\n"
                              "    background: #45475a;\n"
                              "    border-radius: 5px;\n"
                              "    min-height: 20px;\n"
                              "}\n"
                              "\n"
                              "QScrollBar::handle:vertical:hover {\n"
                              "    background: #585b70;\n"
                              "}\n"
                              "\n"
                              "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
                              "    height: 0px;\n"
                              "}")
        self.mainLayout = QtWidgets.QVBoxLayout(RegexIt)
        self.mainLayout.setContentsMargins(16, 16, 16, 16)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName("mainLayout")
        self.regexLabel = QtWidgets.QLabel(RegexIt)
        font = QtGui.QFont()
        font.setBold(True)
        self.regexLabel.setFont(font)
        self.regexLabel.setObjectName("regexLabel")
        self.mainLayout.addWidget(self.regexLabel)
        self.regexInput = QtWidgets.QLineEdit(RegexIt)
        self.regexInput.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.regexInput.setFont(font)
        self.regexInput.setObjectName("regexInput")
        self.mainLayout.addWidget(self.regexInput)
        self.textLabel = QtWidgets.QLabel(RegexIt)
        font = QtGui.QFont()
        font.setBold(True)
        self.textLabel.setFont(font)
        self.textLabel.setObjectName("textLabel")
        self.mainLayout.addWidget(self.textLabel)
        self.textInput = QtWidgets.QPlainTextEdit(RegexIt)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.textInput.setFont(font)
        self.textInput.setObjectName("textInput")
        self.mainLayout.addWidget(self.textInput)
        self.resultLabel = QtWidgets.QLabel(RegexIt)
        font = QtGui.QFont()
        font.setBold(True)
        self.resultLabel.setFont(font)
        self.resultLabel.setObjectName("resultLabel")
        self.mainLayout.addWidget(self.resultLabel)
        self.resultOutput = QtWidgets.QPlainTextEdit(RegexIt)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.resultOutput.setFont(font)
        self.resultOutput.setReadOnly(True)
        self.resultOutput.setObjectName("resultOutput")
        self.mainLayout.addWidget(self.resultOutput)

        self.retranslateUi(RegexIt)
        QtCore.QMetaObject.connectSlotsByName(RegexIt)

        self.regexInput.textChanged.connect(self.update)
        self.textInput.textChanged.connect(self.update)

    def retranslateUi(self, RegexIt):
        _translate = QtCore.QCoreApplication.translate
        RegexIt.setWindowTitle(_translate("RegexIt", "RegexIt — Regex Tester"))
        self.regexLabel.setText(_translate("RegexIt", "Regex Pattern"))
        self.regexInput.setPlaceholderText(_translate("RegexIt", "Enter your regular expression, e.g. ^\\d{3}-\\d{4}$"))
        self.textLabel.setText(_translate("RegexIt", "Test String"))
        self.textInput.setPlaceholderText(
            _translate("RegexIt", "Paste or type the text you want to test the pattern against..."))
        self.resultLabel.setText(_translate("RegexIt", "Result"))
        self.resultOutput.setPlaceholderText(_translate("RegexIt", "Matches will appear here..."))

    def update(self):
        if not self.regexInput.text():
            return
        try:
            match = re.findall(self.regexInput.text(), self.textInput.toPlainText())

            if match:
                self.resultOutput.setPlainText(", ".join(match))
            else:
                self.resultOutput.setPlainText("No match found.")

        except re.error as e:
            self.resultOutput.setPlainText(f"Invalid regex:\n{e}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = RegexItUI(window)
    window.show()
    sys.exit(app.exec_())
