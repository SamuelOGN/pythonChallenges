#!/usr/bin/env python
# coding: utf-8

# In[ ]:


measures = ['inches', 'yards', 'miles', 'millimeters', 'centimeters', 'meters', 'kilometers']
index = ['1', '2', '3', '4', '5', '6', '7']
conversions = [12, 0.33333, 0.000189394, 304.8, 30.48, 0.3048, 0.0003048]

def input_number(num):
    number = num
    try:
        number = int(num)
    except ValueError:
        try:
            number = float(num)
        except ValueError:
            print(f"{number} is not a number. Please input an number")
        
    return number


def range_check(num):
    if num not in index:
        raise Exception("Please select a number from the conversion codes above")
    else:
        return num

    
def conversion(len_num, cov_id):
    index = int(conver_id) - 1
    answer = conversions[index] * len_num
    return answer
    

def pick_measure(conver_id):
    index = int(conver_id) - 1
    measure_name = measures[index]
    return measure_name



length = input_number(input("Enter number in feet: "))

print("")
print("These are the conversion codes:")
print("""Inches: 1
Yards: 2
Miles: 3
Millimeters: 4
Centimeters: 5
Meters: 6
Kilometers: 7""")
print("")

conver_id = range_check(input("Please select a measure you want to convert to: "))
converted = conversion(length, conver_id)
measure = pick_measure(conver_id)

print("")
print(f"{length} feet is equal to {converted} {measure}")

