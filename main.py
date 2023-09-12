from menu import Menu
from franchise import Franchise
from data import data
from business import Business

# Testing

# Menus
brunch = Menu('Brunch', data['items_brunch'], 11, 16)
early_brid = Menu('Early Bird', data['items_early_bird'], 15, 18)
dinner = Menu('Dinner', data['items_dinner'], 17, 22)
kids = Menu('Kids', data['items_kids'], 11, 21)
arepas_menu = Menu('Arepas Menu', [data['arepas_menu']], 10, 22)

# print(brunch)
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_brid.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Franchise
flagship_store = Franchise("1232 West End Road",[brunch, early_brid, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_brid, dinner, kids])

# print(flagship_store.available_menus(17))

# Business
business_1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

business_2 = Business("Take a' Arepa", arepas_place)

print(business_1)
