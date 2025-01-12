import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    """Fetch and display weather data for the entered city."""
    API_KEY = "Place Your API Key HERE"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Extract weather details
        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        # Display weather details
        result_text.set(
            f"Weather in {city_name}:\n"
            f"Temperature: {temperature}°C\n"
            f"Description: {description.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")
    except KeyError:
        messagebox.showerror("Error", "City not found. Please check the city name and try again.")

# Create the main application window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#2d3436")  # Set background color

# Create and place widgets with styling
tk.Label(
    root, text="Weather App", font=("Helvetica", 18, "bold"), bg="#2d3436", fg="#ffffff"
).pack(pady=10)

tk.Label(
    root, text="Enter City Name:", font=("Arial", 12), bg="#2d3436", fg="#dfe6e9"
).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12), width=30, bg="#ffffff", fg="#2d3436")
city_entry.pack(pady=5)

fetch_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    bg="#0984e3",
    fg="#ffffff",
    activebackground="#74b9ff",
    activeforeground="#2d3436",
    command=get_weather,
)
fetch_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(
    root,
    textvariable=result_text,
    font=("Arial", 12),
    justify="left",
    wraplength=350,
    bg="#2d3436",
    fg="#dfe6e9",
)
result_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
