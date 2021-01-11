# import main
import PilihanMenu 
# from sqlite3.dbapi2 import Cursor

class User(PilihanMenu.Menuu):
    coba = 0
    def getUser(self):
        self.query = "SELECT * FROM Login"
        userID = self.execute(self.query,True)
        for i in userID:
            print(i)

    def CekDatabase(self, email, passwd):
        self.query= " select * from Login WHERE Email=\'%s\' and Pasword=\'%s\'"
        self.query = self.query % (email,passwd)
        hasil  = self.execute(self.query)
        # while self.coba < 4:
        #     self.coba = self.coba + 1
        if hasil == None : 
            print("Maaf email / password anda salah atau belum terdaftar")
            return False
        else:
            print("Selamat Datang")
            self.menu()
            return True
            

user1 = User()
user1.CekDatabase(input("masukan email :"),input("masukkan passowd :"))
