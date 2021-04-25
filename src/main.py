from hotels import Hotel, HotelSorter

# We define the hotels
hotel_list = [Hotel("Lakewood", 3, 110, 90, 80, 80), Hotel(
    "Bridgewood", 4, 160, 60, 110, 50), Hotel("Ridgewood", 5, 220, 150, 100, 40)]

# We receive the input
input_ = input('Entre com as informacoes da sua reserva:\n')

# Based on the input, we determine the ideal hotel to choose
ht_sorter = HotelSorter(input_, hotel_list)

best = ht_sorter.find_best_hotel()

print(best)
