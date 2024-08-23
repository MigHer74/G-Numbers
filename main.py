from frames import main_container
import general_tools as gt


if __name__ == ("__main__"):
    gt.verify_data()

    app = main_container.Gnumber()
    app.mainloop()
