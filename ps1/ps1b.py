#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:47:40 2019

@author: kunal
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
monthly_savings = portion_saved * (annual_salary/12.0)
current_savings = 0.0
r = 0.04
months = 0

while(current_savings <= portion_down_payment):
    
    current_savings += monthly_savings + ((current_savings*r)/12)
    months += 1
    if(months%6 == 0):
        annual_salary += annual_salary * semi_annual_raise
        monthly_savings = portion_saved * (annual_salary/12.0)

print("Number of months:", months)
