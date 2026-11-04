rice_price = 45
sugar_price = 40
oil_price = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

print("Rice price:", rice_price)
print("Sugar price:", sugar_price)
print("Oil price:", oil_price)

print("Rice quantity:", rice_qty)
print("Sugar quantity:", sugar_qty)
print("Oil quantity:", oil_qty)

rice_total = rice_price * rice_qty
sugar_total = sugar_price * sugar_qty
oil_total = oil_price * oil_qty

print("Rice total:", rice_total)
print("Sugar total:", sugar_total)
print("Oil total:", oil_total)

total_bill = rice_total + sugar_total + oil_total

print("Total bill:", total_bill)

total_integer = int(total_bill)

print("Total bill as integer:", total_integer)

total_string = str(total_bill)

print("Total bill as string:", total_string)

import random

delivery_charge = random.randint(5, 10)

print("Delivery charge:", delivery_charge)

final_bill = total_bill + delivery_charge

print("Final bill:", final_bill)