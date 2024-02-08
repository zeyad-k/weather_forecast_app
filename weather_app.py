import requests
import tkinter as tk
from tkinter import messagebox

# create main window 
root = tk.Tk()
root.title("Zeyad`s Weather Forecast")
root.rowconfigure(0, minsize=100)
root.columnconfigure(1, minsize=100)

api_key = '6adbbbb2d3eb1229c3047a93241e59bb'  # my api key 

 
 
 
city = tk.StringVar() # Create a StringVar variable to enter city name
entry = tk.Entry(root, textvariable=city)# create entry text input field
entry.grid(column=1, row=0, sticky="w", padx=10)

def validate_city_name(city):

    if not city.strip():  
        messagebox.showinfo("Error", "City name cannot be empty.")# Check if the city name is empty or contains only whitespace
        return 
 
# function 
def on_search():
 # Get the city name from the Entry widget
    city_name = city.get()
    validation_result = validate_city_name(city_name)

    if validation_result:
        # Create the URL using the city name
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
       #send request to the url
        response = requests.get(url)
        data = response.json()
    else:
        print("City name is valid")    

    # Create the URL using the city name
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
#send request to the url
    response = requests.get(url)
    data = response.json()


# check if the request is successful
    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        rain_chance = data['clouds']['all']
        pressure = data['main']['pressure']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        temp_label.config(text=f"Temperature : {temperature}°C")

        print(f"Humidity: {humidity}%")
        humidity_label.config(text=f"Humidity: {humidity}%")

        print(f"Wind Speed: {wind_speed} km/h")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")

        print(f"Rain Probability: {rain_chance}%")
        rain_chance_label.config(text=f"Rain Probability: {rain_chance}%")

        print(f"Pressure: {pressure} hPa")
        pressure_label.config(text=f"Pressure: {pressure} hPa")

    else:
        messagebox.showinfo("Error", "Failed to fetch data, please try again later.")



# Create a new Label widget for location and Add the Label widget to the grid
label = tk.Label(root, text="Location : ")
label.grid(column=0, row=0, sticky="w", padx=10)

# create a  search_button
search_button = tk.Button(root,text="search" ,relief=tk.RAISED,command=on_search)
search_button.grid(column=2, row=0, sticky="w", padx=10 )


 
# Create a Temperature Label widget  and Add the Label widget to the grid
temp_label = tk.Label(root, text="Temperature : ")
temp_label.grid(column=0, row=1, sticky="w", padx=15, pady=5)
# Create a humidity Label widget  and Add the Label widget to the grid
humidity_label = tk.Label(root, text="Humidity : ")
humidity_label.grid(column=0, row=2, sticky="w", padx=15, pady=5)
# Create a wind_speed Label widget  and Add the Label widget to the grid
wind_speed_label = tk.Label(root, text="wind_speed : ")
wind_speed_label.grid(column=0, row=3, sticky="w", padx=15, pady=5)
 # Create a humidity Label widget  and Add the Label widget to the grid
rain_chance_label = tk.Label(root, text="rain_chance : ")
rain_chance_label.grid(column=0, row=4, sticky="w", padx=15, pady=5)

# Create a humidity Label widget  and Add the Label widget to the grid
pressure_label = tk.Label(root, text="pressure : ")
pressure_label.grid(column=0, row=5, sticky="sw", padx=15, pady=5)




root.mainloop() 

 