per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = int(input("Please, enter your deposit amount:"))

max_profit = 0
max_profit_key = ""

for key in per_cent:
    bank_percent = per_cent[key]
    profit = deposit / 100 * bank_percent
    if profit > max_profit:
        max_profit = profit
        max_profit_key = key

print("Max profit you might receive is {} at bank {}".format(max_profit, max_profit_key))
