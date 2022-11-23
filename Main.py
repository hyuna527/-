#이 친구는 main
import main_ui
import sys
import Database

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QPushButton,QStackedWidget,QLabel,QLineEdit,QDialog,QScrollArea,QVBoxLayout,QHBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap,QIcon, QFont
from PyQt5.QtGui import QFontDatabase as QFontDB, QFont
from PyQt5.QtCore import Qt,QRect


class Main():
    def __init__(self):
        self.ui = main_ui.MainUi()
        self.db = Database.Database()
        self.repet = 0

        #로그인 페이지 이벤트
        self.ui.loginPageList[5].clicked.connect(self.ui.enterSignup)
        self.ui.loginPageList[4].clicked.connect(self.ui.enterFind)
        #로그인 확인 누르면 로그인 함수 호출
        self.ui.loginPageList[6].clicked.connect(self.login)
        

        #회원가입 페이지 이벤트
        self.ui.SignPageList[15].clicked.connect(self.repetitionCheck)
        self.ui.SignPageList[16].clicked.connect(self.signupProcess)
        self.ui.SignPageList[18].clicked.connect(self.ui.enterLogin)
        


        #찾기 페이지 이벤트
        self.ui.FindPageList[12].clicked.connect(self.findId)
        self.ui.FindPageList[16].clicked.connect(self.findPw)
        self.ui.FindPageList[20].clicked.connect(self.ui.enterLogin)


        #재생페이지 이벤트
        self.ui.PlayPageList[0].clicked.connect(lambda event : self.ui.addFix(event,"재생목록 추가","추가할 재생목록을 입력하세요","추가"))
        self.ui.PlayPageList[2].clicked.connect(lambda event : self.ui.remove(event,"삭제 확인"))
        self.ui.PlayPageList[3].clicked.connect(lambda event : self.ui.addFix(event,"재생목록 수정","기존에 있던 재생목록 유지해서 띄우기","수정"))






################################################################회원가입 페이지 관련 함수
    def signupProcess(self):
        id = str(self.ui.SignPageList[1].text())
        pw = str(self.ui.SignPageList[4].text())
        chpw = str(self.ui.SignPageList[7].text())
        name = str(self.ui.SignPageList[10].text())
        phone = str(self.ui.SignPageList[13].text())
        check = 0
        #아이디 중복체크가 되었는지 확인
        if self.repet == 0:
            self.ui.SignPageList[2].setText("중복체크를 진행해 주세요")
            self.ui.SignPageList[2].setStyleSheet("background-color: #f2f2f2; color:#222222;")
        elif self.repet == 1:
            check +=1
            print("1:",check)
        
        #가장먼저 모든 칸이 입력되었는지 체크
        if self.checkBlank(id,pw,name,phone) == True:
            check +=1
            print("2:",check)

        #비밀번호와 비밀번호 확인이 일치하지 않으면
        if self.checkPW(pw,chpw) == True:
            check +=1
            print("3:",check)

        #가장나중에 글자수 체크
        if self.checkNum(id,pw,name,phone) == True:
            check +=1
            print("4:",check)

        if check == 4:
            self.ui.makeDia("회원가입 성공","회원가입에 성공하였습니다.")
            self.db.create("member",["id","pw","name","phone"],[id,pw,name,phone])
            self.ui.enterLogin()
        else:
            print(check)
            self.ui.makeDia("회원가입 실패","회원가입에 실패하였습니다. 입력한 내용을 다시 확인해주세요.")


    def checkPW(self,pw,chpw):
        if pw != chpw:
            self.ui.SignPageList[8].setText("비밀번호가 일치하지 않습니다.")
            self.ui.SignPageList[8].setStyleSheet("background-color:#f2f2f2; color: #222222;")
            return False
        else: 
            return True

    def checkBlank(self,id,pw,name,phone):
        #하나라도 0이면 False를 반환한다.
        if len(id) and len(pw) and len(name) and len(phone) != 0:
            self.ui.SignPageList[17].setStyleSheet("background-color:#f2f2f2; color: #f2f2f2;")
            return True
        else:
            self.ui.SignPageList[17].setStyleSheet("background-color:#f2f2f2; color: #222222;")
            return False
            
    #글자수 체크 함수, 모두 20글자 이하이면 True 를 리턴
    def checkNum(self,id,pw,name,phone):
        check = 0
        if len(id) > 20:
            self.ui.SignPageList[2].setText("20글자 이하로 입력해 주세요")
            self.ui.SignPageList[2].setStyleSheet("background-color:#f2f2f2; color: #222222;")
        else : 
            check += 1
        if len(pw) > 20:
            self.ui.SignPageList[5].setText("20글자 이하로 입력해 주세요")
            self.ui.SignPageList[5].setStyleSheet("background-color:#f2f2f2; color: #222222;")
        else : 
            check += 1
        if len(name) > 20:
            self.ui.SignPageList[11].setText("20글자 이하로 입력해 주세요")
            self.ui.SignPageList[11].setStyleSheet("background-color:#f2f2f2; color: #222222;")
        else : 
            check += 1
        if len(phone) > 20:
            self.ui.SignPageList[13].setText("20글자 이하로 입력해 주세요")
            self.ui.SignPageList[13].setStyleSheet("background-color:#f2f2f2; color: #222222;")
        else : 
            check += 1


        if check == 4:
            return True
        else:
            return False



    #아이디 중복 체크
    def repetitionCheck(self):
        id = self.ui.SignPageList[1].text()
        data = self.db.read(["id"],"member")
        if len(data) == 0:
            self.ui.SignPageList[2].setText("사용 가능한 아이디 입니다.")
            self.ui.SignPageList[2].setStyleSheet("background-color: #f2f2f2; color:#222222;")
            self.repet = 1
            return self.repet
        data = data[0]            
        if id in data:
           self.ui.SignPageList[2].setText("중복된 아이디 입니다.")
           self.ui.SignPageList[2].setStyleSheet("background-color: #f2f2f2; color:#222222;")
           self.repet = -1
           return self.repet
        else :
            self.ui.SignPageList[2].setText("사용 가능한 아이디 입니다.")
            self.ui.SignPageList[2].setStyleSheet("background-color: #f2f2f2; color:#222222;")
            self.repet = 1
            return self.repet
