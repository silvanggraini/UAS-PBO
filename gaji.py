import main

class gajiKaryawan(main.inti):
    jumlahGaji = 0
    def gaji(self):
        self.tanggalGajian = input("Masukan tanggal :")
        self.id_karyawan = int(input("Masukan id karyawan :"))
        self.jumlahGaji = int(input("Masukan gaji :"))

        # self.query = '''INSERT INTO Karyawan (tanggalGaji, id_karyawan, gaji) VALUES (\'%s\',\'%d\',\'%d\');'''
        # self.query = self.query % (self.tanggalGajian, self.id_karyawan, self.jumlahGaji)
        # self.execute(self.query)

        self.query = '''INSERT INTO gaji (tanggal, id_karyawan, gaji) VALUES (\'%s\',\'%d\',\'%d\');'''
        self.query = self.query % (self.tanggalGajian, self.id_karyawan, self.jumlahGaji)
        self.execute(self.query)

    def getGaji(self):
        self.query = 'SELECT SUM(gaji) from gaji '
        self.cursor.execute(self.query)
        self.jumlahGaji = self.cursor.fetchall()
        return self.jumlahGaji[0][0]