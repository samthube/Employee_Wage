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
MAX_WORKING_DAYS = 20
MAX_WORKING_HOURS =100

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
    return WAGE_PER_HOUR * FULL_DAY_HOUR , (WAGE_PER_HOUR//2) * FULL_DAY_HOUR 
    
def wage_for_month(full_day_wage, part_time_wage):
    """
    Description:
        This function simulates the employee's attendance and wage computation over a 20-day or 100 hours work period.
        It tracks the number of full-time days, part-time days, and leave days.
    
    Parameter:
        full_day_wage (int): The wage for a full day of work.
        part_time_wage (int): The wage for a part-time day of work.
    
    Return:
        tuple: A list of daily wages for the 20-day period, counts of full-time, part-time, leave days, and total hours worked.
    """
    
    daily_wages = []
    total_days = 0
    total_hours = 0
    full_time_count = 0
    part_time_count = 0
    leaves_count = 0
    
    while total_days < MAX_WORKING_DAYS  and total_hours < MAX_WORKING_HOURS:
        attendance = 2 if total_hours == 96 else check_attendance()
        
        match attendance:
            case 1:
                daily_wages.append(full_day_wage)
                full_time_count += 1
                total_days += 1
                total_hours += FULL_DAY_HOUR
            
            case 2:
                daily_wages.append(part_time_wage)
                part_time_count += 1
                total_days += 1
                total_hours += FULL_DAY_HOUR / 2
            
            case 0:
                daily_wages.append(0)
                leaves_count += 1
                
    
    return daily_wages, full_time_count, part_time_count, leaves_count, total_hours
    
def main():
    full_day_wage, part_time_wage = calculate_wage()
    daily_wages, full_time_count, part_time_count, leaves_count, hours = wage_for_month(full_day_wage, part_time_wage)
    
    print(f"Per day wages of employee: {daily_wages}")
    print(f"Total Wage of the month: ${sum(daily_wages)}")
    print(f"Employee present full time: {full_time_count} days") 
    print(f"Employee present part time: {part_time_count} days") 
    print(f"Employee on leave: {leaves_count} days") 
    print(f"Total hours worked: {hours}")
    

if __name__ == "__main__":
    main()
