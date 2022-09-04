# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 00:13:50 2022

@author: jingy
"""

# 2.12.1 LAB
user_num = int(input())
x = int(input())
if x != 0:
    first_out = user_num//x
    second_out = first_out//x
    third_out = second_out//x
    print(f'{first_out} {second_out} {third_out}')
if x == 0:
    print('ERROR')

# 2.13.1 LAB
gas_mileage = float(input())
cost_gas = float(input())
cost_20mi = (20/gas_mileage)*cost_gas
cost_75mi = (75/gas_mileage)*cost_gas
cost_500mi = (500/gas_mileage)*cost_gas
print(f'{cost_20mi:.2f} {cost_75mi:.2f} {cost_500mi:.2f}')

# 2.14.1 LAB 
age_years = float(input())
weight_pounds = float(input())
heart_rate_bpm = float(input())
time_mins = float(input())
cals_burnt = ((age_years * 0.2757) + (weight_pounds * 0.03295) + (heart_rate_bpm * 1.0781) - 75.4991) * time_mins / 8.368
print(f'Calories: {cals_burnt:.2f} calories')

# 2.15.1 LAB
import math
x = float(input())
y = float(input())
z = float(input())
x_power_to_z = x**z
x_power_y_power_z = x**(y**z)
x_minus_y_abs = math.fabs(x-y)
sqrt_x_power_z = math.sqrt(x_power_to_z)
print(f'{x_power_to_z:.2f} {x_power_y_power_z:.2f} {x_minus_y_abs:.2f} {sqrt_x_power_z:.2f}')

# 2.16.1 LAB
f0 = float(input()) # initial key frequency in Hertz
r = 2**(1/12)
freq = [(f'{(f0 * (r**i)):.2f}') for i in range(0,5)]
print(*freq, sep = ' ')
# 2.18.1 LAB
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))

# FIXME (1): Finish reading other items into variables, then output the three ingredients
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print(f'\nLemonade ingredients - yields {servings:.2f} servings\n{lemon_juice_cups:.2f} cup(s) lemon juice\n{water:.2f} cup(s) water\n{agave_nectar:.2f} cup(s) agave nectar\n')

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
desired_servings = float(input('How many servings would you like to make?\n'))
multiplier = desired_servings/servings
print(f'\nLemonade ingredients - yields {desired_servings:.2f} servings\n{lemon_juice_cups*multiplier:.2f} cup(s) lemon juice\n{water*multiplier:.2f} cup(s) water\n{agave_nectar*multiplier:.2f} cup(s) agave nectar\n')

# FIXME (3): Convert and output the ingredients from (2) to gallons
print(f'Lemonade ingredients - yields {desired_servings:.2f} servings\n{lemon_juice_cups*multiplier/16:.2f} gallon(s) lemon juice\n{water*multiplier/16:.2f} gallon(s) water\n{agave_nectar*multiplier/16:.2f} gallon(s) agave nectar')

# 2.19.1 LAB
item_name = input('Enter food item name:\n')

# FIXME (1): Finish reading item price and quantity, then output a receipt
item_price = float(input('Enter item price:\n'))
item_quant = int(input('Enter item quantity:\n'))
cost = item_price*item_quant
print(f'\nRECEIPT\n{item_quant} {item_name} @ ${item_price:.2f} = ${cost:.2f}\nTotal cost: ${cost:.2f}\n')

# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
item2_name = input('\nEnter second food item name:\n')
item2_price = float(input('Enter item price:\n'))
item2_quant = int(input('Enter item quantity:\n'))
cost2 = item2_price*item2_quant
total_cost = cost+cost2
print(f'\nRECEIPT\n{item_quant} {item_name} @ ${item_price:.2f} = ${cost:.2f}\n{item2_quant} {item2_name} @ ${item2_price:.2f} = ${cost2:.2f}\nTotal cost: ${total_cost:.2f}\n')

# FIXME (3): Add a gratuity and total with tip to the second receipt
print(f'15% gratuity: ${0.15*total_cost:.2f}')
print(f'Total with tip: ${(0.15*total_cost)+total_cost:.2f}')








