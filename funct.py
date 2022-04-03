import ssl
import urllib.request, urllib.parse, urllib.error
from selectorlib import Extractor

class Temperature:

    base_url = 'https://www.timeanddate.com/weather/'
    base_yaml = 'temperature.yaml'

    def __init__(self, country, city):

        # Replace spaces with '-' for both country and city strings
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')

    def _build_url(self):

        '''Builds proper URL string adding country and city'''

        url = self.base_url + self.country + '/' + self.city

        return url
    
    def _scrape(self, data):

        '''Scrapes timeanddate.com and returns current temperature 
        based on the instance's location'''

        extractor = Extractor.from_yaml_file(self.base_yaml) # Extract only the degrees value out of data
        raw_result = extractor.extract(data)

        result = float(raw_result['temp'].replace("°C", "")) # Remove everything except number and save it

        return result

    def get(self):

        '''This method extracts current temperature from timeanddate.com/weather 
        based on instance's country and city values'''

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        url = self._build_url()
        html = urllib.request.urlopen(url, context=ctx) # Connect to the created URL
        data = html.read().decode() # Save all data from URL and decode it from bytes

        result = self._scrape(data)

        return result


class Calories:

    def __init__(self, weight, height, age, country, city):

        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = Temperature(country, city)

    def calculate(self):

        '''Return calculated calories per day value out of 
        instance's weight, height, age and temperature'''

        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature.get() * 10

        return result
