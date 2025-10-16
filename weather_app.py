import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if data.get('cod') != 200:
            messagebox.showerror("Error", f"City {city} not found!")
            return

        weather_info = f"City: {data['name']}, {data['sys']['country']}\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Humidity: {data['main']['humidity']}%\n"
        weather_info += f"Weather: {data['weather'][0]['description'].title()}"

        weather_label.config(text=weather_info)

    except Exception as e:
        messagebox.showerror("Error", f"Error fetching weather: {e}")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x250")

city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_btn.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
weather_label.pack(pady=10)

root.mainloop()
