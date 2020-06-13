# encoding=utf-8
# Elkatip

# main class
class Elkatip():

    api = None
    gui = None

    def __init__(self):
        pass

    def toExt(self, text):
        if not self.api:
            api = __import__("api")
            self.api = api.Api()
        return self.api.toExt(text)
                    
    def toBase(self, text):
        if not self.api:
            api = __import__("api")
            self.api = api.Api()
        return self.api.toBase(text)

    def showGui(self):
        if not self.gui:
            gui = __import__("gui")
            self.gui = gui.Gui()
        self.gui.showGui()


if __name__ == "__main__":
    ktp = Elkatip()
    ktp.showGui()
    # uighurche = "ئالىمجان" # base
    # print(uighurche)
    # uyghurqa = ktp.toExt(uighurche) # ext
    # uighurche = ktp.toBase(uyghurqa) # base
    # print(uyghurqa)
    # print(uighurche)
