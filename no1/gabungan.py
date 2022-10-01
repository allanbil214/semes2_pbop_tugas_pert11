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



class Celana:
    def __init__(self, merk, warna, ukuran):
        self.merk = merk
        self.warna = warna
        self.ukuran = ukuran

class Jenis_Celana(Celana):
    def __init__(self, merk, warna, ukuran, nama_jenis):
        super().__init__(merk, warna, ukuran)
        self .nama_jenis = nama_jenis

class Jeans(Jenis_Celana):
    def __init__(self, merk, warna, ukuran, tekstur, jml_dekorasi):
        super().__init__(merk, warna, ukuran, nama_jenis="Jeans")
        self.tekstur = tekstur
        self.jml_dekorasi = jml_dekorasi

class Casual(Jenis_Celana):
    def __init__(self, merk, warna, ukuran, lebar, jenis_kain):
        super().__init__(merk, warna, ukuran, nama_jenis="Casual")
        self.lebar = lebar
        self.jenis_kain = jenis_kain



class Pakaian:
    def __init__(self, baju:Baju, celana:Celana):
        self.baju = baju
        self.celana = celana

zuckerberg = Pakaian(
    baju=Tank_Top(
        ukuran="L",
        warna="Hitam",
        merk="Rider",
        jenis_kain="Katun"
    ),
    celana=Jeans(
        merk="Watchout",
        warna="Biru Dongker",
        ukuran="L",
        tekstur="Kasar",
        jml_dekorasi=5
    )
)

bill = Pakaian(
    baju=Tuxedo(
        "XL", "Coklat",
        "Havana", 47.2, 
        200_000_000, 2
    ),
    celana=Casual(
        "Hockerty", "Hitam",
        "XL", 60, "Bologna"
    )
)