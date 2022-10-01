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