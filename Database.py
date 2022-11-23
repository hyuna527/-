import sqlite3


class Database:
    def __init__(self):
        self.connect = sqlite3.connect("database.db")
        self.cursor = self.connect.cursor()
        self.result = None

        self.initUserTabe()

    #테이블 처음 생성
    def initUserTabe(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS member (seq INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, pw TEXT, name TEXT, phone TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS video (seq INTEGER PRIMARY KEY AUTOINCREMENT, fk INTEGER, url TEXT, \
            FOREIGN KEY('fk') REFERENCES member(seq))")
        self.connect.commit()


    #Read 조건 O
    def readTable(self,column,tablename,condition,conditioninput):
        read = "SELECT "+column[0]+" FROM "+str(tablename)+" WHERE "+str(condition[0])+"=?"
        for i in range(1,len(condition)):
            read = read+" AND "+str(condition[i])+"=?"
        self.cursor.execute(read,conditioninput)
        data = self.cursor.fetchall()
        return data

    #Read 조건 X
    def read(self,column,tablename):
        read = "SELECT "+column[0]+" FROM "+str(tablename)
        self.cursor.execute(read)
        data = self.cursor.fetchall()
        return data


    #Create self.cursor.execute("INSERT INTO member(id,pw) VALUES(?,?) [hi,1234]")리스트 넣어준다
    def create(self,tablename,columnname,input):
        create = "INSERT INTO "+tablename+"("+str(columnname[0])
        for i in range(1,len(columnname)):
            create = create+", "+str(columnname[i])
        create = create+") VALUES(?"
        for i in range(1,len(columnname)):
            create = create+",?"
        create = create+")"

        
        self.cursor.execute(create,input)
        self.connect.commit()#커밋으로 연결 해주고


    #UPDATE self.cursor.execute("UPDATE member SET id=aplle WHERE id=hi")
    def update(self,tablename,columnchange,change,changepointname,changepoint):
        update = "UPDATE "+tablename+" SET "+columnchange+"="+str(change)+" WHERE "+changepointname+"="+str(changepoint)

        self.cursor.execute(update)
        self.connect.commit()


    #DELETE self.cursor.execute("DELETE FROM member WHERE seq=? [1]") 
    #현재 seq로만 delete이 가능한 상태
    def delete(self,seq):
        self.cursor.execute("DELETE FROM player WHERE seq=?",[seq])
        self.connect.commit()