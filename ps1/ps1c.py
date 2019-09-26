#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:38:59 2019

@author: kunal
"""
total_cost = 1000000
starting_salary = int(input("Enter your annual salary: "))
steps = 0
semi_annual_raise, r = 0.07, 0.04
epsilon = 100
low, high = 0, 10000
portion_saved_integer = high
down_payment = 0.25 * total_cost
isPossible = True

while True:  
    steps += 1
    current_savings = 0.0
    months = 0
    annual_salary = starting_salary
    portion_saved = portion_saved_integer / 10000
    monthly_savings = portion_saved * (annual_salary/12)
    
    while months <= 36:
        current_savings += monthly_savings + ((current_savings*r)/12)
        months += 1
        
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_savings = portion_saved * (annual_salary/12)
            
    if abs(current_savings - down_payment) <= epsilon:
        break
    
    if current_savings < down_payment:
        low = portion_saved_integer
        
    else:
        high = portion_saved_integer
        
    if low >= high:
        isPossible = False
        break
    
    portion_saved_integer = (low + high) // 2
    
if isPossible:
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:", steps)
    
else:
    print("It is not possible to pay the down payment in three years")
