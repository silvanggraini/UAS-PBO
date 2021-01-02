# import sqlite3
# from connect import connect
import main

class stokBarang(main.inti):
    def tampilDataStokBarang(self):
        query = 'SELECT * from stokBarangHijab'
        tampil = self.execute(query,True)
        for row in tampil:
            print(row)

class karyawan(main.inti):
    def tampilDataKaryawan(self):
        query = 'SELECT * from Karyawan'
        tampil = self.execute(query,True)
        for row in tampil:
            print(row)

class pelanggan(main.inti):
    def tampilDataPelanggan(self):
        query = 'SELECT * from pelanggan'
        tampil = self.execute(query,True)
        for row in tampil:
            print(row)

class transaksiJual(main.inti):
    def tampilDataPenjualan(self):
        query = 'SELECT * from transaksiPenjualan'
        tampil = self.execute(query,True)
        for row in tampil:
            print(row)

class transaksiBeli(main.inti):
    def tampilDataPembelian(self):
        query = 'SELECT * from transaksiPembelian'
        tampil = self.execute(query,True)
        for row in tampil:
            print(row)

class laporanJualBeli(main.inti):
    def tampilDataLaporan(self):
        query = 'SELECT * from laporanPenjualan'
        tampil = self.execute(query,True)
        for row in tampil:
            print(row)

# user1 = stokBarang()
# user1.tampilDataStokBarang()