from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QPushButton,QStackedWidget,QLabel,QLineEdit,QDialog,QScrollArea,QVBoxLayout,QHBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap,QIcon, QFont
from PyQt5.QtGui import QFontDatabase as QFontDB, QFont
from PyQt5.QtCore import Qt,QRect
import Database

class MainUi:
    def __init__(self):
        #메인윈도우 생성
        self.mainWindow = QMainWindow()
        self.mainWindow.resize(1600,900)
        self.mainWindow.setStyleSheet("background-color:#f2f2f2;")#기본 회색

        #메인위젯 생성
        self.centralWidget = QWidget(self.mainWindow)
        self.centralWidget.setStyleSheet("background-color:#f2f2f2;")

        #스택 생성
        self.stackedWidget = QStackedWidget(self.mainWindow)
        self.stackedWidget.setGeometry(0,0,1600,900)
        self.stackedWidget.setMaximumSize(1600,900)







        ##############################################################로그인페이지 생성
        self.loginPage = QWidget()
        self.loginPageList = []
        #MyTube 라벨 추가
        self.loginPageList.append(self.makeLabel(self.loginPage,800,300,100,50,"MyTube","color:#222222;"))
        #아이디입력, 비밀번호 입력   returnPressed 나중에 사용할 것 같은데, 입력 다하고 엔터만 눌러도 확인버튼누르는 거랑 같은 효과 
        textList = ["아이디 입력","비밀번호 입력"]
        y = 380
        for i in range(0,2):
            self.loginPageList.append(self.makeLineEdit(self.loginPage,650,y+i*40,300,30,textList[i],"background-color:#797979; color:#ffffff; border-radius: 5px;"))
        #밑에 ID/PW 찾기,회원가입, 로그인버튼 사이에 파이프라인
        self.loginPageList.append(self.makeLabel(self.loginPage,800,460,10,20,"|",""))
        #ID/PW 찾기,회원가입, 로그인버튼
        x = 700
        textList = ["ID/PW 찾기","회원가입","LOGIN"]
        for i in range(0,3):
            self.loginPageList.append(self.makePushbtn(self.loginPage,x+i*120,460,80,20,textList[i],"background-color:#f2f2f2; color:#222222; border-radius: 5px;"))
        #login버튼 위치랑 스타일 재설정
        self.loginPageList[6].setGeometry(750,550,100,50)
        self.loginPageList[6].setStyleSheet("background-color:#ff0000; color:#222222; border-radius: 25px;")
        #스택에 로그인페이지 추가
        self.stackedWidget.addWidget(self.loginPage)#0번
        #############################################################################







        #######################################################################################회원가입 페이지 생성
        self.SignPage = QWidget()
        self.SignPageList = []
        labelTextList = ["ID","PW","","이름","연락처"]
        lineEditTextList = ["아이디 입력","비밀번호 입력","비밀번호 확인","이름 입력","000-0000-0000"]
        y = 250
        for i in range(0,5):
            #입력내용 표시 라벨
            self.SignPageList.append(self.makeLabel(self.SignPage,600,y+i*70,50,20,labelTextList[i],"background-color:#f2f2f2; color: #222222;"))
            #입력값 받는 lineEdit
            self.SignPageList.append(self.makeLineEdit(self.SignPage,660,y+i*70,300,30,lineEditTextList[i],"background-color:#797979; color:#ffffff; border-radius: 5px;"))
            #경고문구 출력 부분
            self.SignPageList.append(self.makeLabel(self.SignPage,660,y+35+i*70,300,20,"경고문구를 출력","background-color:#f2f2f2; color: #f2f2f2;"))
        #중복체크 버튼
        self.SignPageList.append(self.makePushbtn(self.SignPage,970,y,80,20,"✔중복 체크","background-color:#f2f2f2; color:#222222; border-radius: 5px;"))
        #signup 버튼
        self.SignPageList.append(self.makePushbtn(self.SignPage,750,650,100,50,"SIGN UP","background-color:#ff0000; color:#222222; border-radius: 25px;"))
        #모든 칸을 입력하지 않았을때의 경고문구
        self.SignPageList.append(self.makeLabel(self.SignPage,700,750,230,20,"⚠ 모든 칸을 입력해 주세요 ⚠","background-color:#f2f2f2; color: #f2f2f2;"))
        #로그인페이지로 되돌아가는 버튼
        self.SignPageList.append(self.makePushbtn(self.SignPage,700,650,50,50,"↩","background-color:#f2f2f2; color:#222222; border-radius: 5px;"))
        #스택에 회원가입페이지 추가
        self.stackedWidget.addWidget(self.SignPage)#1번
        #######################################################################################







        ########################################################################################아이디/비밀번호 찾기 페이지
        self.FindPage = QWidget()
        self.FindPageList = []
        titleList = [">아이디 찾기<",">비밀번호 찾기<"]
        findTextList = ["이름","연락처"]
        findTextLineEditList = ["이름 입력","000-0000-0000"]

        for i0 in range(0,2):#0~3
            #>아이디 찾기< >비밀번호 찾기< 라벨
            self.FindPageList.append(self.makeLabel(self.FindPage,740,200+i0*280,120,40,titleList[i0],"background-color:#f2f2f2; color: #222222;"))
            #모든칸을 채우지 않았을 경우의 경고문구
            self.FindPageList.append(self.makeLabel(self.FindPage,700,400+i0*400,200,40,'⚠ 모든 칸을 입력해 주세요 ⚠',"background-color:#f2f2f2; color: #f2f2f2;"))
        for i in range(0,2):#
            for i2 in range(0,2):
                #입력내용 표시 라벨
                self.FindPageList.append(self.makeLabel(self.FindPage,600,y+i*70+i2*350,50,20,findTextList[i],"background-color:#f2f2f2; color: #222222;"))
                #입력값 받는 lineEdit
                self.FindPageList.append(self.makeLineEdit(self.FindPage,660,y+i*70+i2*350,300,30,findTextLineEditList[i],"background-color:#797979; color:#ffffff; border-radius: 5px;"))
                #ID/Pw 찾기 확인 버튼
                if i == 1:
                    self.FindPageList.append(self.makePushbtn(self.FindPage,990,y+i*70+i2*350,50,30,"확인","background-color:#ff0000; color:#222222; border-radius: 5px;"))
                #경고문구 출력 부분
                self.FindPageList.append(self.makeLabel(self.FindPage,660,y+35+i*70+i2*350,300,20,"20글자 이내로 입력해주세요","background-color:#f2f2f2; color: #f2f2f2;"))
        #비밀번호 찾기에 id입력 QlineEdit
        #입력내용 표시 라벨
        self.FindPageList.append(self.makeLabel(self.FindPage,600,525,50,20,"ID","background-color:#f2f2f2; color: #222222;"))
        #입력값 받는 lineEdit
        self.FindPageList.append(self.makeLineEdit(self.FindPage,660,525,300,30,"아이디 입력","background-color:#797979; color:#ffffff; border-radius: 5px;"))
        #로그인페이지로 되돌아가는 버튼
        self.FindPageList.append(self.makePushbtn(self.FindPage,775,750,50,50,"↩","background-color:#f2f2f2; color:#222222; border-radius: 5px;"))
        #경고문구 출력 부분
        self.FindPageList.append(self.makeLabel(self.FindPage,660,560,300,20,"20글자 이내로 입력해주세요","background-color:#f2f2f2; color: #f2f2f2;"))
        #스택에 찾기페이지 추가
        self.stackedWidget.addWidget(self.FindPage)#2번
         ##############################################################################







        ###############################################################################재생목록 페이지 생성    
        # scrollaread <- widget <- layout
        # 위젯을 하나 만들어서 scroll영역 안에 넣어주고, 요소들을 넣을위젯을 하나 더 만들어서 레이아웃 안에 넣어주고 
        self.PlayPage = QWidget()

        self.PlayPageList = []
        self.PlayPageList.append(self.makePushbtn(self.PlayPage,80,100,100,30,"재생목록 추가","background-color:#ff0000; color:#222222; border-radius: 5px;"))
        for i in range(0,100):
            self.PlayPageList.append(self.makeLabel(self.PlayPage,80,150+i*40,1000,30,"재생목록 내용"+str(i+1),"background-color:#797979; color:#ffffff; border-radius: 5px;"))
            self.PlayPageList.append(self.makePushbtn(self.PlayPage,1095,150+i*40,50,30,"삭제","background-color:#ff0000; color:#222222; border-radius: 5px;"))
            self.PlayPageList.append(self.makePushbtn(self.PlayPage,1150,150+i*40,50,30,"수정","background-color:#ff0000; color:#222222; border-radius: 5px;"))

        #레이아웃 생성
        self.playLayout = QFormLayout()
        #레이아웃에 버튼, 라벨 요소 추가
        for i2 in range(0,100): 
            self.playLayout.addRow("Name", self.PlayPageList[i])

        #위젯 안에 레이아웃이 세팅됨
        self.PlayPage.setLayout(self.playLayout)
        #스크롤에리아 안에 현재 재생페이지를 세팅함
        self.scroll = QScrollArea()
        self.scroll.setGeometry(QRect(0,200,1600,700))
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidget(self.PlayPage)
        self.scroll.setWidgetResizable(True)
      

  

        # self.scroll=QScrollArea(self.PlayPage)                 # QScrollArea 생성
        # self.scroll.setGeometry(0,200,1600,700)                        # 위치 지정
        # self.scroll.setWidget(self.PlayPageList)                          
        # self.scroll.setWidgetResizable(True)




        #스택에 재생목록 페이지 추가
        self.stackedWidget.addWidget(self.PlayPage)#2번
        ################################################################################
        #ui파일 생성자 맨 아랫줄에 들어가야 하는 두줄
        self.mainWindow.setCentralWidget(self.centralWidget)
        self.mainWindow.show()






    def makeLabel(self,page,x,y,xsize,ysize,text,style):
        label = QLabel(page)
        label.setGeometry(x,y,xsize,ysize)
        label.setText(text)
        label.setStyleSheet(style)
        return label

    def makeLineEdit(self,page,x,y,xsize,ysize,text,style):
        lineEdit = QLineEdit(page)
        lineEdit.setGeometry(x,y,xsize,ysize)
        lineEdit.setStyleSheet(style)
        lineEdit.setText(text)
        return lineEdit

    def makePushbtn(self,page,x,y,xsize,ysize,text,style):
        loginbtn = QPushButton(page)
        loginbtn.setGeometry(x,y,xsize,ysize)
        loginbtn.setStyleSheet(style)
        loginbtn.setText(text)
        return loginbtn



    #페이지 넘김 함수
    def enterLogin(self):
        self.stackedWidget.setCurrentIndex(0)

    def enterSignup(self):
        self.stackedWidget.setCurrentIndex(1)

    def enterFind(self):
        self.stackedWidget.setCurrentIndex(2)

    def enterPlaylist(self):
        self.stackedWidget.setCurrentIndex(3)



    ######################################################################다이얼로그 생성 함수################################
    #문구 하나만 띄우는 알림창 생성 함수
    def makeDia(self,diaName,text):
        #다이얼로그 생성
        self.diaBackground(diaName,500,250)
        #다이얼로그의 문구
        self.label = self.makeLabel(self.dialog,50,50,400,70,text,"")

        self.dialog.show()


    #재생목록 추가, 수정 버튼 클릭시 나오는 다이얼로그
    def addFix(self,event,diaName,text,btnText):
        #다이얼로그 생성
        self.diaBackground(diaName,500,250)
        #다이얼로그의 입력칸
        self.lineEdit = self.makeLineEdit(self.dialog,50,60,400,25,text,"background-color:#797979; color:#ffffff; border-radius: 5px;")
        #다이얼로그의 경고문구
        self.numerror = self.makeLabel(self.dialog,50,90,300,20,"30글자 이내로 입력해 주세요","background-color:#f2f2f2; color:#222222;")
        self.allerror = self.makeLabel(self.dialog,150,140,200,20,"⚠ 모든 칸을 입력해 주세요","background-color:#f2f2f2; color:#222222;")
        #다이얼로그의 버튼
        self.btn = self.makePushbtn(self.dialog,225,170,50,25,btnText,"background-color:#ff0000; color:#222222; border-radius: 10px;")

        self.dialog.show()


    #playlist페이지에서 삭제버튼 누르면 나오는 다이얼로그
    def remove(self,event,diaName):
        #다이얼로그 생성
        self.diaBackground(diaName,300,150)
        #다이얼로그의 문구
        self.label = self.makeLabel(self.dialog,50,50,400,20,"정말 삭제하시겠습니까?","")
        #삭제 Y/N 버튼
        self.Ybtn = self.makePushbtn(self.dialog,130,100,20,20,"Y","background-color:#f2f2f2; color:#222222;")
        self.Xbtn = self.makePushbtn(self.dialog,150,100,20,20,"N","background-color:#f2f2f2; color:#222222;")


        self.dialog.show()
        
    #다이얼로그의 기본 백그라운드 생성함수
    def diaBackground(self,diaName,x,y):
        #다이얼로그 생성
        self.dialog = QDialog()
        self.dialog.setStyleSheet("background-color:#f2f2f2; color:#222222")
        self.dialog.setWindowTitle(diaName)
        self.dialog.setWindowModality(Qt.NonModal)
        self.dialog.resize(x,y)
    ###################################################################################################################3





# # importing pafy
# import pafy 
    
# # url of playlist
# url = "https://www.youtube.com / playlist?list = PLqM7alHXFySGqCvcwfqqMrteqWukz9ZoE"
  
# # getting playlist
# playlist = pafy.get_playlist(url)
  
# # getting playlist items
# items = playlist["items"]
  
# # selecting single item
# item = items[1]

# # getting pafy object
# i_pafy = item['pafy']
      
# # getting meta data
# metadata = item['playlist_meta']

# # checking if it is CC
# value = metadata['is_cc']
  
# # printing value
# print(value)