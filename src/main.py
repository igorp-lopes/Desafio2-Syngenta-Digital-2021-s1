from hotels import Hotel, HotelSorter

sorting = HotelSorter(
    "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)", [])

hotel = Hotel("Lakewood", 3, 110, 90, 80, 80)
hotel.calculate_stay_price([False, False, False], 'Regular')

temp = 0
