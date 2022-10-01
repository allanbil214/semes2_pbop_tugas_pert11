from Celana import Casual, Celana, Jeans
from Baju import Baju, Tank_Top, Tuxedo

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
