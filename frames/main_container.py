from tkinter import Tk, Menu, LabelFrame, Label, Entry
from frames import game_container as gc
from frames import regame_container as rgc
import db_functions as dba


class Gnumber(Tk):
    def __init__(self):
        super().__init__()
        self.build()
        self.menu()
        self.centerFrame()
        self.loadAllData()

    def build(self):
        self.title("G-Numbers | Main Menu")
        self.geometry("600x400")
        self.resizable(False, False)

        self.titlePanel = LabelFrame(self)
        self.titlePanel.pack(pady=(37, 0))

        self.titleLabel = Label(self.titlePanel, width=34, height=2,
                                text="Latest Results",
                                font=("Arial", 12, "bold"))
        self.titleLabel.grid(row=0, column=0)

        self.shortPanel = LabelFrame(self, text=" Short Game Results",
                                     labelanchor="n")
        self.shortPanel.pack(pady=(30, 0))

        self.shortLabel = Label(self.shortPanel, text="Game #1")
        self.shortLabel.grid(row=0, column=0, padx=(15, 5), pady=15)

        self.shortEntry1 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry1.grid(row=0, column=1, padx=(15, 0), pady=15)

        self.shortEntry2 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry2.grid(row=0, column=2, padx=(15, 0), pady=15)

        self.shortEntry3 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry3.grid(row=0, column=3, padx=(15, 0), pady=15)

        self.shortEntry4 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry4.grid(row=0, column=4, padx=(15, 0), pady=15)

        self.shortEntry5 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry5.grid(row=0, column=5, padx=(15, 0), pady=15)

        self.shortEntry6 = Entry(self.shortPanel, width=4, justify="center",
                                 state="readonly")
        self.shortEntry6.grid(row=0, column=6, padx=(15, 15), pady=15)

        self.longPanel = LabelFrame(self, text=" Long Game Results",
                                    labelanchor="n")
        self.longPanel.pack(pady=(30, 0))

        self.longLabel1 = Label(self.longPanel, text="Game #1")
        self.longLabel1.grid(row=0, column=0, padx=(15, 5), pady=(15, 0))

        self.longEntry11 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry11.grid(row=0, column=1, padx=(15, 0), pady=(15, 0))

        self.longEntry12 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry12.grid(row=0, column=2, padx=(15, 0), pady=(15, 0))

        self.longEntry13 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry13.grid(row=0, column=3, padx=(15, 0), pady=(15, 0))

        self.longEntry14 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry14.grid(row=0, column=4, padx=(15, 0), pady=(15, 0))

        self.longEntry15 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry15.grid(row=0, column=5, padx=(15, 0), pady=(15, 0))

        self.longEntry16 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry16.grid(row=0, column=6, padx=(15, 15), pady=(15, 0))

        self.longLabel2 = Label(self.longPanel, text="Game #2")
        self.longLabel2.grid(row=1, column=0, padx=(15, 5), pady=(15, 0))

        self.longEntry21 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry21.grid(row=1, column=1, padx=(15, 0), pady=(15, 0))

        self.longEntry22 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry22.grid(row=1, column=2, padx=(15, 0), pady=(15, 0))

        self.longEntry23 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry23.grid(row=1, column=3, padx=(15, 0), pady=(15, 0))

        self.longEntry24 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry24.grid(row=1, column=4, padx=(15, 0), pady=(15, 0))

        self.longEntry25 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry25.grid(row=1, column=5, padx=(15, 0), pady=(15, 0))

        self.longEntry26 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry26.grid(row=1, column=6, padx=(15, 15), pady=(15, 0))

        self.longLabel3 = Label(self.longPanel, text="Game #3")
        self.longLabel3.grid(row=2, column=0, padx=(15, 5), pady=15)

        self.longEntry31 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry31.grid(row=2, column=1, padx=(15, 0), pady=15)

        self.longEntry32 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry32.grid(row=2, column=2, padx=(15, 0), pady=15)

        self.longEntry33 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry33.grid(row=2, column=3, padx=(15, 0), pady=15)

        self.longEntry34 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry34.grid(row=2, column=4, padx=(15, 0), pady=15)

        self.longEntry35 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry35.grid(row=2, column=5, padx=(15, 0), pady=15)

        self.longEntry36 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry36.grid(row=2, column=6, padx=(15, 15), pady=15)

    def menu(self):
        self.mainMenu = Menu()

        self.optionGame = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Game", menu=self.optionGame)

        self.optionGame.add_command(label="Play",
                                    command=lambda: gc.GPanel(self))
        self.optionGame.add_command(label="RePlay",
                                    command=lambda: rgc.RGPanel(self))
        self.optionGame.add_separator()
        self.optionGame.add_command(label="Exit", command=self.quit)

        self.optionView = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="View", menu=self.optionView)

        self.optionView.add_cascade(label="Short Game")
        self.optionView.add_cascade(label="Long Game")

        self.optionData = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Data", menu=self.optionData)

        self.optionData.add_cascade(label="Previous Data")
        self.optionData.add_cascade(label="Winner Numbers")

        self.optionAbout = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="About", menu=self.optionAbout)

        self.config(menu=self.mainMenu)

    def loadAllData(self):
        dataShort, dataLong = dba.dbaShowLatest()

        self.enableEntries()

        self.shortEntry1.insert(0, dataShort[3])
        self.shortEntry2.insert(0, dataShort[4])
        self.shortEntry3.insert(0, dataShort[5])
        self.shortEntry4.insert(0, dataShort[6])
        self.shortEntry5.insert(0, dataShort[7])
        self.shortEntry6.insert(0, dataShort[8])

        self.longEntry11.insert(0, dataLong[0][3])
        self.longEntry12.insert(0, dataLong[0][4])
        self.longEntry13.insert(0, dataLong[0][5])
        self.longEntry14.insert(0, dataLong[0][6])
        self.longEntry15.insert(0, dataLong[0][7])
        self.longEntry16.insert(0, dataLong[0][8])

        self.longEntry21.insert(0, dataLong[1][3])
        self.longEntry22.insert(0, dataLong[1][4])
        self.longEntry23.insert(0, dataLong[1][5])
        self.longEntry24.insert(0, dataLong[1][6])
        self.longEntry25.insert(0, dataLong[1][7])
        self.longEntry26.insert(0, dataLong[1][8])

        self.longEntry31.insert(0, dataLong[2][3])
        self.longEntry32.insert(0, dataLong[2][4])
        self.longEntry33.insert(0, dataLong[2][5])
        self.longEntry34.insert(0, dataLong[2][6])
        self.longEntry35.insert(0, dataLong[2][7])
        self.longEntry36.insert(0, dataLong[2][8])

        self.disableEntries()

    def enableEntries(self):
        self.shortEntry1.config(state="normal")
        self.shortEntry2.config(state="normal")
        self.shortEntry3.config(state="normal")
        self.shortEntry4.config(state="normal")
        self.shortEntry5.config(state="normal")
        self.shortEntry6.config(state="normal")

        self.longEntry11.config(state="normal")
        self.longEntry12.config(state="normal")
        self.longEntry13.config(state="normal")
        self.longEntry14.config(state="normal")
        self.longEntry15.config(state="normal")
        self.longEntry16.config(state="normal")

        self.longEntry21.config(state="normal")
        self.longEntry22.config(state="normal")
        self.longEntry23.config(state="normal")
        self.longEntry24.config(state="normal")
        self.longEntry25.config(state="normal")
        self.longEntry26.config(state="normal")

        self.longEntry31.config(state="normal")
        self.longEntry32.config(state="normal")
        self.longEntry33.config(state="normal")
        self.longEntry34.config(state="normal")
        self.longEntry35.config(state="normal")
        self.longEntry36.config(state="normal")

    def disableEntries(self):
        self.shortEntry1.config(state="readonly")
        self.shortEntry2.config(state="readonly")
        self.shortEntry3.config(state="readonly")
        self.shortEntry4.config(state="readonly")
        self.shortEntry5.config(state="readonly")
        self.shortEntry6.config(state="readonly")

        self.longEntry11.config(state="readonly")
        self.longEntry12.config(state="readonly")
        self.longEntry13.config(state="readonly")
        self.longEntry14.config(state="readonly")
        self.longEntry15.config(state="readonly")
        self.longEntry16.config(state="readonly")

        self.longEntry21.config(state="readonly")
        self.longEntry22.config(state="readonly")
        self.longEntry23.config(state="readonly")
        self.longEntry24.config(state="readonly")
        self.longEntry25.config(state="readonly")
        self.longEntry26.config(state="readonly")

        self.longEntry31.config(state="readonly")
        self.longEntry32.config(state="readonly")
        self.longEntry33.config(state="readonly")
        self.longEntry34.config(state="readonly")
        self.longEntry35.config(state="readonly")
        self.longEntry36.config(state="readonly")

    def centerFrame(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")
