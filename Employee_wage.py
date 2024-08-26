'''
@Author: Samadhan Thube
@Date: 2024-08-24
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-24
@Title : Employee Wage Computation Problem 
'''

import random

class Employee_Wage:
      
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
    def calculate_wage(cls, wage_per_hour, full_day_hour):
        """
        Description:
            This function calculates the daily wage for both full-day and part-time work.
        
        Parameters:
            wage_per_hour (int): The wage rate per hour.
            full_day_hour (int): The number of hours in a full working day.
        
        Return:
            tuple: The wages for a full day and a part-time day.
        """
        return wage_per_hour * full_day_hour, (wage_per_hour // 2) * full_day_hour
    
    @classmethod
    def wage_for_month(cls, max_working_days, max_working_hours, full_day_hour, wage_per_hour):
        """
        Description:
            This function simulates the employee's attendance and wage computation over a month.
            It tracks the number of full-time days, part-time days, and leave days.
        
        Parameters:
            max_working_days (int): The maximum number of working days in a month.
            max_working_hours (int): The maximum number of working hours in a month.
            full_day_hour (int): The number of hours in a full working day.
            wage_per_hour (int): The wage rate per hour.
        
        Return:
            tuple: A list of daily wages for the period, counts of full-time, part-time, leave days, and total hours worked.
        """
        full_day_wage, part_time_wage = cls.calculate_wage(wage_per_hour, full_day_hour)
        
        daily_wages = []
        total_days = 0
        total_hours = 0
        full_time_count = 0
        part_time_count = 0
        leaves_count = 0
        
        while total_days < max_working_days and total_hours < max_working_hours:
            attendance = cls.check_attendance()
            
            match attendance:
                case 1:
                    daily_wages.append(full_day_wage)
                    full_time_count += 1
                    total_days += 1
                    total_hours += full_day_hour
                
                case 2:
                    daily_wages.append(part_time_wage)
                    part_time_count += 1
                    total_days += 1
                    total_hours += full_day_hour / 2
                
                case 0:
                    daily_wages.append(0)
                    leaves_count += 1
                    
        return daily_wages, full_time_count, part_time_count, leaves_count, total_hours
 
         
def main():
    wage_per_hour = int(input("Enter wage per hour: "))
    full_day_hour = int(input("Enter full day hour: "))
    max_working_days = int(input("Enter total working days of month: "))
    max_working_hours = int(input("Enter total working hours of month: "))
    
    daily_wages, full_time_count, part_time_count, leaves_count, hours = Employee_Wage.wage_for_month(
        max_working_days, max_working_hours, full_day_hour, wage_per_hour
    )
    
    print("-" * 50)
    
    print(f"Per day wages of employee: {daily_wages}")
    print(f"Total Wage of the month: ${sum(daily_wages)}")
    print(f"Employee present full time: {full_time_count} days") 
    print(f"Employee present part time: {part_time_count} days") 
    print(f"Employee on leave: {leaves_count} days") 
    print(f"Total hours worked: {hours}")
    

if __name__ == "__main__":
    main()
