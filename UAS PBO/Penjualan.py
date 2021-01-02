import TampilHijab

class transaksiPenjualan(TampilHijab.stokBarang):
    totalTP = 0
    def penjualan(self):
        print("Silahkan mau belanja apa")
        print(f'{"No"} \t{"Jenis Barang"} \t{"Nama Barang"} \t {"Harga Barang"} \t {"Stok Barang"}')
        print('-'*75)
        self.tampilDataStokBarang()
        self.jenisBarangJual = input("Masukan jenis barang? ")
        if self.jenisBarangJual == "Pashmina":
            self.namaBarang = input("Apa nama barang yang dicari? ")
            self.jumlahBarangJual = int(input("Berapa banyak yang dibeli?(dalam satuan helai)"))
            if self.namaBarang == "Ceruty":
                self.totalTP = self.jumlahBarangJual * 25000 
            else:
                self.totalTP = self.jumlahBarangJual * 35000 
        elif self.jenisBarangJual == "Segiempat":
            self.namaBarang = input("Apa nama barang yang dicari?")
            self.jumlahBarangJual = int(input("Berapa banyak yang dibeli?(dalam satuan helai)"))
            if self.namaBarang == "Bella Squere":
                self.totalTP = self.jumlahBarangJual * 25000 
            else:
                self.totalTP = self.jumlahBarangJual * 30000 
        else:
            self.namaBarang = input("Apa nama barang yang dicari?")
            self.jumlahBarangJual = int(input("Berapa banyak yang dibeli?(dalam satuan helai)"))
            if self.namaBarang == "KCB Tali":
                self.totalTP = self.jumlahBarangJual * 50000 
            elif self.namaBarang == "Renda":
                self.totalTP = self.jumlahBarangJual * 45000 
            else:
                self.totalTP = self.jumlahBarangJual * 45000 

        self.tanggalPenjualan = input("Masukan tanggal :")
        self.idPelanggan = int(input("Masukan id pelanggan :"))

        self.query = '''INSERT INTO transaksiPenjualan (tanggalPenjualan, id_pelanggan ,jenisBarang, jumlahBarang, totalPenjualan) 
        VALUES (\'%s\',\'%d\',\'%s\',\'%d\',\'%d\');'''
        self.query = self.query % (self.tanggalPenjualan, self.idPelanggan, self.jenisBarangJual, self.jumlahBarangJual, self.totalTP)
        self.execute(self.query)

    def getTotalTP(self):
        self.query = 'SELECT SUM(totalPenjualan) from transaksiPenjualan '
        self.cursor.execute(self.query)
        self.totalTP = self.cursor.fetchall()
        return self.totalTP[0][0]

        


        
