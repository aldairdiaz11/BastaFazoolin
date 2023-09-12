from menu import Menu
from franchise import Franchise
from data import data


# Testing
brunch = Menu('Brunch', data['items_brunch'], 11, 16)
early_brid = Menu('Early Bird', data['items_early_bird'], 15, 18)
dinner = Menu('Dinner', data['items_dinner'], 17, 22)
kinds = Menu('Kids', data['items_kids'], 11, 21)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_brid.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
