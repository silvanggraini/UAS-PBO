# import main
import PilihanMenu 
# from sqlite3.dbapi2 import Cursor

class users(PilihanMenu.Menuu):
    def getUser(self):
        self.query = "SELECT * FROM Login"
        userID = self.execute(self.query,True)
        for i in userID:
            print(i)

    def cekDatabase(self, email, passwd):
        self.query= " select * from Login WHERE Email=\'%s\' and Pasword=\'%s\'"
        self.query = self.query % (email,passwd)
        hasil  = self.execute(self.query)
        if hasil == None :
            print("Maaf email anda belum terdaftar")
            return False
        else:
            print("Selamat Datang")
            self.menu()
            return True

user1 = users()
user1.cekDatabase(input("masukan email :"),input("masukkan passowd :"))
