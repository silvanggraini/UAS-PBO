# import transaksiPembelian
import Pembelian
import Penjualan
import gaji
# import main 
# import main 

class Laporan( gaji.GajiKaryawan,Penjualan.TransaksiPenjualan,Pembelian.TransaksiPembelian):
    def laporanTransaksi(self):
        self.keuntungan = self.getTotalTP() - (self.getTotalTB() + self.getGaji())
        print(self.keuntungan)
        
        self.query = '''INSERT INTO laporanPenjualan (totalGajiKaryawan, totalPenjualan, totalPembelian, keuntungan) 
        VALUES (\'%d\',\'%d\',\'%d\',\'%d\');'''
        self.query = self.query % (self.getGaji(), self.getTotalTP(), self.getTotalTB(), self.keuntungan)
        self.execute(self.query)
       