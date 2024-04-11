import tkinter as tk


class WeatherAPPGUI:
    def __int__(self, master):
        self.master = master
        master.title('Weather Application')

def main():
    root = tk.Tk()
    app = WeatherAPPGUI()
    root.geometry('350x350')
    root.mainloop()


if __name__ == '__main__':
    main()
