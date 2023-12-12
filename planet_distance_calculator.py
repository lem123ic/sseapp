import requests

def get_planet_info(planet_name):
    # Replace 'YOUR_API_KEY' with an actual API key if required (not needed for this API)
    api_url = f'https://api.api-ninjas.com/v1/planets?name={planet_name}'

    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        planet_data = response.json()
        if planet_data:
            return planet_data[0]
    else:
        print("Error:", response.status_code, response.text)
        return None

def calculate_travel_time(distance, speed):
    # Speed is in km/h, convert it to km/s for consistency
    speed_per_second = speed / 3600
    
    # Calculate time = distance / speed
    time_in_seconds = distance / speed_per_second
    
    # Convert time to hours and minutes
    hours = int(time_in_seconds // 3600)
    minutes = int((time_in_seconds % 3600) // 60)
    
    return hours, minutes

# List of planets
planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Speed of the rocket in km/h
speed_of_rocket = 25000

for planet_name in planets:
    planet_info = get_planet_info(planet_name)

    if planet_info:
        distance_to_earth = planet_info.get("distance_light_year")
        
        if distance_to_earth is not None:
            # Calculate travel time
            travel_hours, travel_minutes = calculate_travel_time(distance_to_earth, speed_of_rocket)
            
            print(f"\nDetails for {planet_name}:")
            print(f"The distance from {planet_name} to Earth is approximately {distance_to_earth} light years.")
            print(f"Travel time by rocket (speed: {speed_of_rocket} km/h): {travel_hours} hours and {travel_minutes} minutes.")
        else:
            print(f"Failed to retrieve distance data for {planet_name}.")
    else:
        print(f"Failed to retrieve planet data for {planet_name}.")
