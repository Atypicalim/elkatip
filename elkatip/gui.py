# encoding=utf-8
# gui

import os
import imp
import tkinter
import tkinter.font
import tkinter.ttk

# main class
class Gui():

    def __init__(self):
        self.modulePath = os.path.dirname(__file__)
        self.stageText = "ئېلكاتىپ" # base
        self.fontName = "UKIJ Tuz Qara"
        self.font = (self.fontName, 12)
    
    def getFonts(self):
        fonts = []
        for item in tkinter.font.families():
            tmp = item.upper()
            if ("ALKATIP" in tmp or "UKIJ" in tmp) and "TGHRA" not in tmp and "@" not in tmp and "MARKA" not in tmp:
                fonts.append(item)
        return fonts

    # graphic user interface
    def showGui(self):
        api = imp.load_source("api", self.modulePath + "/api.py")
        api = api.Api()
        windowW = 500
        windowH = 600
        # 
        window = tkinter.Tk()
        window.title("Elkatip")
        window.resizable(width=False,height=False)
        window.geometry('{}x{}+10+20'.format(windowW, windowH))
        #
        tkinter.Label(window,text = self.stageText, font=("ALKATIP Kufi", 22)).pack(side=tkinter.TOP, padx=10, pady = 10)
        # base
        txt = "ئاساسىي رايۇن : كومپيتوتېردا بىر تەرەپ قىلىش قولاي بولغان ئۆلچەملىك ھەرىپلەر"
        tkinter.Label(window,text = txt, font=self.font, justify=tkinter.RIGHT).pack(side=tkinter.TOP, fill="x")
        baseValue = tkinter.StringVar(window, self.stageText)
        def baseInput(*args):
            self.stageText = baseValue.get()
            self.drawStage()
        baseValue.trace_add("write", baseInput)
        baseEntry = tkinter.Entry(window, textvariable=baseValue, font=self.font, justify=tkinter.CENTER)
        baseEntry.pack(fill="x", padx=10, pady = 5, side=tkinter.TOP)
        # ext
        txt = "كېڭەيتىلگەن رايۇن : فوتوشۇپ ۋە گىرافىك پىروگراممىلىرىدا كۆرسىتىشكە بۇلىدۇ"
        tkinter.Label(window,text = txt, font=self.font, justify=tkinter.RIGHT).pack(side=tkinter.TOP)
        extValue = tkinter.StringVar(window, api.toExt(self.stageText))
        def extraInput(*args):
            self.stageText = api.toBase(extValue.get())
            self.drawStage()
        extValue.trace_add("write", extraInput)
        extEntry = tkinter.Entry(window, textvariable=extValue, font=self.font, justify=tkinter.CENTER)
        extEntry.pack(fill="x", padx=10, pady = 5, side=tkinter.TOP)
        # fonts
        txt = "ئۇيغۇرچە فونىتلار : كومپيۇتېرىڭىزدىكى بىر قىسىم ئەلكاتىپ ۋە يۇكىج فونتلىرى"
        tkinter.Label(window,text = txt, font=self.font).pack(side=tkinter.TOP)
        fonts = self.getFonts()
        comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值  
        comboxlist= tkinter.ttk.Combobox(window,textvariable=comvalue, justify=tkinter.CENTER) #初始化  
        comboxlist["values"]=fonts 
        comboxlist.current(0)  #选择第一个
        def comboChange(*args):
            self.fontName = comboxlist.get()
            self.drawStage()
        comboxlist.bind("<<ComboboxSelected>>", comboChange)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
        comboxlist.pack(fill="x", padx=10, pady = 5, side=tkinter.TOP)
        # base to ext
        def baseToExt():
            extValue.set(api.toExt(baseValue.get()))
        baseToExtBtn = tkinter.Button(window,text='ئاساسىي رايۇننى كېگەيتىلگەن رايۇنغا ئايلاندۇرۇش', font=self.font, command = baseToExt)
        baseToExtBtn.pack(fill="x", padx=10, pady = 5, side = tkinter.TOP)
        # ext to base
        def extToBase():
            baseValue.set(api.toBase(extValue.get()))
        extToBaseBtn = tkinter.Button(window,text='كېگەيتىلگەن رايۇننى ئاساسىي رايۇنغا ئايلاندۇرۇش', font=self.font, command = extToBase)
        extToBaseBtn.pack(fill="x", padx=10, pady = 5, side = tkinter.TOP)
        # draw ext to stage
        def drawStage():
            txt = api.toExt(self.stageText)
            max = 300
            if len(txt) > max:
                txt = txt[0:max] + "..."
            self.stageLabel['text'] = '[' + txt + ']'
            self.stageLabel['font'] = tkinter.font.Font(family=self.fontName, size=20)
        self.drawStage = drawStage
        # stage
        self.stageLabel = tkinter.Label(window,text = "", wraplength = 475)
        self.stageLabel.pack(side=tkinter.TOP, fill="x", padx=10, pady = 20)
        self.drawStage()
        # loop
        window.mainloop()
        pass