################################################################회원가입 페이지 관련 함수





################################################################로그인 페이지 관련 함수
    def login(self):
        id =  str(self.ui.loginPageList[1].text())
        pw = str(self.ui.loginPageList[2].text())
        idList = []

        chid = self.db.read(["id"],"member")
        for i in range(0,len(chid)):
            idList.append(chid[i][0])

        if id in idList:
            chpw = self.db.readTable(["pw"],"member",["id"],[id])[0][0]
            if pw == chpw:
                self.ui.enterPlaylist()
            else:
                self.ui.makeDia("로그인 실패","로그인에 실패하였습니다. 비밀번호를 확인해 주세요")
        else:
            self.ui.makeDia("로그인 실패","존재하지 않는 아이디입니다. 다시 확인해 주세요")
################################################################로그인 페이지 관련 함수




################################################################찾기 페이지 관련 함수
    def checkBlank(self,id,pw,name,phone):
        #하나라도 0이면 False를 반환한다.
        if len(id) and len(pw) and len(name) and len(phone) != 0:
            self.ui.SignPageList[17].setStyleSheet("background-color:#f2f2f2; color: #f2f2f2;")
            return True
        else:
            self.ui.SignPageList[17].setStyleSheet("background-color:#f2f2f2; color: #222222;")
            return False

    def findId(self):
        name = str(self.ui.FindPageList[5].text())
        phone = str(self.ui.FindPageList[11].text())
        check = 0
        ch2 = 0

        #우선 모든 칸이 입력되었는지 체크
        if len(name) ==0 or len(phone)==0:
            self.ui.FindPageList[1].setStyleSheet("background-color:#f2f2f2; color: #222222;")
        else:
            self.ui.FindPageList[1].setStyleSheet("background-color:#f2f2f2; color: #f2f2f2;")
            ch2 +=1
        #글자수를 만족시켰는지 체크
        if len(name) > 20:
            self.ui.FindPageList[6].setStyleSheet("background-color: #f2f2f2; color:#222222;")
        else:
            self.ui.FindPageList[6].setStyleSheet("background-color: #f2f2f2; color:#f2f2f2;")
            ch2 +=1
        if len(phone) > 20:
            self.ui.FindPageList[13].setStyleSheet("background-color: #f2f2f2; color:#222222;")
        else:
            self.ui.FindPageList[13].setStyleSheet("background-color: #f2f2f2; color:#f2f2f2;")
            ch2 +=1


        if ch2 == 3:
            try:
                id = self.db.readTable(["id"],"member",["name","phone"],[name,phone])[0][0]
            except IndexError:
                self.ui.makeDia("아이디찾기 실패","아이디를 찾을 수 없습니다.")
                check = 1

            if check == 0:
                self.ui.makeDia("아이디찾기 성공",name+"님의 아이디는 "+str(id)+"입니다.")

    def findPw(self):
        id = self.ui.FindPageList[19].text()
        name = str(self.ui.FindPageList[8].text())
        phone = self.ui.FindPageList[15].text()
        check = 0
        ch2 = 0


        #우선 모든 칸이 입력되었는지 체크
        if len(id) == 0 or len(name) ==0 or len(phone)==0:
            self.ui.FindPageList[3].setStyleSheet("background-color:#f2f2f2; color: #222222;")
        else:
            self.ui.FindPageList[3].setStyleSheet("background-color:#f2f2f2; color: #f2f2f2;")
            ch2 +=1
        #글자수를 만족시켰는지 체크
        if len(id) >20:
            self.ui.FindPageList[20].setStyleSheet("background-color: #f2f2f2; color:#222222;")
        else:
            self.ui.FindPageList[20].setStyleSheet("background-color: #f2f2f2; color:#f2f2f2;")
            ch2 +=1
        if len(name) > 20:
            self.ui.FindPageList[9].setStyleSheet("background-color: #f2f2f2; color:#222222;")
        else:
            self.ui.FindPageList[9].setStyleSheet("background-color: #f2f2f2; color:#f2f2f2;")
            ch2 +=1
        if len(phone) > 20:
            self.ui.FindPageList[17].setStyleSheet("background-color: #f2f2f2; color:#222222;")
        else:
            self.ui.FindPageList[17].setStyleSheet("background-color: #f2f2f2; color:#f2f2f2;")
            ch2 +=1

        
    
        if ch2 == 4:
            try:
                pw = self.db.readTable(["pw"],"member",["id","name","phone"],[id,name,phone])[0][0]
            except IndexError:
                self.ui.makeDia("비밀번호찾기 실패","비밀번호를 찾을 수 없습니다.")
                check = 1

            if check == 0:
                self.ui.makeDia("비밀번호찾기 성공",name+"님의 비밀번호는 "+str(pw)+"입니다.")
###############################################################################찾기 페이지 관련 함수
      
    








if __name__=="__main__":
    app = QApplication(sys.argv)
    main = Main()

    sys.exit(app.exec_())