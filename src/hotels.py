import re
class Hotel:

    def __init__(self, name, classification, tax_week, tax_weekend):
        self.name = name
        self.classification = classification
        self.tax_week = tax_week
        self.tax_weekend = tax_weekend


class HotelSorter:

    def __init__(self, input, hotel_list):
        self.hotel_list = hotel_list
        self.input = input
        pass

    def input_parser(self, input):
        """
        Method that parses the essential data from the input
        """

        # Extracting the client type
        client_type = input.split(':')[0]

        # Extracting the dates between brackets using regex
        dates = re.findall(r'\(.*?\)', input)

        # We transform our dates
