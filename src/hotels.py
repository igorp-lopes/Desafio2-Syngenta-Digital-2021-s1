class Hotel:

    def __init__(self, name, classification, tax_week, tax_weekend):
        self.name = name
        self.classification = classification
        self.tax_week = tax_week
        self.tax_weekend = tax_weekend


class HotelSorter:

    def __init__(self, input, hotel_list):
        self.hotel_list = hotel_list
        pass
