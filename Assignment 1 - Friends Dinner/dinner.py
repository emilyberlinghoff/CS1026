# Developed by: Emily Berlinghoff
# Date: Feb 8, 2023
# Desc: Friends Dinner

# Starting variables
numPizza = 0
numPasta = 0
numFalafel = 0
numSteak = 0
numBeverage = 0

# Asking how many people are invited
numInvitees = int(input('Please enter the number of invitees:'))
print('\n')  # Extra line just to make it look neater

# Loop
x = 1
while x <= numInvitees:
    # Asking dietary preferences
    y = numInvitees
    print('Please enter the order details for invitee Number {}/{}'.format(x, y))
    # ^ The format is so there's no space between the numbers and the slash
    keto = input('Do you want a keto friendly meal? Type "y" for yes and "n" for no.')
    if keto != 'y':  # This is so everything but 'y' will be programmed as no
        keto = 'n'
    vegan = input('Do you want a vegan meal?')
    if vegan != 'y':
        vegan = 'n'
    gf = input('Do you want a Gluten-free meal?')
    if gf != 'y':
        gf = 'n'

    # Meals list
    if keto == 'y' and vegan == 'y' and gf == 'n':
        meal1 = 'pizza'
        numPizza = numPizza + 1  # numPizza was originally 0, but this adds 1 to the total
    elif keto == 'n' and vegan == 'y' and gf == 'n':
        meal1 = 'pasta'
        numPasta = numPasta + 1
    elif keto == 'y' and vegan == 'y' and gf == 'y':
        meal1 = 'falafel'
        numFalafel = numFalafel + 1
    elif keto == 'y' and vegan == 'n' and gf == 'y':
        meal1 = 'steak'
        numSteak = numSteak + 1
    else:
        meal1 = 'beverage'
        numBeverage = numBeverage + 1
    x = x + 1
    print('--------------------')
print('\n')
print("Moving on!")
print("\n")

# Cost of each meal
costPizza = numPizza * 44.50
costPasta = numPasta * 48.99
costFalafel = numFalafel * 52.99
costSteak = numSteak * 49.60
costBeverage = numBeverage * 5.99

# Billing receipt
tip = int(input('How much do you want to tip your server (% percent)?'))
print('\n')
print('You have ', numInvitees, 'invitees with the following orders:')
print("{} invitees ordered Pizza. The cost is: ${:.2f}".format(numPizza, round(numPizza * 44.50, 2)))
# ^ '{:.2f} and the format function are used to format the answer to 2 decimal places exactly
print("{} invitees ordered Pasta. The cost is: ${:.2f}".format(numPasta, round(numPasta * 48.99, 2)))
print("{} invitees ordered Falafel. The cost is: ${:.2f}".format(numFalafel, round(numFalafel * 52.99, 2)))
print("{} invitees ordered Steak. The cost is: ${:.2f}".format(numSteak, round(numSteak * 49.60, 2)))
print("{} invitees ordered only beverage. The cost is: ${:.2f}".format(numBeverage, round(numBeverage * 5.99, 2)))
subtotalBeforeTax = round(costPizza + costPasta + costFalafel + costSteak + costBeverage, 2)
print('\n')
print('Your subtotal before tax is: ${:.2f}'.format(subtotalBeforeTax))
subtotalAfterTax = round((costPizza + costPasta + costFalafel + costSteak + costBeverage) * 1.13, 2)
print('Your subtotal after tax is: ${:.2f}'.format(subtotalAfterTax))
total = round((costPizza + costPasta + costFalafel + costSteak + costBeverage) * 1.13 * (1 + tip / 100))
print('Your total cost after {}% tip is: ${:.2f}'.format(tip, total))
print('\n')
print('Thank you for eating here! Please come back soon!')
