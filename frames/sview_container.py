from tkinter import Tk, Frame, LabelFrame, Entry, Label, Button
from tkinter.ttk import Combobox


class ShortView(Tk):
    def __init__(self):
        super().__init__()
        self.shortBuild()

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
                                   state="disabled")
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
                                state="disabled")
        self.buttonYes.grid(row=0, column=0, padx=(0, 20))

        self.buttonNo = Button(self.buttonPanel, width=15, text="Cancel",
                               state="disabled")
        self.buttonNo.grid(row=0, column=1)

        self.buttonClose = Button(self.buttonPanel, width=15, text="Close",
                                  command=self.destroy)
        self.buttonClose.grid(row=1, column=1, pady=(15, 0))


app = ShortView()
app.mainloop()
