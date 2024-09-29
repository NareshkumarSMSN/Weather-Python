import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    # Make a request to the API
    response = requests.get(complete_url)
    
    # Convert the response to JSON format
    data = response.json()
    
    # Check the "cod" field in the response to see if the city was found
    if data.get("cod") == 200:  # '200' indicates successful response
        main = data["main"]
        weather = data["weather"][0]
        
        # Extract weather information
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        # Display the weather information in the labels
        label_city.config(text=f"City: {city_name}")
        label_temp.config(text=f"Temperature: {temperature}°C")
        label_pressure.config(text=f"Atmospheric Pressure: {pressure} hPa")
        label_humidity.config(text=f"Humidity: {humidity}%")
        label_desc.config(text=f"Description: {weather_description}")
    
    else:
        # If city is not found or another error occurred
        messagebox.showerror("Error", f"Error: {data.get('message', 'City not found')}. Please check the city name.")

# Function that runs when the button is clicked
def fetch_weather():
    city_name = entry_city.get()
    api_key = "b16044a87ee96615092a554d95f34ad3"  # Replace with your actual API key
    get_weather(city_name, api_key)

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Weather App")

# Label for instructions
label_instruction = tk.Label(root, text="Enter City Name:")
label_instruction.pack(pady=10)

# Entry box to enter city name
entry_city = tk.Entry(root, width=30)
entry_city.pack(pady=5)

# Button to trigger the API request
button_get_weather = tk.Button(root, text="Get Weather", command=fetch_weather)
button_get_weather.pack(pady=10)

# Labels to display weather info
label_city = tk.Label(root, text="", font=("bold", 14))
label_city.pack(pady=5)

label_temp = tk.Label(root, text="")
label_temp.pack(pady=5)

label_pressure = tk.Label(root, text="")
label_pressure.pack(pady=5)

label_humidity = tk.Label(root, text="")
label_humidity.pack(pady=5)

label_desc = tk.Label(root, text="")
label_desc.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
