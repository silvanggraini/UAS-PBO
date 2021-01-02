import main

class transaksiPembelian(main.inti):
    totalTB = 0
    def pembelian(self):
        self.tanggalPembelian = str(input("Masukan tanggal pembelian :"))
        self.jenisBarang = input("Masukan jenis barang :")
        self.jumlahBarang = int(input("Masukan jumlah barang:"))
        self.hargaBarang = int(input("Masukan harga barang :"))
        self.namaToko = input("Masukan nama toko :")
        # self.noHpToko = int(input("Masukan no hp pemilik toko :")) , noHpToko ,\'%d\' self.noHpToko,
        self.totalTB = self.jumlahBarang * self.hargaBarang
        print(self.totalTB)

        self.query = '''INSERT INTO transaksiPembelian (tanggalPembelian, jenisBarang, hargaBarang, jumlahBarang, 
        total_hargaPembelian, namaToko) 
        VALUES (\'%s\',\'%s\',\'%d\',\'%d\',\'%d\',\'%s\');'''
        self.query = self.query % (self.tanggalPembelian, self.jenisBarang, self.hargaBarang, self.jumlahBarang,
        self.totalTB,self.namaToko)
        self.execute(self.query)

    def getTotalTB(self):
        self.query = 'SELECT SUM(total_HargaPembelian) from transaksiPembelian '
        self.cursor.execute(self.query)
        self.totalTB = self.cursor.fetchall()
        return self.totalTB[0][0]