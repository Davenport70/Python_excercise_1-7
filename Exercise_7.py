# SIMPLEST - Restaurant Waiter Helper

# User Stories
# starter code
menu = ['falafel', 'HuMMus', 'coUScous', 'Bacalhau a Bras']
food_order = []
#1
# AS a Use I want to be able to see the menu in a formated way, so that I can order my meal.
print(menu[0].capitalize())
print(menu[1].capitalize())
print(menu[2].capitalize())
print(menu[3].capitalize())
#2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
order1 = input('What would you like to add to order?: ').capitalize()
food_order.append(order1)
order2 = input('What would you like to add to order?: ').capitalize()
food_order.append(order2)
order3 = input('What would you like to add to order?: ').capitalize()
food_order.append(order3)

#3
# As a user, I want to have my order read back to me in formated way so I know what I ordered.

print(food_order)

# DOD
# its own project on your laptop and Github
# be git tracked
# have 5 commits mininum!