class Allan_2:
    def __init__(self, dipasang:bool = False, vendor:str = "", tipe:str = ""):
        self.dipasang = dipasang
        self.vendor = vendor
        self.tipe = tipe

    def print_info(self):
        if(self.dipasang == True):
            print("Kartu Grafik terpasang!")
        else:
            print("Kartu Grafik tidak terpasang.")