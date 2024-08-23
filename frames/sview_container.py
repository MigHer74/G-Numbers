from tkinter import Toplevel, Frame, LabelFrame, Entry, Label, Button
from tkinter.ttk import Combobox
import db_functions as dba


class ShortView(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.transient(parent)
        self.grab_set()
        self.shortBuild()
        self.enableEntries()
        self.cleanEntries()
        self.retrieveData()
        self.disableEntries()
        self.focus()

    def shortBuild(self):
        self.title("G-Numbers | Data Short Game")
        self.resizable(False, False)

        self.panelView = LabelFrame(self, text=" Saved Numbers ",
                                    labelanchor="n")
        self.panelView.pack(padx=(15, 15), pady=(15, 0))

        self.labelWeek1 = Label(self.panelView, text="Week #1:")
        self.labelWeek1.grid(row=0, column=0, padx=(15, 10), pady=(10, 0))

        self.entryWeek11 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek11.grid(row=0, column=1, padx=(5, 15), pady=(10, 0))
        self.entryWeek12 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek12.grid(row=0, column=2, padx=(0, 15), pady=(10, 0))
        self.entryWeek13 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek13.grid(row=0, column=3, padx=(0, 15), pady=(10, 0))
        self.entryWeek14 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek14.grid(row=0, column=4, padx=(0, 15), pady=(10, 0))
        self.entryWeek15 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek15.grid(row=0, column=5, padx=(0, 15), pady=(10, 0))
        self.entryWeek16 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek16.grid(row=0, column=6, padx=(0, 15), pady=(10, 0))

        self.labelWeek2 = Label(self.panelView, text="Week #2:")
        self.labelWeek2.grid(row=1, column=0, padx=(15, 10), pady=(10, 0))

        self.entryWeek21 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek21.grid(row=1, column=1, padx=(5, 15), pady=(10, 0))
        self.entryWeek22 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek22.grid(row=1, column=2, padx=(0, 15), pady=(10, 0))
        self.entryWeek23 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek23.grid(row=1, column=3, padx=(0, 15), pady=(10, 0))
        self.entryWeek24 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek24.grid(row=1, column=4, padx=(0, 15), pady=(10, 0))
        self.entryWeek25 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek25.grid(row=1, column=5, padx=(0, 15), pady=(10, 0))
        self.entryWeek26 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek26.grid(row=1, column=6, padx=(0, 15), pady=(10, 0))

        self.labelWeek3 = Label(self.panelView, text="Week #3:")
        self.labelWeek3.grid(row=2, column=0, padx=(15, 10), pady=(10, 0))

        self.entryWeek31 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek31.grid(row=2, column=1, padx=(5, 15), pady=(10, 0))
        self.entryWeek32 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek32.grid(row=2, column=2, padx=(0, 15), pady=(10, 0))
        self.entryWeek33 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek33.grid(row=2, column=3, padx=(0, 15), pady=(10, 0))
        self.entryWeek34 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek34.grid(row=2, column=4, padx=(0, 15), pady=(10, 0))
        self.entryWeek35 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek35.grid(row=2, column=5, padx=(0, 15), pady=(10, 0))
        self.entryWeek36 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek36.grid(row=2, column=6, padx=(0, 15), pady=(10, 0))

        self.labelWeek4 = Label(self.panelView, text="Week #4:")
        self.labelWeek4.grid(row=3, column=0, padx=(15, 10), pady=(10, 0))

        self.entryWeek41 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek41.grid(row=3, column=1, padx=(5, 15), pady=(10, 0))
        self.entryWeek42 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek42.grid(row=3, column=2, padx=(0, 15), pady=(10, 0))
        self.entryWeek43 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek43.grid(row=3, column=3, padx=(0, 15), pady=(10, 0))
        self.entryWeek44 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek44.grid(row=3, column=4, padx=(0, 15), pady=(10, 0))
        self.entryWeek45 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek45.grid(row=3, column=5, padx=(0, 15), pady=(10, 0))
        self.entryWeek46 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek46.grid(row=3, column=6, padx=(0, 15), pady=(10, 0))

        self.labelWeek5 = Label(self.panelView, text="Week #5:")
        self.labelWeek5.grid(row=4, column=0, padx=(15, 10), pady=(10, 0))

        self.entryWeek51 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek51.grid(row=4, column=1, padx=(5, 15), pady=(10, 0))
        self.entryWeek52 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek52.grid(row=4, column=2, padx=(0, 15), pady=(10, 0))
        self.entryWeek53 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek53.grid(row=4, column=3, padx=(0, 15), pady=(10, 0))
        self.entryWeek54 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek54.grid(row=4, column=4, padx=(0, 15), pady=(10, 0))
        self.entryWeek55 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek55.grid(row=4, column=5, padx=(0, 15), pady=(10, 0))
        self.entryWeek56 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek56.grid(row=4, column=6, padx=(0, 15), pady=(10, 0))

        self.labelWeek6 = Label(self.panelView, text="Week #6:")
        self.labelWeek6.grid(row=5, column=0, padx=(15, 10), pady=(10, 10))

        self.entryWeek61 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek61.grid(row=5, column=1, padx=(5, 15), pady=(10, 10))
        self.entryWeek62 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek62.grid(row=5, column=2, padx=(0, 15), pady=(10, 10))
        self.entryWeek63 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek63.grid(row=5, column=3, padx=(0, 15), pady=(10, 10))
        self.entryWeek64 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek64.grid(row=5, column=4, padx=(0, 15), pady=(10, 10))
        self.entryWeek65 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek65.grid(row=5, column=5, padx=(0, 15), pady=(10, 10))
        self.entryWeek66 = Entry(self.panelView, width=4, justify="center",
                                 state="readonly")
        self.entryWeek66.grid(row=5, column=6, padx=(0, 15), pady=(10, 10))

        self.buttonUpdate = Button(self, width=15, text="Update",
                                   command=self.updateData)
        self.buttonUpdate.pack(pady=(20, 0))

        self.panelModify = LabelFrame(self, text=" Update Data Storage ",
                                      labelanchor="n")
        self.panelModify.pack(padx=(15, 15), pady=(20, 15))

        self.panelWeek = Frame(self.panelModify)
        self.panelWeek.grid(row=0, column=0, sticky="w")

        self.labelWeek = Label(self.panelWeek, text="Week")
        self.labelWeek.grid(row=0, column=0, padx=(15, 10), pady=(10, 0))

        self.panelNumbers = Frame(self.panelModify)
        self.panelNumbers.grid(row=1, column=0)

        self.comboWeek = Combobox(self.panelNumbers, width=5,
                                  values=[1, 2, 3, 4, 5, 6], state="disabled")
        self.comboWeek.grid(row=0, column=0, padx=(15, 0), pady=(10, 10))

        self.entryWeek1 = Entry(self.panelNumbers, width=4, justify="center",
                                state="readonly")
        self.entryWeek1.grid(row=0, column=1, padx=(15, 0), pady=(10, 10))

        self.entryWeek2 = Entry(self.panelNumbers, width=4, justify="center",
                                state="readonly")
        self.entryWeek2.grid(row=0, column=2, padx=(15, 0), pady=(10, 10))

        self.entryWeek3 = Entry(self.panelNumbers, width=4, justify="center",
                                state="readonly")
        self.entryWeek3.grid(row=0, column=3, padx=(15, 0), pady=(10, 10))

        self.entryWeek4 = Entry(self.panelNumbers, width=4, justify="center",
                                state="readonly")
        self.entryWeek4.grid(row=0, column=4, padx=(15, 0), pady=(10, 10))

        self.entryWeek5 = Entry(self.panelNumbers, width=4, justify="center",
                                state="readonly")
        self.entryWeek5.grid(row=0, column=5, padx=(15, 0), pady=(10, 10))

        self.entryWeek6 = Entry(self.panelNumbers, width=4, justify="center",
                                state="readonly")
        self.entryWeek6.grid(row=0, column=6, padx=(15, 15), pady=(10, 10))

        self.buttonPanel = Frame(self)
        self.buttonPanel.pack(pady=(10, 20))

        self.buttonYes = Button(self.buttonPanel, width=15, text="Save",
                                state="disabled", command=self.saveData)
        self.buttonYes.grid(row=0, column=0, padx=(0, 20))

        self.buttonNo = Button(self.buttonPanel, width=15, text="Cancel",
                               state="disabled", command=self.cancelData)
        self.buttonNo.grid(row=0, column=1)

        self.buttonClose = Button(self.buttonPanel, width=15, text="Close",
                                  command=self.destroy)
        self.buttonClose.grid(row=1, column=1, pady=(15, 0))

    def updateData(self):
        self.buttonUpdate.config(state="disabled")
        self.comboWeek.config(state="readonly")
        self.comboWeek.bind("<<ComboboxSelected>>", self.selectWeek)

    def cancelData(self):
        self.comboWeek.config(state="active")
        self.comboWeek.delete(0, "end")
        self.comboWeek.config(state="disabled")
        self.buttonYes.config(state="disabled")
        self.buttonNo.config(state="disabled")
        self.buttonUpdate.config(state="active")
        self.cleanWeekEntries()
        self.disableWeekEntries()

    def saveData(self):
        tempWeek = "W" + self.comboWeek.get()
        tempData = (int(self.entryWeek1.get()),
                    int(self.entryWeek2.get()),
                    int(self.entryWeek3.get()),
                    int(self.entryWeek4.get()),
                    int(self.entryWeek5.get()),
                    int(self.entryWeek6.get()))

        dba.dbaUpdateOneWeek("S", tempWeek, 1, tempData)

        self.cancelData()
        self.enableEntries()
        self.cleanEntries()
        self.retrieveData()
        self.disableEntries()

    def selectWeek(self, event):
        self.selectedWeek = ("W" + self.comboWeek.get())
        self.dataWeek = dba.dbaRetrieveOneWeek("short", self.selectedWeek)
        self.enableWeekEntries()
        self.cleanWeekEntries()
        self.insertWeekEntries()
        self.buttonYes.config(state="normal")
        self.buttonNo.config(state="normal")

    def retrieveData(self):
        datashort = dba.dbaRetriveOrderValues("short")

        self.entryWeek11.insert(0, datashort[0][3])
        self.entryWeek12.insert(0, datashort[0][4])
        self.entryWeek13.insert(0, datashort[0][5])
        self.entryWeek14.insert(0, datashort[0][6])
        self.entryWeek15.insert(0, datashort[0][7])
        self.entryWeek16.insert(0, datashort[0][8])

        self.entryWeek21.insert(0, datashort[1][3])
        self.entryWeek22.insert(0, datashort[1][4])
        self.entryWeek23.insert(0, datashort[1][5])
        self.entryWeek24.insert(0, datashort[1][6])
        self.entryWeek25.insert(0, datashort[1][7])
        self.entryWeek26.insert(0, datashort[1][8])

        self.entryWeek31.insert(0, datashort[2][3])
        self.entryWeek32.insert(0, datashort[2][4])
        self.entryWeek33.insert(0, datashort[2][5])
        self.entryWeek34.insert(0, datashort[2][6])
        self.entryWeek35.insert(0, datashort[2][7])
        self.entryWeek36.insert(0, datashort[2][8])

        self.entryWeek41.insert(0, datashort[3][3])
        self.entryWeek42.insert(0, datashort[3][4])
        self.entryWeek43.insert(0, datashort[3][5])
        self.entryWeek44.insert(0, datashort[3][6])
        self.entryWeek45.insert(0, datashort[3][7])
        self.entryWeek46.insert(0, datashort[3][8])

        self.entryWeek51.insert(0, datashort[4][3])
        self.entryWeek52.insert(0, datashort[4][4])
        self.entryWeek53.insert(0, datashort[4][5])
        self.entryWeek54.insert(0, datashort[4][6])
        self.entryWeek55.insert(0, datashort[4][7])
        self.entryWeek56.insert(0, datashort[4][8])

        self.entryWeek61.insert(0, datashort[5][3])
        self.entryWeek62.insert(0, datashort[5][4])
        self.entryWeek63.insert(0, datashort[5][5])
        self.entryWeek64.insert(0, datashort[5][6])
        self.entryWeek65.insert(0, datashort[5][7])
        self.entryWeek66.insert(0, datashort[5][8])

    def enableEntries(self):
        self.entryWeek11.config(state="normal")
        self.entryWeek12.config(state="normal")
        self.entryWeek13.config(state="normal")
        self.entryWeek14.config(state="normal")
        self.entryWeek15.config(state="normal")
        self.entryWeek16.config(state="normal")

        self.entryWeek21.config(state="normal")
        self.entryWeek22.config(state="normal")
        self.entryWeek23.config(state="normal")
        self.entryWeek24.config(state="normal")
        self.entryWeek25.config(state="normal")
        self.entryWeek26.config(state="normal")

        self.entryWeek31.config(state="normal")
        self.entryWeek32.config(state="normal")
        self.entryWeek33.config(state="normal")
        self.entryWeek34.config(state="normal")
        self.entryWeek35.config(state="normal")
        self.entryWeek36.config(state="normal")

        self.entryWeek41.config(state="normal")
        self.entryWeek42.config(state="normal")
        self.entryWeek43.config(state="normal")
        self.entryWeek44.config(state="normal")
        self.entryWeek45.config(state="normal")
        self.entryWeek46.config(state="normal")

        self.entryWeek51.config(state="normal")
        self.entryWeek52.config(state="normal")
        self.entryWeek53.config(state="normal")
        self.entryWeek54.config(state="normal")
        self.entryWeek55.config(state="normal")
        self.entryWeek56.config(state="normal")

        self.entryWeek61.config(state="normal")
        self.entryWeek62.config(state="normal")
        self.entryWeek63.config(state="normal")
        self.entryWeek64.config(state="normal")
        self.entryWeek65.config(state="normal")
        self.entryWeek66.config(state="normal")

    def disableEntries(self):
        self.entryWeek11.config(state="readonly")
        self.entryWeek12.config(state="readonly")
        self.entryWeek13.config(state="readonly")
        self.entryWeek14.config(state="readonly")
        self.entryWeek15.config(state="readonly")
        self.entryWeek16.config(state="readonly")

        self.entryWeek21.config(state="readonly")
        self.entryWeek22.config(state="readonly")
        self.entryWeek23.config(state="readonly")
        self.entryWeek24.config(state="readonly")
        self.entryWeek25.config(state="readonly")
        self.entryWeek26.config(state="readonly")

        self.entryWeek31.config(state="readonly")
        self.entryWeek32.config(state="readonly")
        self.entryWeek33.config(state="readonly")
        self.entryWeek34.config(state="readonly")
        self.entryWeek35.config(state="readonly")
        self.entryWeek36.config(state="readonly")

        self.entryWeek41.config(state="readonly")
        self.entryWeek42.config(state="readonly")
        self.entryWeek43.config(state="readonly")
        self.entryWeek44.config(state="readonly")
        self.entryWeek45.config(state="readonly")
        self.entryWeek46.config(state="readonly")

        self.entryWeek51.config(state="readonly")
        self.entryWeek52.config(state="readonly")
        self.entryWeek53.config(state="readonly")
        self.entryWeek54.config(state="readonly")
        self.entryWeek55.config(state="readonly")
        self.entryWeek56.config(state="readonly")

        self.entryWeek61.config(state="readonly")
        self.entryWeek62.config(state="readonly")
        self.entryWeek63.config(state="readonly")
        self.entryWeek64.config(state="readonly")
        self.entryWeek65.config(state="readonly")
        self.entryWeek66.config(state="readonly")

    def cleanEntries(self):
        self.entryWeek11.delete(0, "end")
        self.entryWeek12.delete(0, "end")
        self.entryWeek13.delete(0, "end")
        self.entryWeek14.delete(0, "end")
        self.entryWeek15.delete(0, "end")
        self.entryWeek16.delete(0, "end")

        self.entryWeek21.delete(0, "end")
        self.entryWeek22.delete(0, "end")
        self.entryWeek23.delete(0, "end")
        self.entryWeek24.delete(0, "end")
        self.entryWeek25.delete(0, "end")
        self.entryWeek26.delete(0, "end")

        self.entryWeek31.delete(0, "end")
        self.entryWeek32.delete(0, "end")
        self.entryWeek33.delete(0, "end")
        self.entryWeek34.delete(0, "end")
        self.entryWeek35.delete(0, "end")
        self.entryWeek36.delete(0, "end")

        self.entryWeek41.delete(0, "end")
        self.entryWeek42.delete(0, "end")
        self.entryWeek43.delete(0, "end")
        self.entryWeek44.delete(0, "end")
        self.entryWeek45.delete(0, "end")
        self.entryWeek46.delete(0, "end")

        self.entryWeek51.delete(0, "end")
        self.entryWeek52.delete(0, "end")
        self.entryWeek53.delete(0, "end")
        self.entryWeek54.delete(0, "end")
        self.entryWeek55.delete(0, "end")
        self.entryWeek56.delete(0, "end")

        self.entryWeek61.delete(0, "end")
        self.entryWeek62.delete(0, "end")
        self.entryWeek63.delete(0, "end")
        self.entryWeek64.delete(0, "end")
        self.entryWeek65.delete(0, "end")
        self.entryWeek66.delete(0, "end")

    def enableWeekEntries(self):
        self.entryWeek1.config(state="normal")
        self.entryWeek2.config(state="normal")
        self.entryWeek3.config(state="normal")
        self.entryWeek4.config(state="normal")
        self.entryWeek5.config(state="normal")
        self.entryWeek6.config(state="normal")

    def disableWeekEntries(self):
        self.entryWeek1.config(state="readonly")
        self.entryWeek2.config(state="readonly")
        self.entryWeek3.config(state="readonly")
        self.entryWeek4.config(state="readonly")
        self.entryWeek5.config(state="readonly")
        self.entryWeek6.config(state="readonly")

    def cleanWeekEntries(self):
        self.entryWeek1.delete("0", "end")
        self.entryWeek2.delete("0", "end")
        self.entryWeek3.delete("0", "end")
        self.entryWeek4.delete("0", "end")
        self.entryWeek5.delete("0", "end")
        self.entryWeek6.delete("0", "end")

    def insertWeekEntries(self):
        self.entryWeek1.insert("0", self.dataWeek[0][3])
        self.entryWeek2.insert("0", self.dataWeek[0][4])
        self.entryWeek3.insert("0", self.dataWeek[0][5])
        self.entryWeek4.insert("0", self.dataWeek[0][6])
        self.entryWeek5.insert("0", self.dataWeek[0][7])
        self.entryWeek6.insert("0", self.dataWeek[0][8])
        self.entryWeek1.focus()
