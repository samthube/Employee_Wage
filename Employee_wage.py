'''
@Author: Samadhan Thube
@Date: 2024-08-24
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-24
@Title : Employee Wage Computation Problem 
'''

import random

class Employee_Wage:
    
    def __init__(self, wage_per_hour, full_day_hour, max_working_days, max_working_hours):
        """
        Description:
            Initializes the Employee_Wage object with company-specific details.
        
        Parameter:
            wage_per_hour (int): The wage per hour for the employee.
            full_day_hour (int): The number of hours considered a full day.
            max_working_days (int): The maximum number of working days in a month.
            max_working_hours (int): The maximum number of working hours in a month.
            
        Return:
            None
        """
        self.wage_per_hour = wage_per_hour
        self.full_day_hour = full_day_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        
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

    def calculate_wage(self):
        """
        Description:
            This function calculates the daily wage for both full-day and part-time work.
        
        Parameter:
            None
        
        Return:
            tuple: The wages for a full day and a part-time day.
        """
        return self.wage_per_hour * self.full_day_hour, (self.wage_per_hour // 2) * self.full_day_hour

    def wage_for_month(self, full_day_wage, part_time_wage):
        """
        Description:
            This function simulates the employee's attendance and wage computation over a 20-day or 100 hours work period.
            It tracks the number of full-time days, part-time days, and leave days.
        
        Parameter:
            full_day_wage (int): The wage for a full day of work.
            part_time_wage (int): The wage for a part-time day of work.
        
        Return:
            tuple: A list of daily wages for the period, counts of full-time, part-time, leave days, and total hours worked.
        """
        
        while self.total_days < self.max_working_days and self.total_hours < self.max_working_hours:
            attendance = 2 if self.total_hours == 96 else self.check_attendance()
            
            match attendance:
                case 1:
                    self.daily_wages.append(full_day_wage)
                    self.full_time_count += 1
                    self.total_days += 1
                    self.total_hours += self.full_day_hour
                
                case 2:
                    self.daily_wages.append(part_time_wage)
                    self.part_time_count += 1
                    self.total_days += 1
                    self.total_hours += self.full_day_hour / 2
                
                case 0:
                    self.daily_wages.append(0)
                    self.leaves_count += 1
                    
        return self.daily_wages, self.full_time_count, self.part_time_count, self.leaves_count, self.total_hours
 
         
def main():
    wage_per_hour = int(input("Enter wage per hour: "))
    full_day_hour = int(input("Enter full day hour: "))
    max_working_days = int(input("Enter total working days of month: "))
    max_working_hours = int(input("Enter total working hours of month: "))
    
    employee_object = Employee_Wage(wage_per_hour,full_day_hour,max_working_days,max_working_hours)
    full_day_wage, part_time_wage = employee_object.calculate_wage()
    daily_wages, full_time_count, part_time_count, leaves_count, hours = employee_object.wage_for_month(full_day_wage, part_time_wage)
    
    print("-"*234)
    
    print(f"Per day wages of employee: {daily_wages}")
    print(f"Total Wage of the month: ${sum(daily_wages)}")
    print(f"Employee present full time: {full_time_count} days") 
    print(f"Employee present part time: {part_time_count} days") 
    print(f"Employee on leave: {leaves_count} days") 
    print(f"Total hours worked: {hours}")
    

if __name__ == "__main__":
    main()