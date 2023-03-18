import Database

class Find():
    def __init__(self,ui):
        self.ui = ui
        self.db = Database.Database()

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