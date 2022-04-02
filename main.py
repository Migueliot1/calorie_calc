import ssl
import urllib.request, urllib.parse, urllib.error
from selectorlib import Extractor

class Temperature:

    url = 'https://www.timeanddate.com/weather/'

    def __init__(self, country, city):

        self.country = country
        self.city = city

    def get(self):

        '''This method extracts current temperature from timeanddate.com/weather 
        based on passed city and country'''

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = self.url + self.country + '/' + self.city # Make final URL with country and city
        html = urllib.request.urlopen(url, context=ctx) # Connect to the created URL
        data = html.read().decode() # Save all data from URL and decode it from bytes

        extractor = Extractor.from_yaml_file('temperature.yaml') # Extract only the degrees value out of data
        raw_result = extractor.extract(data)

        result = float(raw_result['temp'].replace("°C", "")) # Remove everything except number and save it

        return result


class Calories:

    def __init__(self, weight, height, age, country, city):

        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = Temperature(country, city)

    def calculate(self):

        # put every piece of data into the formula, calculate calories/day amount and return that value

        return None
