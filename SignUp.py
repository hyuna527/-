import Database

class SignUp():
    def __init__(self,ui):
        self.ui = ui
        self.db = Database.Database()

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