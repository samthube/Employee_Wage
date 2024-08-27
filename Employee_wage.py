'''
@Author: Samadhan Thube
@Date: 2024-08-24
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-24
@Title : Employee Wage Computation Problem 
'''

import random

class Employee_Wage:
    
    def __init__(self, company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours):
        """
        Description:
            Constructor to initialize the instance variables for the company.
        
        Parameters:
            company_name (str): Name of the company.
            wage_per_hour (int): The wage rate per hour.
            full_day_hour (int): The number of hours in a full working day.
            max_working_days (int): The maximum number of working days in a month.
            max_working_hours (int): The maximum number of working hours in a month.
        """
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.full_day_hour = full_day_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.total_wage = 0
      
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
        
        Return:
            tuple: The wages for a full day and a part-time day.
        """
        return self.wage_per_hour * self.full_day_hour, (self.wage_per_hour // 2) * self.full_day_hour
    
    
    def wage_for_month(self):
        """
        Description:
            This function simulates the employee's attendance and wage computation over a month.
            It tracks the number of full-time days, part-time days, and leave days.
        
        Return:
            tuple: A list of daily wages for the period, counts of full-time, part-time, leave days, and total hours worked.
        """
        full_day_wage, part_time_wage = self.calculate_wage()
        
        daily_wages = []
        total_days = 0
        total_hours = 0
        full_time_count = 0
        part_time_count = 0
        leaves_count = 0
        
        while total_days < self.max_working_days and total_hours < self.max_working_hours:
            attendance = self.check_attendance()
            
            match attendance:
                case 1:
                    daily_wages.append(full_day_wage)
                    full_time_count += 1
                    total_days += 1
                    total_hours += self.full_day_hour
            
                case 2:
                    daily_wages.append(part_time_wage)
                    part_time_count += 1
                    total_days += 1
                    total_hours += self.full_day_hour / 2
            
                case 0:
                    daily_wages.append(0)
                    leaves_count += 1
                        
        return daily_wages, full_time_count, part_time_count, leaves_count, total_hours
 
         
class CompanyEmpWage:
    def __init__(self):
        """
        Description:
            Constructor to initialize the CompanyEmpWage with an empty list of companies.
        
        Parameter:
            None
        """
        self.companies = []

    def add_and_compute_wage(self, company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours):
        """
        Description:
            Adds a company and computes the wages by creating an instance of Employee_Wage and storing it.
        
        Parameters:
            company_name (str): Name of the company.
            wage_per_hour (int): The wage rate per hour.
            full_day_hour (int): The number of hours in a full working day.
            max_working_days (int): The maximum number of working days in a month.
            max_working_hours (int): The maximum number of working hours in a month.
        
        Return:
            None
        """
        company = Employee_Wage(company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours)
        self.companies.append(company)

        
        daily_wages, full_time_count, part_time_count, leaves_count, total_hours = company.wage_for_month()
        company.total_wage = sum(daily_wages)

        print(f"Company: {company.company_name}")
        print(f"Per day wages of employee: {daily_wages}")
        print(f"Total Wage of the month: ${company.total_wage}")
        print(f"Employee present full time: {full_time_count} days")
        print(f"Employee present part time: {part_time_count} days")
        print(f"Employee on leave: {leaves_count} days")
        print(f"Total hours worked: {total_hours}")
        print("-" * 50)


def main():
    emp_wage_builder = CompanyEmpWage()
    number_of_companies = int(input("Enter no of companies: "))

    for _ in range(number_of_companies):
        company_name = input("Enter company name: ")
        wage_per_hour = int(input("Enter wage per hour: "))
        full_day_hour = int(input("Enter full day hour: "))
        max_working_days = int(input("Enter total working days of month: "))
        max_working_hours = int(input("Enter total working hours of month: "))

        emp_wage_builder.add_and_compute_wage(company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours)


if __name__ == "__main__":
    main()


