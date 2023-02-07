import sys
from PyQt5.QtWidgets import QWidget, QTextEdit, QApplication, QPushButton, QLineEdit
from PyQt5 import QtGui
import string
import random
import time
import pyperclip





global dictmapA2B
global dictmapB2A
global plan
global allsymbols_shuffleA
global allsymbols_shuffleB
global allsymbols
global seedA
plan="encrypt"


allsymbols=[]
seedA=1948213
for i in range(3000):
    allsymbols.append(chr(i))
allsymbols_shuffleA=allsymbols.copy()
random.seed(seedA)
random.shuffle(allsymbols_shuffleA)
random.seed()




seedB = 487

allsymbols_shuffleB=allsymbols.copy()
random.seed(seedB)
random.shuffle(allsymbols_shuffleB)
random.seed()



dictmapA2B=dict()
dictmapB2A=dict()

for cc in range(len(allsymbols_shuffleA)):
    dictmapA2B[allsymbols_shuffleA[cc]]=allsymbols_shuffleB[cc]

for cc in range(len(allsymbols_shuffleB)):
    dictmapB2A[allsymbols_shuffleB[cc]]=allsymbols_shuffleA[cc]








def showondisplay():
    global dictmapA2B
    global dictmapB2A
    global plan
    global allsymbols_shuffleA
    global allsymbols_shuffleB
    global allsymbols
    global seedA

    
    freshlyentered = entertext.toPlainText()
    text = freshlyentered

    newtext=''
    if plan=='decrypt':
        for count in range(len(text)):
            newtext += dictmapB2A[text[count]]
    else:
        for count in range(len(text)):
            newtext += dictmapA2B[text[count]]
            
    processedfreshentery=newtext
    displaytext.setText(processedfreshentery)


def decrypt_plan():
    
    print('decrypting')
    global plan
    plan='decrypt'
    decryptpushbutton.setStyleSheet("background-color:green")
    encryptpushbutton.setStyleSheet("background-color:grey")


def encrypt_plan():
    
    print('encrypting')
    global plan
    plan='encrypt'
    decryptpushbutton.setStyleSheet("background-color:grey")
    encryptpushbutton.setStyleSheet("background-color:green")

def allowkeyedit():
    keykeykey.setReadOnly(False)


def updatekey():
    global dictmapA2B
    global dictmapB2A
    global allsymbols_shuffleA
    global allsymbols_shuffleB
    global allsymbols
    global seedA
    global seedBB
    key = keykeykey.setReadOnly(False)
    seedBB=keykeykey.text()
    keykeykey.setPlaceholderText("*****hidden******")
    keykeykey.clear()
    keykeykey.setReadOnly(True)

    #seedB = 487
    seedB = 0
    for cc in range(len(allsymbols_shuffleA)):
        if allsymbols_shuffleA[cc] in seedBB:
            seedB += int(1.62*cc + 0.3 * cc**2)

    allsymbols_shuffleB=allsymbols.copy()
    random.seed(seedB)
    random.shuffle(allsymbols_shuffleB)
    random.seed()



    dictmapA2B=dict()
    dictmapB2A=dict()

    for cc in range(len(allsymbols_shuffleA)):
        dictmapA2B[allsymbols_shuffleA[cc]]=allsymbols_shuffleB[cc]

    for cc in range(len(allsymbols_shuffleB)):
        dictmapB2A[allsymbols_shuffleB[cc]]=allsymbols_shuffleA[cc]

    showondisplay()


def randomkeyonstartup():
    global dictmapA2B
    global dictmapB2A
    global allsymbols_shuffleA
    global allsymbols_shuffleB
    global allsymbols
    global seedA
    global seedBB




    randystring = str(''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=8)))
    seedBB=randystring
    keykeykey.setPlaceholderText("*****hidden******")
    keykeykey.clear()
    keykeykey.setReadOnly(True)

    #seedB = 487
    seedB = 0
    for cc in range(len(allsymbols_shuffleA)):
        if allsymbols_shuffleA[cc] in seedBB:
            seedB += int(1.62*cc + 0.3 * cc**2)

    allsymbols_shuffleB=allsymbols.copy()
    random.seed(seedB)
    random.shuffle(allsymbols_shuffleB)
    random.seed()



    dictmapA2B=dict()
    dictmapB2A=dict()

    for cc in range(len(allsymbols_shuffleA)):
        dictmapA2B[allsymbols_shuffleA[cc]]=allsymbols_shuffleB[cc]

    for cc in range(len(allsymbols_shuffleB)):
        dictmapB2A[allsymbols_shuffleB[cc]]=allsymbols_shuffleA[cc]

    showondisplay()
    
def copykey():
    global seedBB
    
    pyperclip.copy(seedBB)
    

if __name__=="__main__":
    app=QApplication(sys.argv)
    w=QWidget()
    w.resize(900,900)
    w.setWindowTitle('bojuAI')

    displaytext = QTextEdit(w)
    displaytext.resize(800,450)
    displaytext.move(50,50)
    displaytext.setReadOnly(True)
    displaytext.setStyleSheet("background-color: black; color: white")
    #displaytext.setPlaceholderText("Do not type here")
    
##    displaytext.font().setPointSize(55) 
##    displaytext.setFont(displaytext.font())

    font = QtGui.QFont()
    font.setPointSize(20)
    displaytext.setFont(font)



    entertext = QTextEdit(w)
    entertext.resize(800,300)
    entertext.move(50,550)
    entertext.setReadOnly(False)
    entertext.setStyleSheet("background-color: white; color: black")
    entertext.setPlaceholderText("Enter text here")
    entertext.textChanged.connect(showondisplay)
    ##call a function named showondisplay which simply pulls the content
    #from entertext and makes it the content on displaytext
    entertext.setFont(font)

    encryptpushbutton = QPushButton(w)
    encryptpushbutton.setText("ENCRYPT")
    encryptpushbutton.move(50,500)
    encryptpushbutton.resize(100,50)
    encryptpushbutton.clicked.connect(encrypt_plan)
    
    encryptpushbutton.setStyleSheet("background-color: green")
    

    decryptpushbutton = QPushButton(w)
    decryptpushbutton.setText("DECRYPT")
    decryptpushbutton.move(200,500)
    decryptpushbutton.resize(100,50)
    decryptpushbutton.clicked.connect(decrypt_plan)
    decryptpushbutton.setStyleSheet("background-color: grey")


    keykeykey = QLineEdit(w)
    keykeykey.setEchoMode(QLineEdit.Password)
    keykeykey.setStyleSheet('lineedit-password-character: 9679')
    keykeykey.resize(200,50)
    keykeykey.move(400,500)
    keykeykey.setReadOnly(True)
    #keykeykey.setStyleSheet("background-color: white; color: black")
    keykeykey.setPlaceholderText("Enter a Secret Key")
    keykeykey.returnPressed.connect(updatekey)


    keyeditbutton = QPushButton(w)
    keyeditbutton.setText("EDIT")
    keyeditbutton.move(600,500)
    keyeditbutton.resize(100,50)
    keyeditbutton.clicked.connect(allowkeyedit)
    keyeditbutton.setStyleSheet("background-color: grey")


    showkeybrieflybutton = QPushButton(w)
    showkeybrieflybutton.setText("Copy Key")
    showkeybrieflybutton.move(700,500)
    showkeybrieflybutton.resize(100,50)
    showkeybrieflybutton.clicked.connect(copykey)
    showkeybrieflybutton.setStyleSheet("background-color: grey")
    

    randomkeyonstartup()


    w.show()
    sys.exit(app.exec())
