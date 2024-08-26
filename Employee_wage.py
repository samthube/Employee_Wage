'''
@Author: Samadhan Thube
@Date: 2024-08-22
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-22
@Title : Employee Wage Computation Problem
'''

import random

class Employee_Wage:
    
    WAGE_PER_HOUR = 20 
    FULL_DAY_HOUR = 8
    MAX_WORKING_DAYS = 20
    MAX_WORKING_HOURS = 100
    
    daily_wages = []
    total_days = 0
    total_hours = 0
    full_time_count = 0
    part_time_count = 0
    leaves_count = 0
    
    @classmethod
    def check_attendance(cls):
        """
        Description:
            This function generates a random value to determine the attendance of an employee.
        
        Parameter:
            None
        
        Return:
            int: Returns 0 if the employee is absent, 1 if full-time, 2 if part-time.
        """
        return random.randint(0, 2) 

    @classmethod
    def calculate_wage(cls):
        """
        Description:
            This function calculates the daily wage for both full-day and part-time work.
        
        Parameter:
            None
        
        Return:
            tuple: The wages for a full day and a part-time day.
        """
        return cls.WAGE_PER_HOUR * cls.FULL_DAY_HOUR, (cls.WAGE_PER_HOUR // 2) * cls.FULL_DAY_HOUR 

    @classmethod
    def wage_for_month(cls):
        """
        Description:
            This class method simulates the employee's attendance and wage computation over a 20-day or 100 hours work period.
            It tracks the number of full-time days, part-time days, and leave days using class variables.
        
        Parameter:
            None
        
        Return:
            tuple: A list of daily wages for the 20-day period, counts of full-time, part-time, leave days, and total hours worked.
        """
        full_day_wage, part_time_wage = cls.calculate_wage()
        
        while cls.total_days < cls.MAX_WORKING_DAYS and cls.total_hours < cls.MAX_WORKING_HOURS:
            attendance = 2 if cls.total_hours == 96 else cls.check_attendance()
            
            match attendance:
                case 1:
                    cls.daily_wages.append(full_day_wage)
                    cls.full_time_count += 1
                    cls.total_days += 1
                    cls.total_hours += cls.FULL_DAY_HOUR
                
                case 2:
                    cls.daily_wages.append(part_time_wage)
                    cls.part_time_count += 1
                    cls.total_days += 1
                    cls.total_hours += cls.FULL_DAY_HOUR / 2
                
                case 0:
                    cls.daily_wages.append(0)
                    cls.leaves_count += 1
                    
        return cls.daily_wages, cls.full_time_count, cls.part_time_count, cls.leaves_count, cls.total_hours
        
def main():
    daily_wages, full_time_count, part_time_count, leaves_count, hours = Employee_Wage.wage_for_month()
    
    print(f"Per day wages of employee: {daily_wages}")
    print(f"Total Wage of the month: ${sum(daily_wages)}")
    print(f"Employee present full time: {full_time_count} days") 
    print(f"Employee present part time: {part_time_count} days") 
    print(f"Employee on leave: {leaves_count} days") 
    print(f"Total hours worked: {hours}")
    

if __name__ == "__main__":
    main()
