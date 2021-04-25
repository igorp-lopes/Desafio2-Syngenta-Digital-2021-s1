import re
class Hotel:

    def __init__(self, name, classification, price_week, price_weekend):
        self.name = name
        self.classification = classification
        self.price_week = price_week
        self.price_weekend = price_weekend
        self.total_price = 0

    def calculate_stay_price(self, dates):
        """
        Method that determines the total price paid for staying at the hotel
        for the given dates
        """

        price = 0
        for date in dates:
            # If the current day is a weekend day
            if(date):
                price += self.price_weekend
            else:
                price += self.price_week

        self.total_price = price

class HotelSorter:

    def __init__(self, input, hotel_list):
        self.hotel_list = hotel_list
        self.client_type, self.dates = self.input_parser(input)


    def input_parser(self, input):
        """
        Method that parses the essential data from the input
        """

        # Extracting the client type
        client_type = input.split(':')[0]

        # Extracting the dates between brackets using regex
        dates = re.findall(r'\(.*?\)', input)

        # We transform our dates relative to their respective weekday, False for weekdays and True for weekend days
        dates = [True if date == ('(sat)' or '(sun)')
                 else False for date in dates]

        return client_type, dates
