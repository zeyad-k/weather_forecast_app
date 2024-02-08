# Import necessary libraries
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to fetch weather data
def get_weather():
    # Retrieve the city name from the entry field
    city_name = city.get()
    
	# Validate if the city name is empty
    if not city_name:
        messagebox.showwarning("Empty City", "Please enter a city name.")
        return
    # Validate if the city name contains numbers
    elif any(char.isdigit() for char in city_name):
        messagebox.showwarning("Invalid Input", "Please enter a valid city name without numbers.")
        return

	 # API request to fetch weather data based on the city name
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    
    # Check if the API request was successful
    if response.status_code == 200:
        data = response.json() # Parse JSON response
        update_labels(data) # Update GUI labels with weather information
    else:
        messagebox.showinfo("Error", "Failed to fetch data, please try again later.")
        
# Function to update GUI labels with weather information
def update_labels(data):
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    rain_chance = data['clouds']['all']
    pressure = data['main']['pressure']
    
	# Update label texts with weather information
    temp_label.config(text=f"Temperature: {temperature}°C")
    humidity_label.config(text=f"Humidity: {humidity}%")
    wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")
    rain_chance_label.config(text=f"Rain Probability: {rain_chance}%")
    pressure_label.config(text=f"Pressure: {pressure} hPa")

# Create the main window
root = tk.Tk()
root.title("Zeyad's Weather Forecast")

# API key for OpenWeatherMap
api_key = '6adbbbb2d3eb1229c3047a93241e59bb'

# Set styles for ttk widgets
style = ttk.Style()
style.configure('TButton', foreground='blue', font=('Arial', 10))
style.configure('TLabel', font=('Arial', 12))

# Create StringVar for city entry
city = tk.StringVar()
entry = ttk.Entry(root, textvariable=city)
entry.grid(column=1, row=0, padx=15, pady=10, sticky='w')

# Label for the city entry
label = ttk.Label(root, text="Location: ", style='TLabel')
label.grid(column=0, row=0, padx=15, pady=10, sticky='w')

# Search button to fetch weather data
search_button = ttk.Button(root, text="Search", style='TButton', command=get_weather)
search_button.grid(column=2, row=0, padx=15, pady=10, sticky='w')

# Labels to display weather information
temp_label = ttk.Label(root, text="Temperature: ", style='TLabel')
temp_label.grid(column=0, row=1, padx=15, pady=10, sticky='w')

humidity_label = ttk.Label(root, text="Humidity: ", style='TLabel')
humidity_label.grid(column=0, row=2, padx=15, pady=10, sticky='w')

wind_speed_label = ttk.Label(root, text="Wind Speed: ", style='TLabel')
wind_speed_label.grid(column=0, row=3, padx=15, pady=10, sticky='w')

rain_chance_label = ttk.Label(root, text="Rain Probability: ", style='TLabel')
rain_chance_label.grid(column=0, row=4, padx=15, pady=10, sticky='w')

pressure_label = ttk.Label(root, text="Pressure: ", style='TLabel')
pressure_label.grid(column=0, row=5, padx=15, pady=10, sticky='w')

# Start the GUI event loop
root.mainloop()
