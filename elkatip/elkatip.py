# encoding=utf-8
# Elkatip

import os
import imp

# main class
class Elkatip():

    api = None
    gui = None

    def __init__(self):
        self.modulePath = os.path.dirname(__file__)
        pass

    def toExt(self, text):
        if not self.api:
            api = imp.load_source("api", self.modulePath + "/api.py")
            self.api = api.Api()
        return self.api.toExt(text)
                    
    def toBase(self, text):
        if not self.api:
            api = imp.load_source("api", self.modulePath + "/api.py")
            self.api = api.Api()
        return self.api.toBase(text)

    def showGui(self):
        if not self.gui:
            gui = imp.load_source("gui", self.modulePath + "/gui.py")
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
