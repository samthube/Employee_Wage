'''
@Author: Samadhan Thube
@Date: 2024-08-22
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-22
@Title : Employee Wage Computation Problem
'''

import random

WAGE_PER_HOUR = 20 
FULL_DAY_HOUR = 8

def check_attendance():
    """
    Description:
        This function generates a random value to determine the attendance of an employee.
    
    Parameter:
        None
    
    Return:
        int: Returns 1 if the employee is present, 0 if absent.
    """
    return random.randint(0, 1) 

def calculate_wage():
    """
    Description:
        This function calculates the daily wage for an employee based on a full day of work.
    
    Parameter:
        None
    
    Return:
        int: The total daily wage of the employee.
    """
    return WAGE_PER_HOUR * FULL_DAY_HOUR  
    

def main():

    attendance = check_attendance()
    
    if attendance == 1:
        print("Employee is present")
        print(f"Daily Wage Of Employee is: ${calculate_wage()}")
    else:
        print("Employee is absent, no wage")

if __name__ == "__main__":
    main()
