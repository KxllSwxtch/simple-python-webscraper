import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get(
    url="https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XnWGOXX0mCg")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_='tombstone-container')
period_names = [item.find(class_='period-name').get_text() for item in items]
short_descs = [item.find(class_='short-desc').get_text() for item in items]
temps = [item.find(class_='temp').get_text() for item in items]

# Create a pandas data frame
weather_stuff = pd.DataFrame(
    {
        'Period': period_names,
        'Short Descriptions': short_descs,
        'Temperatures': temps
    }
)

weather_stuff.to_csv('weather.csv')
