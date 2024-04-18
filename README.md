# Weather Application

This is a simple weather application that fetches weather information for a given city using the
OpenWeatherMap API and displays it in a graphical user interface (GUI) built in TKinter.

## Files

*fetch_weather_script.py*

This file contains the function 'fetch_weather(city)' that retrieves weather data for a given city
using the OpenWeatherMap API. It returns a dictionary containing weather description, current
temperature, and city name.

*main.py*

This is the main script that creates the GUI for the weather application using Tkinter. It allows
users to input a city name, fetches weather data using the '**fetch_weather**' function from 
'**fetch_weather_script.py**', and displays the weather information in the GUI.

## Usage

1. Ensure you have Python installed on your system,
2. Clone this repository to your local machine.
3. Install the required dependencies:

    `pip install requests`

4. Run the '**main.py**' script:

    `python main.py`

5. Enter the name of the city for which you want to fetch weather information in the provided input 
field.

6. Click the  "**Get Weather**" button to fetch and display weather information.

## Dependencies

* requests: This package is used to make HTTP requests to OpenWeatherAPI.

## Contributing 

Contributions are welcome! If you have any suggestions or improvements, feel free to open an
issue or create a pull request.

## License 

This project is licensed under the MIT License. See the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) file for details. 