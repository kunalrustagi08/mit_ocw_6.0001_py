"""
Created on Mon Sep 23 10:16:27 2019

@author: kunal
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))

portion_down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12.0
portion_saved *=  monthly_salary
current_savings = 0
r = 0.04
months = 0

while(current_savings <= portion_down_payment):
    
    current_savings += portion_saved + ((current_savings*r)/12)
    months += 1

print("Number of months:", months)
