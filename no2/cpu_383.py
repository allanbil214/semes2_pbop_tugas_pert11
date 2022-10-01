class Allan_1:
    def __init__(self, dipasang:bool = False, merk:str = "", generasi:int = 0):
        self.dipasang = dipasang
        self.merk = merk
        self.generasi = generasi
        
    def print_info(self):
        if(self.dipasang == True):
            print("Prosessor terpasang!")
        else:
            print("Processor belum terpasang.")