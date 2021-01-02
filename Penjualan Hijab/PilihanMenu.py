# import Pembelian, Pembelian.transaksiPembelian,  Penjualan.transaksiPenjualan,TampilHijab.transaksiJual
import TampilHijab
import gaji
# import Penjualan
import PK
import laporan

class Menuu( TampilHijab.transaksiJual, TampilHijab.transaksiBeli, TampilHijab.karyawan
            ,PK.karyawan, PK.pelanggan, TampilHijab.pelanggan, laporan.laporan, gaji.gajiKaryawan):
    def menu(self):
        while True:
            print("menu \n1. Transaksi Penjualan \n2. Transaksi Pembelian \n3. Data Karyawan \n4. Gaji karyawan \n5. Data Pelanggan \n6. Laporan Penjualan \n7. Keluar")
            self.pilihan = int(input("Masukan pilihan :"))
            if self.pilihan == 1:
                self.pembelian()
                self.tampilBeli = input("Apakah Anda ingin menampilkan data pembelian ? ")
                if self.tampilBeli == "Ya":
                    self.tampilDataPembelian()
                else:
                    pass
            elif self.pilihan == 2:
                self.penjualan()
                self.tampilJual = input("Apakah Anda ingin menampilkan data penjualan ? ")
                if self.tampilJual == "Ya":
                    self.tampilDataPenjualan()
                else:
                    pass
            elif self.pilihan == 3:
                self.inputKaryawan()
                self.tampilKaryawan = input("Apakah anda ingin menampilkan data karyawan? ")
                if self.tampilKaryawan == "Ya":
                    self.tampilDataKaryawan()
                else:
                    pass
            elif self.pilihan == 4:
                self.gaji()
                # self.tampilDatapelanggan = input("Apakah anda ingin menampilkan data pelanggan? ")
                # if self.tampilDatapelanggan == "Ya":
                #     self.tampilDataPelanggan()
                # else:
                #     pass
            elif self.pilihan == 5:
                self.inputPelanggan()
                self.tampilDatapelanggan = input("Apakah anda ingin menampilkan data pelanggan? ")
                if self.tampilDatapelanggan == "Ya":
                    self.tampilDataPelanggan()
                else:
                    pass
            elif self.pilihan == 6:
                self.laporanTransaksi()
                self.tampilLaporan= input("Apakah anda ingin menampilkan data Laporan? ")
                if self.tampilLaporan == "Ya":
                    self.laporanTransaksi()
                else:
                    pass
            else:
                self.con.close()
                exit()

            