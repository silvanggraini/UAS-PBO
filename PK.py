import main

class karyawan(main.inti):
    def inputKaryawan(self):
        self.namakaryawan = input("Masukan nama:")
        self.umurKaryawan = int(input("Masukan umur:"))
        self.alamatkaryawan = input("Masukan alamat :")
        self.query = '''INSERT INTO karyawan (nama, umur, alamat) VALUES (\'%s\',\'%d\',\'%s\');'''
        self.query = self.query % (self.namakaryawan, self.umurKaryawan, self.alamatkaryawan)
        self.execute(self.query)

class pelanggan(main.inti):
    def inputPelanggan(self):
        self.namaPelanggan = input("Masukan nama pelanggan :")
        self.noHpPelanggan = input("Masukan no Hp pelanggan :")
        self.alamatPelanggan = input("Masukan alamat pelanggan :")
        self.query = '''INSERT INTO pelanggan (namaPelanggan, noHpPelanggan, alamat) VALUES (\'%s\',\'%s\',\'%s\');'''
        self.query = self.query % (self.namaPelanggan, self.noHpPelanggan, self.alamatPelanggan)
        self.execute(self.query)