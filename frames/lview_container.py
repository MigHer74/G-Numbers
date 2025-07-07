from tkinter import Toplevel, Frame, LabelFrame, Entry, Label, Button
from tkinter import Radiobutton, IntVar
import general_tools as gt
import db_functions as dba


class LongView(Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.weekSelect = IntVar()
        self.weekSelect.set(0)

        self.transient(parent)
        self.grab_set()
        self.loadData()
        self.longBuild()
        self.focus()

    def longBuild(self):
        self.title("G-Numbers | Data Long Game")
        gt.center_window(self, 705, 620)
        self.resizable(False, False)

        self.titleFrame = LabelFrame(self)
        self.titleFrame.grid(row=0, column=0, columnspan=3,
                             padx=(15, 15), pady=(15, 0), sticky="we")

        self.titleLabel = Label(self.titleFrame, text="Saved Numbers")
        self.titleLabel.pack(pady=(5, 5))

        self.lblFrame1 = LabelFrame(self, width=215, height=143)
        self.lblFrame1.grid(row=1, column=0, padx=(15, 0), pady=(15, 0))
        self.lblFrame1.grid_propagate(False)

        self.radio1 = Radiobutton(self.lblFrame1, text="Week #1", value=1,
                                  variable=self.weekSelect,
                                  command=self.changeUpdateSelect)
        self.radio1.grid(row=0, column=0, pady=(10, 0))

        self.lblw1g1 = Label(self.lblFrame1, text=self.label11)
        self.lblw1g1.grid(row=1, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw1g2 = Label(self.lblFrame1, text=self.label12)
        self.lblw1g2.grid(row=2, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw1g3 = Label(self.lblFrame1, text=self.label13)
        self.lblw1g3.grid(row=3, column=0, padx=(10, 10), pady=(10, 10),
                          sticky="w")

        self.lblFrame2 = LabelFrame(self, width=215, height=143)
        self.lblFrame2.grid(row=1, column=1, padx=(15, 0), pady=(15, 0))
        self.lblFrame2.grid_propagate(False)

        self.radio2 = Radiobutton(self.lblFrame2, text="Week #2", value=2,
                                  variable=self.weekSelect,
                                  command=self.changeUpdateSelect)
        self.radio2.grid(row=0, column=0, pady=(10, 0))

        self.lblw2g1 = Label(self.lblFrame2, text=self.label21)
        self.lblw2g1.grid(row=1, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw2g2 = Label(self.lblFrame2, text=self.label22)
        self.lblw2g2.grid(row=2, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw2g3 = Label(self.lblFrame2, text=self.label23)
        self.lblw2g3.grid(row=3, column=0, padx=(10, 10), pady=(10, 10),
                          sticky="w")

        self.lblFrame3 = LabelFrame(self, width=215, height=143)
        self.lblFrame3.grid(row=1, column=2, padx=(15, 15), pady=(15, 0))
        self.lblFrame3.grid_propagate(False)

        self.radio3 = Radiobutton(self.lblFrame3, text="Week #3", value=3,
                                  variable=self.weekSelect,
                                  command=self.changeUpdateSelect)
        self.radio3.grid(row=0, column=0, pady=(10, 0))

        self.lblw3g1 = Label(self.lblFrame3, text=self.label31)
        self.lblw3g1.grid(row=1, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw3g2 = Label(self.lblFrame3, text=self.label32)
        self.lblw3g2.grid(row=2, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw3g3 = Label(self.lblFrame3, text=self.label33)
        self.lblw3g3.grid(row=3, column=0, padx=(10, 10), pady=(10, 10),
                          sticky="w")

        self.lblFrame4 = LabelFrame(self, width=215, height=143)
        self.lblFrame4.grid(row=2, column=0, padx=(15, 0), pady=(15, 0))
        self.lblFrame4.grid_propagate(False)

        self.radio4 = Radiobutton(self.lblFrame4, text="Week #4", value=4,
                                  variable=self.weekSelect,
                                  command=self.changeUpdateSelect)
        self.radio4.grid(row=0, column=0, pady=(10, 0))

        self.lblw4g1 = Label(self.lblFrame4, text=self.label41)
        self.lblw4g1.grid(row=1, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw4g2 = Label(self.lblFrame4, text=self.label42)
        self.lblw4g2.grid(row=2, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw4g3 = Label(self.lblFrame4, text=self.label43)
        self.lblw4g3.grid(row=3, column=0, padx=(10, 10), pady=(10, 10),
                          sticky="w")

        self.lblFrame5 = LabelFrame(self, width=215, height=143)
        self.lblFrame5.grid(row=2, column=1, padx=(15, 0), pady=(15, 0))
        self.lblFrame5.grid_propagate(False)

        self.radio5 = Radiobutton(self.lblFrame5, text="Week #5", value=5,
                                  variable=self.weekSelect,
                                  command=self.changeUpdateSelect)
        self.radio5.grid(row=0, column=0, pady=(10, 0))

        self.lblw5g1 = Label(self.lblFrame5, text=self.label51)
        self.lblw5g1.grid(row=1, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw5g2 = Label(self.lblFrame5, text=self.label52)
        self.lblw5g2.grid(row=2, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw5g3 = Label(self.lblFrame5, text=self.label53)
        self.lblw5g3.grid(row=3, column=0, padx=(10, 10), pady=(10, 10),
                          sticky="w")

        self.lblFrame6 = LabelFrame(self, width=215, height=143)
        self.lblFrame6.grid(row=2, column=2, padx=(15, 15), pady=(15, 0))
        self.lblFrame6.grid_propagate(False)

        self.radio6 = Radiobutton(self.lblFrame6, text="Week #6", value=6,
                                  variable=self.weekSelect,
                                  command=self.changeUpdateSelect)
        self.radio6.grid(row=0, column=0, pady=(10, 0))

        self.lblw6g1 = Label(self.lblFrame6, text=self.label61)
        self.lblw6g1.grid(row=1, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw6g2 = Label(self.lblFrame6, text=self.label62)
        self.lblw6g2.grid(row=2, column=0, padx=(10, 10), pady=(10, 0),
                          sticky="w")
        self.lblw6g3 = Label(self.lblFrame6, text=self.label63)
        self.lblw6g3.grid(row=3, column=0, padx=(10, 10), pady=(10, 10),
                          sticky="w")

        self.buttonUpdate = Button(self, width=15, text="Update",
                                   state="disabled", command=self.updateAction)
        self.buttonUpdate.grid(row=3, column=0, columnspan=3, pady=(20, 0))

        self.updateFrame = LabelFrame(self, text=" Update Data Storage",
                                      labelanchor="n")
        self.updateFrame.grid(row=4, column=0, columnspan=3, padx=(15, 15),
                              pady=(20, 15))

        self.entryFrame = Frame(self.updateFrame)
        self.entryFrame.grid(row=0, column=0, padx=(15, 0), pady=(15, 15))

        self.labelWeek = Label(self.entryFrame, text="Week:")
        self.labelWeek.grid(row=0, column=0, padx=(0, 15), pady=(0, 10),
                            sticky="w")

        self.entryWeek = Entry(self.entryFrame, width=4, justify="center",
                               state="readonly")
        self.entryWeek.grid(row=0, column=1, padx=(0, 15), pady=(0, 10))

        self.labelGame1 = Label(self.entryFrame, text="Game #1:")
        self.labelGame1.grid(row=1, column=0, padx=(0, 15), pady=(0, 10))

        self.entryGame11 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame11.grid(row=1, column=1, padx=(0, 15), pady=(0, 10))

        self.entryGame12 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame12.grid(row=1, column=2, padx=(0, 15), pady=(0, 10))

        self.entryGame13 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame13.grid(row=1, column=3, padx=(0, 15), pady=(0, 10))

        self.entryGame14 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame14.grid(row=1, column=4, padx=(0, 15), pady=(0, 10))

        self.entryGame15 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame15.grid(row=1, column=5, padx=(0, 15), pady=(0, 10))

        self.entryGame16 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame16.grid(row=1, column=6, padx=(0, 15), pady=(0, 10))

        self.labelGame2 = Label(self.entryFrame, text="Game #2:")
        self.labelGame2.grid(row=2, column=0, padx=(0, 15), pady=(0, 10))

        self.entryGame21 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame21.grid(row=2, column=1, padx=(0, 15), pady=(0, 10))

        self.entryGame22 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame22.grid(row=2, column=2, padx=(0, 15), pady=(0, 10))

        self.entryGame23 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame23.grid(row=2, column=3, padx=(0, 15), pady=(0, 10))

        self.entryGame24 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame24.grid(row=2, column=4, padx=(0, 15), pady=(0, 10))

        self.entryGame25 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame25.grid(row=2, column=5, padx=(0, 15), pady=(0, 10))

        self.entryGame26 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame26.grid(row=2, column=6, padx=(0, 15), pady=(0, 10))

        self.labelGame3 = Label(self.entryFrame, text="Game #3:")
        self.labelGame3.grid(row=3, column=0, padx=(0, 15), pady=(0, 10))

        self.entryGame31 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame31.grid(row=3, column=1, padx=(0, 15), pady=(0, 10))

        self.entryGame32 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame32.grid(row=3, column=2, padx=(0, 15), pady=(0, 10))

        self.entryGame33 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame33.grid(row=3, column=3, padx=(0, 15), pady=(0, 10))

        self.entryGame34 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame34.grid(row=3, column=4, padx=(0, 15), pady=(0, 10))

        self.entryGame35 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame35.grid(row=3, column=5, padx=(0, 15), pady=(0, 10))

        self.entryGame36 = Entry(self.entryFrame, width=4, justify="center",
                                 state="readonly")
        self.entryGame36.grid(row=3, column=6, padx=(0, 15), pady=(0, 10))

        self.buttonFrame = Frame(self.updateFrame)
        self.buttonFrame.grid(row=0, column=1, padx=(15, 20), pady=(15, 15))

        self.buttonSave = Button(self.buttonFrame, width=15, text="Save",
                                 state="disabled", command=self.saveAction)
        self.buttonSave.grid(row=0, column=0, pady=(0, 15))

        self.buttonCancel = Button(self.buttonFrame, width=15, text="Cancel",
                                   state="disabled", command=self.cancelAction)
        self.buttonCancel.grid(row=1, column=0, pady=(0, 15))

        self.buttonClose = Button(self.buttonFrame, width=15, text="Close",
                                  command=self.destroy)
        self.buttonClose.grid(row=2, column=0)

    def loadData(self):
        (self.week1Game1, self.week1Game2,
         self.week1Game3) = gt.load_weeks("long", "W1")

        (self.week2Game1, self.week2Game2,
         self.week2Game3) = gt.load_weeks("long", "W2")

        (self.week3Game1, self.week3Game2,
         self.week3Game3) = gt.load_weeks("long", "W3")

        (self.week4Game1, self.week4Game2,
         self.week4Game3) = gt.load_weeks("long", "W4")

        (self.week5Game1, self.week5Game2,
         self.week5Game3) = gt.load_weeks("long", "W5")

        (self.week6Game1, self.week6Game2,
         self.week6Game3) = gt.load_weeks("long", "W6")

        self.label11 = f"Game #1  --->  {self.week1Game1}"
        self.label12 = f"Game #2  --->  {self.week1Game2}"
        self.label13 = f"Game #3  --->  {self.week1Game3}"

        self.label21 = f"Game #1  --->  {self.week2Game1}"
        self.label22 = f"Game #2  --->  {self.week2Game2}"
        self.label23 = f"Game #3  --->  {self.week2Game3}"

        self.label31 = f"Game #1  --->  {self.week3Game1}"
        self.label32 = f"Game #2  --->  {self.week3Game2}"
        self.label33 = f"Game #3  --->  {self.week3Game3}"

        self.label41 = f"Game #1  --->  {self.week4Game1}"
        self.label42 = f"Game #2  --->  {self.week4Game2}"
        self.label43 = f"Game #3  --->  {self.week4Game3}"

        self.label51 = f"Game #1  --->  {self.week5Game1}"
        self.label52 = f"Game #2  --->  {self.week5Game2}"
        self.label53 = f"Game #3  --->  {self.week5Game3}"

        self.label61 = f"Game #1  --->  {self.week6Game1}"
        self.label62 = f"Game #2  --->  {self.week6Game2}"
        self.label63 = f"Game #3  --->  {self.week6Game3}"

    def changeUpdateSelect(self):
        if self.weekSelect.get() > 0:
            self.buttonUpdate.config(state="active")

    def updateAction(self):
        self.radio1.config(state="disabled")
        self.radio2.config(state="disabled")
        self.radio3.config(state="disabled")
        self.radio4.config(state="disabled")
        self.radio5.config(state="disabled")
        self.radio6.config(state="disabled")

        self.buttonUpdate.config(state="disabled")
        self.buttonSave.config(state="normal")
        self.buttonCancel.config(state="normal")

        self.eneableLongEntries()
        self.cleanLongEntries()

        self.weekUpdate = ("W" + str(self.weekSelect.get()))

        datalong = dba.dbaRetrieveOrderValues("long", self.weekUpdate)

        self.entryWeek.insert(0, self.weekSelect.get())

        self.entryGame11.insert(0, datalong[0][3])
        self.entryGame12.insert(0, datalong[0][4])
        self.entryGame13.insert(0, datalong[0][5])
        self.entryGame14.insert(0, datalong[0][6])
        self.entryGame15.insert(0, datalong[0][7])
        self.entryGame16.insert(0, datalong[0][8])

        self.entryGame21.insert(0, datalong[1][3])
        self.entryGame22.insert(0, datalong[1][4])
        self.entryGame23.insert(0, datalong[1][5])
        self.entryGame24.insert(0, datalong[1][6])
        self.entryGame25.insert(0, datalong[1][7])
        self.entryGame26.insert(0, datalong[1][8])

        self.entryGame31.insert(0, datalong[2][3])
        self.entryGame32.insert(0, datalong[2][4])
        self.entryGame33.insert(0, datalong[2][5])
        self.entryGame34.insert(0, datalong[2][6])
        self.entryGame35.insert(0, datalong[2][7])
        self.entryGame36.insert(0, datalong[2][8])

        self.entryWeek.config(state="disabled")
        self.entryGame11.focus()

    def saveAction(self):
        self.datalong01 = (self.entryGame11.get(), self.entryGame12.get(),
                           self.entryGame13.get(), self.entryGame14.get(),
                           self.entryGame15.get(), self.entryGame16.get())

        self.datalong02 = (self.entryGame21.get(), self.entryGame22.get(),
                           self.entryGame23.get(), self.entryGame24.get(),
                           self.entryGame25.get(), self.entryGame26.get())

        self.datalong03 = (self.entryGame31.get(), self.entryGame32.get(),
                           self.entryGame33.get(), self.entryGame34.get(),
                           self.entryGame35.get(), self.entryGame36.get())

        dba.dbaUpdateOneWeek("L", self.weekUpdate, 1, self.datalong01)
        dba.dbaUpdateOneWeek("L", self.weekUpdate, 2, self.datalong02)
        dba.dbaUpdateOneWeek("L", self.weekUpdate, 3, self.datalong03)

        self.cancelAction()
        self.updateMainPanel()

        if self.weekUpdate == "W1":
            self.updateLongMaster()

    def cancelAction(self):
        self.entryWeek.config(state="normal")

        self.cleanLongEntries()
        self.disableLongEntries()

        self.weekSelect.set(0)

        self.radio1.config(state="normal")
        self.radio2.config(state="normal")
        self.radio3.config(state="normal")
        self.radio4.config(state="normal")
        self.radio5.config(state="normal")
        self.radio6.config(state="normal")

        self.buttonSave.config(state="disable")
        self.buttonCancel.config(state="disabled")

    def updateLongMaster(self):
        self.eneableLongMasterPanel()
        self.cleanLongMasterPanel()
        self.insertLongMasterPanel()
        self.disableLongMasterPanel()

    def eneableLongEntries(self):
        self.entryWeek.config(state="normal")

        self.entryGame11.config(state="normal")
        self.entryGame12.config(state="normal")
        self.entryGame13.config(state="normal")
        self.entryGame14.config(state="normal")
        self.entryGame15.config(state="normal")
        self.entryGame16.config(state="normal")

        self.entryGame21.config(state="normal")
        self.entryGame22.config(state="normal")
        self.entryGame23.config(state="normal")
        self.entryGame24.config(state="normal")
        self.entryGame25.config(state="normal")
        self.entryGame26.config(state="normal")

        self.entryGame31.config(state="normal")
        self.entryGame32.config(state="normal")
        self.entryGame33.config(state="normal")
        self.entryGame34.config(state="normal")
        self.entryGame35.config(state="normal")
        self.entryGame36.config(state="normal")

    def disableLongEntries(self):
        self.entryWeek.config(state="readonly")

        self.entryGame11.config(state="readonly")
        self.entryGame12.config(state="readonly")
        self.entryGame13.config(state="readonly")
        self.entryGame14.config(state="readonly")
        self.entryGame15.config(state="readonly")
        self.entryGame16.config(state="readonly")

        self.entryGame21.config(state="readonly")
        self.entryGame22.config(state="readonly")
        self.entryGame23.config(state="readonly")
        self.entryGame24.config(state="readonly")
        self.entryGame25.config(state="readonly")
        self.entryGame26.config(state="readonly")

        self.entryGame31.config(state="readonly")
        self.entryGame32.config(state="readonly")
        self.entryGame33.config(state="readonly")
        self.entryGame34.config(state="readonly")
        self.entryGame35.config(state="readonly")
        self.entryGame36.config(state="readonly")

    def cleanLongEntries(self):
        self.entryWeek.delete(0, "end")

        self.entryGame11.delete(0, "end")
        self.entryGame12.delete(0, "end")
        self.entryGame13.delete(0, "end")
        self.entryGame14.delete(0, "end")
        self.entryGame15.delete(0, "end")
        self.entryGame16.delete(0, "end")

        self.entryGame21.delete(0, "end")
        self.entryGame22.delete(0, "end")
        self.entryGame23.delete(0, "end")
        self.entryGame24.delete(0, "end")
        self.entryGame25.delete(0, "end")
        self.entryGame26.delete(0, "end")

        self.entryGame31.delete(0, "end")
        self.entryGame32.delete(0, "end")
        self.entryGame33.delete(0, "end")
        self.entryGame34.delete(0, "end")
        self.entryGame35.delete(0, "end")
        self.entryGame36.delete(0, "end")

    def updateMainPanel(self):
        (self.updateW1g1, self.updateW1g2,
         self.updateW1g3) = gt.load_weeks("long", "W1")

        (self.updateW2g1, self.updateW2g2,
         self.updateW2g3) = gt.load_weeks("long", "W2")

        (self.updateW3g1, self.updateW3g2,
         self.updateW3g3) = gt.load_weeks("long", "W3")

        (self.updateW4g1, self.updateW4g2,
         self.updateW4g3) = gt.load_weeks("long", "W4")

        (self.updateW5g1, self.updateW5g2,
         self.updateW5g3) = gt.load_weeks("long", "W5")

        (self.updateW6g1, self.updateW6g2,
         self.updateW6g3) = gt.load_weeks("long", "W6")

        self.lblw1g1.config(text=f"Game #1  --->  {self.updateW1g1}")
        self.lblw1g2.config(text=f"Game #2  --->  {self.updateW1g2}")
        self.lblw1g3.config(text=f"Game #3  --->  {self.updateW1g3}")

        self.lblw2g1.config(text=f"Game #1  --->  {self.updateW2g1}")
        self.lblw2g2.config(text=f"Game #2  --->  {self.updateW2g2}")
        self.lblw2g3.config(text=f"Game #3  --->  {self.updateW2g3}")

        self.lblw3g1.config(text=f"Game #1  --->  {self.updateW3g1}")
        self.lblw3g2.config(text=f"Game #2  --->  {self.updateW3g2}")
        self.lblw3g3.config(text=f"Game #3  --->  {self.updateW3g3}")

        self.lblw4g1.config(text=f"Game #1  --->  {self.updateW4g1}")
        self.lblw4g2.config(text=f"Game #2  --->  {self.updateW4g2}")
        self.lblw4g3.config(text=f"Game #3  --->  {self.updateW4g3}")

        self.lblw5g1.config(text=f"Game #1  --->  {self.updateW5g1}")
        self.lblw5g2.config(text=f"Game #2  --->  {self.updateW5g2}")
        self.lblw5g3.config(text=f"Game #3  --->  {self.updateW5g3}")

        self.lblw6g1.config(text=f"Game #1  --->  {self.updateW6g1}")
        self.lblw6g2.config(text=f"Game #2  --->  {self.updateW6g2}")
        self.lblw6g3.config(text=f"Game #3  --->  {self.updateW6g3}")

    def eneableLongMasterPanel(self):
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

    def cleanLongMasterPanel(self):
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

    def insertLongMasterPanel(self):
        self.master.longEntry11.insert(0, self.datalong01[0])
        self.master.longEntry12.insert(0, self.datalong01[1])
        self.master.longEntry13.insert(0, self.datalong01[2])
        self.master.longEntry14.insert(0, self.datalong01[3])
        self.master.longEntry15.insert(0, self.datalong01[4])
        self.master.longEntry16.insert(0, self.datalong01[5])

        self.master.longEntry21.insert(0, self.datalong02[0])
        self.master.longEntry22.insert(0, self.datalong02[1])
        self.master.longEntry23.insert(0, self.datalong02[2])
        self.master.longEntry24.insert(0, self.datalong02[3])
        self.master.longEntry25.insert(0, self.datalong02[4])
        self.master.longEntry26.insert(0, self.datalong02[5])

        self.master.longEntry31.insert(0, self.datalong03[0])
        self.master.longEntry32.insert(0, self.datalong03[1])
        self.master.longEntry33.insert(0, self.datalong03[2])
        self.master.longEntry34.insert(0, self.datalong03[3])
        self.master.longEntry35.insert(0, self.datalong03[4])
        self.master.longEntry36.insert(0, self.datalong03[5])

    def disableLongMasterPanel(self):
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
