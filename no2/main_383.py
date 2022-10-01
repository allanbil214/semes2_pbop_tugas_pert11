from gpu_383 import Allan_2
from cpu_383 import Allan_1

class Allan_0():
    def __init__(
            self, ram:float, 
            prosessor:Allan_1() = Allan_1(False, "", 0), 
            kartu_grafis:Allan_2() = Allan_1(False, "", 0)
        ):
        self.prosessor = prosessor
        self.kartu_grafis = kartu_grafis
        self.ram = ram

    def tampilkan_spesifikasi(self):
        print(" \n[i] Spesifikasi Komputer")
        if(self.prosessor.dipasang == True):
            print(f"CPU\t : {self.prosessor.merk} Generasi {self.prosessor.generasi}")
        if(self.kartu_grafis.dipasang == True):
            print(f"GPU\t : {self.kartu_grafis.vendor} {self.kartu_grafis.tipe}")
        print(f"RAM\t : {self.ram} MB")

    def diagnosa_sistem(self):
        print("\n===============================================================")
        print(" \n[i] Diagnosa Sistem Komputer")
        self.prosessor.print_info()
        self.kartu_grafis.print_info()
        if(self.ram > 12000):
            print("PC bisa menjalankan aplikasi apapun.")
        elif(self.ram >= 8000):
            print("PC bisa multitasking.")
        else:
            print("PC Standar, bisa menjalankan MS. Office dan Programming.")

#object kesatu
diyPC = Allan_0(ram = 2000)
diyPC.diagnosa_sistem()
diyPC.tampilkan_spesifikasi()
print("Object\t : Komputer DIY\n")

#object kedua
lttPC = Allan_0(
    ram = 64000,
    prosessor = Allan_1(
        dipasang = True, 
        merk = "AMD ThreadRipper x3560", 
        generasi = 12
        ), 
    kartu_grafis = Allan_2(
        dipasang = True,
        vendor = "NVIDIA", 
        tipe = "GeForce RTX 3090 TI"
        )
    )

lttPC.diagnosa_sistem()
lttPC.tampilkan_spesifikasi()
print("Object\t : Komputer LTT\n")

#object ketiga
schPC = Allan_0(
    ram = 8000,
    prosessor = Allan_1(
        dipasang = True, 
        merk = "Intel Pentium 7540H", 
        generasi = 7
        )
    )

schPC.diagnosa_sistem()
schPC.tampilkan_spesifikasi()
print("Object\t : Komputer School\n")