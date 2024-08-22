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
    return random.randint(0, 2) 

def calculate_wage():
    """
    Description:
        This function calculates the daily wage for both full-day and part-time work.
    
    Parameter:
        None
    
    Return:
        int: The total full day and part-time wage of the employee.
    """
    return WAGE_PER_HOUR * FULL_DAY_HOUR , (WAGE_PER_HOUR/2) * FULL_DAY_HOUR 
    
def wage_for_month(full_day_wage , part_time_wage ):
    """
    Description:
        This function simulates the employee's attendance and wage computation over a 20-day work period.
        It tracks the number of full-time days, part-time days, and leave days.
    
    Parameter:
        full_day_wage (int): The wage for a full day of work.
        part_time_wage (int): The wage for a part-time day of work.
    
    Return:
        list: A list of daily wages for the 20-day period.
        int: The count of full-time days.
        int: The count of part-time days.
        int: The count of leave days.
    """
    i = 0
    wages = []
    full_time_count = 0
    part_time_count = 0
    leaves_count = 0
    while (i < 20):
        attendance = check_attendance()
        match(attendance):
            case 1:
                wages.append(full_day_wage)
                full_time_count += 1
            
            case 2:
                wages.append(part_time_wage)
                part_time_count +=1
            
            case(_):
                wages.append(0)
                leaves_count += 1
                
        i += 1
    return wages , full_time_count ,part_time_count ,leaves_count    
        
        
    
def main():

    
    full_day_wage , part_time_wage = calculate_wage()
    wages,full_time_count ,part_time_count ,leaves_count = wage_for_month(full_day_wage , part_time_wage )
    
    print (f"per day wages of employee: {wages} ")
    print(f"wages of month : ${sum(wages)}")
    print(f"Employye present full time : {full_time_count} days ") 
    print(f"Employye present part time : {part_time_count} days ") 
    print(f"Employye on leave : {leaves_count} days ") 
    

if __name__ == "__main__":
    main()
