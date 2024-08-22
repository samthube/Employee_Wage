'''
@Author: Samadhan Thube
@Date: 2024-08-22
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-22
@Title : Employee Wage Computation Problem
'''
import random

def check_attendance():
    """
    Description:
        This function generates a random value to determine attendance.
        
    Parameter:
        None
    
    Return:
        int: 1 if the employee is present, 0 if absent.
    """
    
    return random.randint(0, 1) 

def main():
    attendance = check_attendance()
    if attendance == 1:
        print("Employee is present")
    else:
        print("Employee is absent")

if __name__ == "__main__":
    main()