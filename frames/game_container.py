from tkinter import Toplevel, Frame, LabelFrame, Label, Entry, Button
from tkinter import Radiobutton, StringVar
import db_functions as dba
import game_engine as gen


class GPanel(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()

        self.gameType = StringVar()
        self.gameType.set(None)

        self.build()
        self.focus()

    def build(self):
        self.title("G-Numbers | Game Panel")
        self.resizable(False, False)

        self.panelOne = Frame(self)
        self.panelOne.grid(row=0, column=0, padx=(15, 10), pady=(15, 0))

        self.selectGame = LabelFrame(self.panelOne, text=" Select Game ",
                                     labelanchor="n")
        self.selectGame.grid(row=0, column=0)

        self.shortSel = Radiobutton(self.selectGame, text="Short Game",
                                    value="short", variable=self.gameType,
                                    command=self.gameAction)
        self.shortSel.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.longSel = Radiobutton(self.selectGame, text="Long Game",
                                   value="long", variable=self.gameType,
                                   command=self.gameAction)
        self.longSel.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.buttonGame = Frame(self.panelOne)
        self.buttonGame.grid(row=1, column=0, pady=(20, 15))

        self.buttonPlay = Button(self.buttonGame, width=15, text="Play Game",
                                 state="disabled", command=self.gameplay)
        self.buttonPlay.grid(row=0, column=0)

        self.buttonReset = Button(self.buttonGame, width=15, text="Reset Game",
                                  state="disabled", command=self.gameReset)
        self.buttonReset.grid(row=1, column=0, pady=(15, 0))

        self.buttonClose = Button(self.buttonGame, width=15, text="Close",
                                  command=self.destroy)
        self.buttonClose.grid(row=2, column=0, pady=(15, 0))

        self.panelTwo = Frame(self)
        self.panelTwo.grid(row=0, column=1, padx=(15, 15), pady=(15, 0),
                           sticky="n")

        self.shortPanel = LabelFrame(self.panelTwo,
                                     text=" Short Game Numbers ",
                                     labelanchor="n")
        self.shortPanel.grid(row=0, column=1)

        self.shortLabel = Label(self.shortPanel, text="Game #1")
        self.shortLabel.grid(row=0, column=0, padx=(10, 0), pady=10)

        self.shortEntry01 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry01.grid(row=0, column=1, padx=(10, 0), pady=10)

        self.shortEntry02 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry02.grid(row=0, column=2, padx=(10, 0), pady=10)

        self.shortEntry03 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry03.grid(row=0, column=3, padx=(10, 0), pady=10)

        self.shortEntry04 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry04.grid(row=0, column=4, padx=(10, 0), pady=10)

        self.shortEntry05 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry05.grid(row=0, column=5, padx=(10, 0), pady=10)

        self.shortEntry06 = Entry(self.shortPanel, width=4, justify="center",
                                  state="readonly")
        self.shortEntry06.grid(row=0, column=6, padx=(10, 15), pady=10)

        self.longPanel = LabelFrame(self.panelTwo, text=" Long Game Numbers ",
                                    labelanchor="n")
        self.longPanel.grid(row=1, column=1, pady=(25, 0))

        self.longLabel1 = Label(self.longPanel, text="Game #1")
        self.longLabel1.grid(row=0, column=0, padx=(10, 0), pady=10)

        self.longEntry11 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry11.grid(row=0, column=1, padx=(10, 0), pady=10)

        self.longEntry12 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry12.grid(row=0, column=2, padx=(10, 0), pady=10)

        self.longEntry13 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry13.grid(row=0, column=3, padx=(10, 0), pady=10)

        self.longEntry14 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry14.grid(row=0, column=4, padx=(10, 0), pady=10)

        self.longEntry15 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry15.grid(row=0, column=5, padx=(10, 0), pady=10)

        self.longEntry16 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry16.grid(row=0, column=6, padx=(10, 15), pady=10)

        self.longLabel2 = Label(self.longPanel, text="Game #2")
        self.longLabel2.grid(row=1, column=0, padx=(10, 0), pady=10)

        self.longEntry21 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry21.grid(row=1, column=1, padx=(10, 0), pady=10)

        self.longEntry22 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry22.grid(row=1, column=2, padx=(10, 0), pady=10)

        self.longEntry23 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry23.grid(row=1, column=3, padx=(10, 0), pady=10)

        self.longEntry24 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry24.grid(row=1, column=4, padx=(10, 0), pady=10)

        self.longEntry25 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry25.grid(row=1, column=5, padx=(10, 0), pady=10)

        self.longEntry26 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry26.grid(row=1, column=6, padx=(10, 15), pady=10)

        self.longLabel3 = Label(self.longPanel, text="Game #3")
        self.longLabel3.grid(row=2, column=0, padx=(10, 0), pady=10)

        self.longEntry31 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry31.grid(row=2, column=1, padx=(10, 0), pady=10)

        self.longEntry32 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry32.grid(row=2, column=2, padx=(10, 0), pady=10)

        self.longEntry33 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry33.grid(row=2, column=3, padx=(10, 0), pady=10)

        self.longEntry34 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry34.grid(row=2, column=4, padx=(10, 0), pady=10)

        self.longEntry35 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry35.grid(row=2, column=5, padx=(10, 0), pady=10)

        self.longEntry36 = Entry(self.longPanel, width=4, justify="center",
                                 state="readonly")
        self.longEntry36.grid(row=2, column=6, padx=(10, 15), pady=10)

    def buildResults(self):
        (listResult1, listResult2,
         listResult3, listResult4) = gen.gEngine(self.gameType.get())

        if self.gameType.get() == "short":
            result1 = f"5+ -> {", ".join(listResult1)}"
            result2 = f"4 --> {", ".join(listResult2)}"
            result3 = f"3 --> {", ".join(listResult3)}"
            result4 = f"2 --> {", ".join(listResult4)}"
        else:
            result1 = f"6+ -> {", ".join(listResult1)}"
            result2 = f"5 --> {", ".join(listResult2)}"
            result3 = f"4 --> {", ".join(listResult3)}"
            result4 = f"3 --> {", ".join(listResult4)}"

        self.panelThree = Frame(self)
        self.panelThree.grid(row=1, column=0, columnspan=2, padx=15,
                             pady=(10, 15), sticky="we")

        self.panelButton = Frame(self.panelThree)
        self.panelButton.grid(row=0, column=0)

        self.buttonNew = Button(self.panelButton, width=15, text="New Game",
                                command=self.gameNew)
        self.buttonNew.pack()

        self.panelResults = LabelFrame(self.panelThree, width=310, height=150,
                                       text=" Numbers Repetition ",
                                       labelanchor="n")
        self.panelResults.grid(row=0, column=1, padx=(25, 0))
        self.panelResults.grid_propagate(False)

        self.labelRow01 = Label(self.panelResults, text=result1)
        self.labelRow01.grid(row=0, column=0, padx=10, pady=(5, 0),
                             sticky="w")

        self.labelRow02 = Label(self.panelResults, text=result2)
        self.labelRow02.grid(row=1, column=0, padx=10, pady=(10, 0),
                             sticky="w")

        self.labelRow03 = Label(self.panelResults, text=result3)
        self.labelRow03.grid(row=2, column=0, padx=10, pady=(10, 0),
                             sticky="w")

        self.labelRow04 = Label(self.panelResults, text=result4)
        self.labelRow04.grid(row=3, column=0, padx=10, pady=(10, 10),
                             sticky="w")

    def gameAction(self):
        self.shortSel.config(state="disabled")
        self.longSel.config(state="disabled")
        self.buttonPlay.config(state="active")
        self.buttonReset.config(state="active")

        self.enableEntries()

    def gameReset(self):
        self.cleanEntries()
        self.disableEntries()

        self.gameType.set(None)

        self.shortSel.config(state="normal")
        self.longSel.config(state="normal")
        self.buttonPlay.config(state="disabled")
        self.buttonReset.config(state="disabled")

    def gameplay(self):
        self.buttonPlay.config(state="disabled")
        self.buttonReset.config(state="disabled")

        dba.dbaUpdateGame(self.gameType.get())

        if self.gameType.get() == "short":
            data = ("S", "W1", 1,
                    int(self.shortEntry01.get()),
                    int(self.shortEntry02.get()),
                    int(self.shortEntry03.get()),
                    int(self.shortEntry04.get()),
                    int(self.shortEntry05.get()),
                    int(self.shortEntry06.get()))

            self.disableEntries()
            dba.dbaInsertValues(data)
        else:
            data1 = ("L", "W1", 1,
                     int(self.longEntry11.get()),
                     int(self.longEntry12.get()),
                     int(self.longEntry13.get()),
                     int(self.longEntry14.get()),
                     int(self.longEntry15.get()),
                     int(self.longEntry16.get()))

            data2 = ("L", "W1", 2,
                     int(self.longEntry21.get()),
                     int(self.longEntry22.get()),
                     int(self.longEntry23.get()),
                     int(self.longEntry24.get()),
                     int(self.longEntry25.get()),
                     int(self.longEntry26.get()))

            data3 = ("L", "W1", 3,
                     int(self.longEntry31.get()),
                     int(self.longEntry32.get()),
                     int(self.longEntry33.get()),
                     int(self.longEntry34.get()),
                     int(self.longEntry35.get()),
                     int(self.longEntry36.get()))

            self.disableEntries()
            dba.dbaInsertValues(data1)
            dba.dbaInsertValues(data2)
            dba.dbaInsertValues(data3)

        self.buildResults()
        self.updateMaster()

    def gameNew(self):
        self.panelThree.destroy()
        self.enableEntries()
        self.gameReset()

    def enableEntries(self):
        if self.gameType.get() == "short":
            self.shortEntry01.config(state="normal")
            self.shortEntry02.config(state="normal")
            self.shortEntry03.config(state="normal")
            self.shortEntry04.config(state="normal")
            self.shortEntry05.config(state="normal")
            self.shortEntry06.config(state="normal")

            self.shortEntry01.focus()
        else:
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

            self.longEntry11.focus()

    def disableEntries(self):
        if self.gameType.get() == "short":
            self.shortEntry01.config(state="readonly")
            self.shortEntry02.config(state="readonly")
            self.shortEntry03.config(state="readonly")
            self.shortEntry04.config(state="readonly")
            self.shortEntry05.config(state="readonly")
            self.shortEntry06.config(state="readonly")
        else:
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

    def cleanEntries(self):
        if self.gameType.get() == "short":
            self.shortEntry01.delete(0, "end")
            self.shortEntry02.delete(0, "end")
            self.shortEntry03.delete(0, "end")
            self.shortEntry04.delete(0, "end")
            self.shortEntry05.delete(0, "end")
            self.shortEntry06.delete(0, "end")
        else:
            self.longEntry11.delete(0, "end")
            self.longEntry12.delete(0, "end")
            self.longEntry13.delete(0, "end")
            self.longEntry14.delete(0, "end")
            self.longEntry15.delete(0, "end")
            self.longEntry16.delete(0, "end")

            self.longEntry21.delete(0, "end")
            self.longEntry22.delete(0, "end")
            self.longEntry23.delete(0, "end")
            self.longEntry24.delete(0, "end")
            self.longEntry25.delete(0, "end")
            self.longEntry26.delete(0, "end")

            self.longEntry31.delete(0, "end")
            self.longEntry32.delete(0, "end")
            self.longEntry33.delete(0, "end")
            self.longEntry34.delete(0, "end")
            self.longEntry35.delete(0, "end")
            self.longEntry36.delete(0, "end")

    def updateMaster(self):
        dataShort, dataLong = dba.dbaShowLatest()

        self.enableMasterEntries()
        self.cleanMasterEntries()

        self.master.shortEntry1.insert(0, dataShort[3])
        self.master.shortEntry2.insert(0, dataShort[4])
        self.master.shortEntry3.insert(0, dataShort[5])
        self.master.shortEntry4.insert(0, dataShort[6])
        self.master.shortEntry5.insert(0, dataShort[7])
        self.master.shortEntry6.insert(0, dataShort[8])

        self.master.longEntry11.insert(0, dataLong[0][3])
        self.master.longEntry12.insert(0, dataLong[0][4])
        self.master.longEntry13.insert(0, dataLong[0][5])
        self.master.longEntry14.insert(0, dataLong[0][6])
        self.master.longEntry15.insert(0, dataLong[0][7])
        self.master.longEntry16.insert(0, dataLong[0][8])

        self.master.longEntry21.insert(0, dataLong[1][3])
        self.master.longEntry22.insert(0, dataLong[1][4])
        self.master.longEntry23.insert(0, dataLong[1][5])
        self.master.longEntry24.insert(0, dataLong[1][6])
        self.master.longEntry25.insert(0, dataLong[1][7])
        self.master.longEntry26.insert(0, dataLong[1][8])

        self.master.longEntry31.insert(0, dataLong[2][3])
        self.master.longEntry32.insert(0, dataLong[2][4])
        self.master.longEntry33.insert(0, dataLong[2][5])
        self.master.longEntry34.insert(0, dataLong[2][6])
        self.master.longEntry35.insert(0, dataLong[2][7])
        self.master.longEntry36.insert(0, dataLong[2][8])

        self.disableMasterEntries()

    def enableMasterEntries(self):
        self.master.shortEntry1.config(state="normal")
        self.master.shortEntry2.config(state="normal")
        self.master.shortEntry3.config(state="normal")
        self.master.shortEntry4.config(state="normal")
        self.master.shortEntry5.config(state="normal")
        self.master.shortEntry6.config(state="normal")

        self.master.longEntry11.config(state="normal")
        self.master.longEntry12.config(state="normal")
        self.master.longEntry13.config(state="normal")
        self.master.longEntry14.config(state="normal")
        self.master.longEntry15.config(state="normal")
        self.master.longEntry16.config(state="normal")

        self.master.longEntry21.config(state="normal")
        self.master.longEntry22.config(state="normal")
        self.master.longEntry23.config(state="normal")
        self.master.longEntry24.config(state="normal")
        self.master.longEntry25.config(state="normal")
        self.master.longEntry26.config(state="normal")

        self.master.longEntry31.config(state="normal")
        self.master.longEntry32.config(state="normal")
        self.master.longEntry33.config(state="normal")
        self.master.longEntry34.config(state="normal")
        self.master.longEntry35.config(state="normal")
        self.master.longEntry36.config(state="normal")

    def disableMasterEntries(self):
        self.master.shortEntry1.config(state="readonly")
        self.master.shortEntry2.config(state="readonly")
        self.master.shortEntry3.config(state="readonly")
        self.master.shortEntry4.config(state="readonly")
        self.master.shortEntry5.config(state="readonly")
        self.master.shortEntry6.config(state="readonly")

        self.master.longEntry11.config(state="readonly")
        self.master.longEntry12.config(state="readonly")
        self.master.longEntry13.config(state="readonly")
        self.master.longEntry14.config(state="readonly")
        self.master.longEntry15.config(state="readonly")
        self.master.longEntry16.config(state="readonly")

        self.master.longEntry21.config(state="readonly")
        self.master.longEntry22.config(state="readonly")
        self.master.longEntry23.config(state="readonly")
        self.master.longEntry24.config(state="readonly")
        self.master.longEntry25.config(state="readonly")
        self.master.longEntry26.config(state="readonly")

        self.master.longEntry31.config(state="readonly")
        self.master.longEntry32.config(state="readonly")
        self.master.longEntry33.config(state="readonly")
        self.master.longEntry34.config(state="readonly")
        self.master.longEntry35.config(state="readonly")
        self.master.longEntry36.config(state="readonly")

    def cleanMasterEntries(self):
        self.master.shortEntry1.delete(0, "end")
        self.master.shortEntry2.delete(0, "end")
        self.master.shortEntry3.delete(0, "end")
        self.master.shortEntry4.delete(0, "end")
        self.master.shortEntry5.delete(0, "end")
        self.master.shortEntry6.delete(0, "end")

        self.master.longEntry11.delete(0, "end")
        self.master.longEntry12.delete(0, "end")
        self.master.longEntry13.delete(0, "end")
        self.master.longEntry14.delete(0, "end")
        self.master.longEntry15.delete(0, "end")
        self.master.longEntry16.delete(0, "end")

        self.master.longEntry21.delete(0, "end")
        self.master.longEntry22.delete(0, "end")
        self.master.longEntry23.delete(0, "end")
        self.master.longEntry24.delete(0, "end")
        self.master.longEntry25.delete(0, "end")
        self.master.longEntry26.delete(0, "end")

        self.master.longEntry31.delete(0, "end")
        self.master.longEntry32.delete(0, "end")
        self.master.longEntry33.delete(0, "end")
        self.master.longEntry34.delete(0, "end")
        self.master.longEntry35.delete(0, "end")
        self.master.longEntry36.delete(0, "end")
