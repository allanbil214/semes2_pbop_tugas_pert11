class Baju:
    def __init__(self, ukuran, warna):
        self.ukuran = ukuran
        self.warna = warna

class Lengan_Panjang(Baju):
    def __init__(self, ukuran, warna, merk, tingkat_gerah):
        super().__init__(ukuran, warna)
        self.merk = merk
        self.tingkat_gerah = tingkat_gerah

class Lengan_Pendek(Baju):
    def __init__(self, ukuran, warna, merk):
        super().__init__(ukuran, warna)
        self.merk = merk

class Tank_Top(Lengan_Pendek):
    def __init__(self, ukuran, warna, merk, jenis_kain):
        super().__init__(ukuran, warna, merk)
        self.jents_kain = jenis_kain

class Swimming_Top(Lengan_Pendek ):
    def __init__(self, ukuran, warna, merk, jenis_kelamin):
        super().__init__(ukuran, warna, merk)
        self.jents_kelamin = jenis_kelamin

class Tuxedo(Lengan_Panjang):
    def __init__(self, ukuran, warna, merk, tingkat_gerah, harga, ketebalan):
        super().__init__(ukuran, warna, merk, tingkat_gerah)
        self.harga = harga
        self.ketebalan = ketebalan

    def buka_jas(self):
        print("Jas dibuka...")

    def buka_pita(self):
        print( "Pita dibuka...")