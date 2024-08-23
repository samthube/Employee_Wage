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
    
    def __init__(self):
        self.daily_wages = []
        self.total_days = 0
        self.total_hours = 0
        self.full_time_count = 0
        self.part_time_count = 0
        self.leaves_count = 0
         
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
        
    def wage_for_month(self, full_day_wage, part_time_wage):
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
        
        while self.total_days < self.MAX_WORKING_DAYS and self.total_hours < self.MAX_WORKING_HOURS:
            attendance = 2 if self.total_hours == 96 else self.check_attendance()
            
            match attendance:
                case 1:
                    self.daily_wages.append(full_day_wage)
                    self.full_time_count += 1
                    self.total_days += 1
                    self.total_hours += self.FULL_DAY_HOUR
                
                case 2:
                    self.daily_wages.append(part_time_wage)
                    self.part_time_count += 1
                    self.total_days += 1
                    self.total_hours += self.FULL_DAY_HOUR / 2
                
                case 0:
                    self.daily_wages.append(0)
                    self.leaves_count += 1
                    
        return self.daily_wages, self.full_time_count, self.part_time_count, self.leaves_count, self.total_hours
        
def main():
    employee_object = Employee_Wage()
    full_day_wage, part_time_wage = employee_object.calculate_wage()
    daily_wages, full_time_count, part_time_count, leaves_count, hours = employee_object.wage_for_month(full_day_wage, part_time_wage)
    
    print(f"Per day wages of employee: {daily_wages}")
    print(f"Total Wage of the month: ${sum(daily_wages)}")
    print(f"Employee present full time: {full_time_count} days") 
    print(f"Employee present part time: {part_time_count} days") 
    print(f"Employee on leave: {leaves_count} days") 
    print(f"Total hours worked: {hours}")
    

if __name__ == "__main__":
    main()
