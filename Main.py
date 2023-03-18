#이 친구는 main
import main_ui
import sys
import Database
import Login
import SignUp
import Find

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QPushButton,QStackedWidget,QLabel,QLineEdit,QDialog,QScrollArea,QVBoxLayout,QHBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap,QIcon, QFont
from PyQt5.QtGui import QFontDatabase as QFontDB, QFont
from PyQt5.QtCore import Qt,QRect


class Main():
    def __init__(self):
        self.ui = main_ui.MainUi()
        self.db = Database.Database()
        self.login = Login.Login(self.ui)
        self.signup=SignUp.SignUp(self.ui)
        self.find = Find.Find(self.ui)

        self.repet = 0

        #로그인 페이지 이벤트
        self.ui.loginPageList[5].clicked.connect(self.ui.enterSignup)
        self.ui.loginPageList[4].clicked.connect(self.ui.enterFind)
        #로그인 확인 누르면 로그인 함수 호출
        self.ui.loginPageList[6].clicked.connect(self.login.login)
        

        #회원가입 페이지 이벤트
        self.ui.SignPageList[15].clicked.connect(self.signup.repetitionCheck)
        self.ui.SignPageList[16].clicked.connect(self.signup.signupProcess)
        self.ui.SignPageList[18].clicked.connect(self.ui.enterLogin)
        


        #찾기 페이지 이벤트
        self.ui.FindPageList[12].clicked.connect(self.find.findId)
        self.ui.FindPageList[16].clicked.connect(self.find.findPw)
        self.ui.FindPageList[20].clicked.connect(self.ui.enterLogin)


        #재생페이지 이벤트
        self.ui.PlayPageList[0].clicked.connect(lambda event : self.ui.addFix(event,"재생목록 추가","추가할 재생목록을 입력하세요","추가"))
        self.ui.PlayPageList[2].clicked.connect(lambda event : self.ui.remove(event,"삭제 확인"))
        self.ui.PlayPageList[3].clicked.connect(lambda event : self.ui.addFix(event,"재생목록 수정","기존에 있던 재생목록 유지해서 띄우기","수정"))


if __name__=="__main__":
    app = QApplication(sys.argv)
    main = Main()

    sys.exit(app.exec_())