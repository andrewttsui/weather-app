This is a quick weather app built for the tech.la engineering application.

It uses the OpenWeather API to get weather information for specific locations.

In order to remove any ambiguity between locations with the same name, I used the city id parameter. In city.list.json, one will find a list of cities and each city has its own unique id.

To run the app, clone the repo into your local machine. Once inside the directory, run 'python3 input.py' in your terminal. It will prompt you for the city id; use the city id found in city.list.json.