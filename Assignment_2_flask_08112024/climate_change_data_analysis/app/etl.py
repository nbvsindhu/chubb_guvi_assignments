import requests
import pandas as pd
from app import db
from app.models import ClimateData

# ETL function for OpenWeatherMap data (JSON)
def fetch_openweathermap_data():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key'
    response = requests.get(url).json()
    
    # Extract relevant data
    temperature = response['main']['temp']
    precipitation = response['rain']['1h'] if 'rain' in response else 0
    date = pd.to_datetime(response['dt'], unit='s').date()
    
    # Store data in DB
    climate_data = ClimateData(source='OpenWeatherMap', temperature=temperature, precipitation=precipitation, date=date)
    db.session.add(climate_data)
    db.session.commit()

# ETL function for NOAA (CSV)
def fetch_noaa_data():
    df = pd.read_csv('data/noaa_data.csv')
    
    for index, row in df.iterrows():
        climate_data = ClimateData(source='NOAA', temperature=row['temperature'], precipitation=row['precipitation'], date=row['date'])
        db.session.add(climate_data)
    
    db.session.commit()

# ETL function for NASA (CSV)
def fetch_nasa_data():
    df = pd.read_csv('data/nasa_data.csv')
    
    for index, row in df.iterrows():
        climate_data = ClimateData(source='NASA', temperature=row['temperature'], precipitation=row['precipitation'], date=row['date'])
        db.session.add(climate_data)
    
    db.session.commit()

# ETL function for CSV data (General)
def load_data_from_csv():
    df = pd.read_csv('data/weather_data.csv')
    
    for index, row in df.iterrows():
        climate_data = ClimateData(source='CSV', temperature=row['temperature'], precipitation=row['precipitation'], date=row['date'])
        db.session.add(climate_data)
    
    db.session.commit()

# Function to scrape HTML data (for example, precipitation data)
def fetch_precipitation_data():
    # Scraping logic (for demo, assuming simple HTML table)
    with open('data/precipitation_data.html', 'r') as file:
        html_content = file.read()
    
    # Assume scraping and parsing logic here
    # For now, we directly insert the data for simplicity.
    climate_data = ClimateData(source='HTML', temperature=20, precipitation=5, date="2024-01-01")
    db.session.add(climate_data)
    db.session.commit()

