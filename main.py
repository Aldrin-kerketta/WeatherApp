import tkinter as tk
import fetch_weather_script

class WeatherAPPGUI:
    def __init__(self, master):
        self.master = master
        master.title('Weather Application')
        self.create_widget()

    def create_widget(self):
        self.city_label = tk.Label(self.master, text='Welcome to Weather application !!', padx=2, pady=20)
        self.city_label.pack()

        self.city_entry = tk.Entry(self.master)
        self.city_entry.pack()

        self.submit_btn = tk.Button(text='Get Weather', command=self.show)
        self.submit_btn.pack()

        self.city_info = tk.Label(self.master, text='')
        self.city_info.pack()

        self.weather_info = tk.Label(self.master, text='')
        self.weather_info.pack()

        self.temp_info = tk.Label(self.master, text='')
        self.temp_info.pack()

    def show(self):
        if self.city_entry:
            data = fetch_weather_script.fetch_weather(self.city_entry.get())
            self.weather_info.config(text=f"Weather: {data['weather']}")
            self.temp_info.config(text=f"Temp: {data['curr_temp']}")
            self.city_info.config(text=f"City: {data['city']}")

def main():
    root = tk.Tk()
    app = WeatherAPPGUI(root)
    root.geometry('350x350')
    root.mainloop()


if __name__ == '__main__':
    main()
