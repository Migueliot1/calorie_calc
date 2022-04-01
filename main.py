class Temperature:

    def __init__(self, city, country):

        self.city = city
        self.country = country

    def get(self):

        # do the webscrape of city and country to check the weather

        return None


class Calories_Data:

    def __init__(self, weight, height, age, city, country):

        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = Temperature(city=city, country=country)

    def calculate(self):

        # put every piece of data into the formula, calculate calories/day amount and return that value

        return None