number_of_tickets = int(input("Enter number of tickets you want to buy:"))
ages = []
for i in range (0, number_of_tickets):
    ages.append(int(input("Enter age of participant {}:".format(i+1))))

result = 0
for age in ages:
    if 17 < age < 25:
        result = result + 990
    if age > 24:
        result = result + 1390

applied_discount = False
discount = 0
if number_of_tickets > 3:
    discount = result / 10
    result = result - discount
    applied_discount = True

print("Your final amount is: {}".format(result))
if applied_discount:
    print("Your discount is: {}".format(discount))