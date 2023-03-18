import Database

class Login():
    def __init__(self,ui):
        self.ui = ui
        self.db = Database.Database()

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