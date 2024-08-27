"""
@Author: Samadhan Thube
@Date: 2024-08-27
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-27
@Title : Employee Wage Computation Problem 
"""
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
        self.daily_wages = []
        self.full_time_count = 0
        self.part_time_count = 0
        self.leaves_count = 0
        self.total_hours = 0
      
    @classmethod   
    def check_attendance(cls):
        """
        Description:
            Generates a random value to determine the attendance of an employee.
            
        Parameter:
            None
        
        Return:
            int: Returns 0 if the employee is absent, 1 if full-time, 2 if part-time.
        """
        return random.randint(0, 2)
    
    def calculate_wage(self):
        """
        Description:
            Calculates the daily wage for both full-day and part-time work.
            
        Parameter:
            None
        
        Return:
            tuple: The wages for a full day and a part-time day.
        """
        return self.wage_per_hour * self.full_day_hour, (self.wage_per_hour // 2) * self.full_day_hour
    
    def wage_for_month(self):
        """
        Description:
            Simulates the employee's attendance and wage computation over a month.
            Tracks the number of full-time days, part-time days, and leave days.
            
        Parameter:
            None
        
        Return:
            tuple: A list of daily wages, counts of full-time, part-time, leave days, and total hours worked.
        """
        full_day_wage, part_time_wage = self.calculate_wage()
        
        total_days = 0
        total_hours = 0
        
        while total_days < self.max_working_days and total_hours < self.max_working_hours:
            attendance = self.check_attendance()
            
            match attendance:
                case 1:
                    self.daily_wages.append(full_day_wage)
                    self.full_time_count += 1
                    total_days += 1
                    total_hours += self.full_day_hour
            
                case 2:
                    self.daily_wages.append(part_time_wage)
                    self.part_time_count += 1
                    total_days += 1
                    total_hours += self.full_day_hour / 2
            
                case 0:
                    self.daily_wages.append(0)
                    self.leaves_count += 1
                        
        self.total_wage = sum(self.daily_wages)
        self.total_hours = total_hours  
        return self.daily_wages, self.full_time_count, self.part_time_count, self.leaves_count, self.total_hours
 
class CompanyEmpWage:
    def __init__(self):
        """
        Description:
            Initializes the CompanyEmpWage with an empty list of companies.
        
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
        company.wage_for_month()

    def display_companies(self):
        """
        Description:
            Displays the list of companies and their total wages.
            
        Parameter:
            None

        Return:
            None
        """
        if not self.companies:
            print("No companies to display.")
            return
        
        for company in self.companies:
            print(f"Company: {company.company_name}")
            print(f"Per day wages of employee: {company.daily_wages}")
            print(f"Total Wage of the month: ${company.total_wage}")
            print(f"Employee present full time: {company.full_time_count} days")
            print(f"Employee present part time: {company.part_time_count} days")
            print(f"Employee on leave: {company.leaves_count} days")
            print(f"Total hours worked: {company.total_hours}")
            print("-" * 50)

def main():

    emp_wage_builder = CompanyEmpWage()
    
    while True:
        print("Menu:")
        print("1. Add and Compute Wage for Company")
        print("2. Display All Companies")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            company_name = input("Enter company name: ")
            wage_per_hour = int(input("Enter wage per hour: "))
            full_day_hour = int(input("Enter full day hour: "))
            max_working_days = int(input("Enter total working days of month: "))
            max_working_hours = int(input("Enter total working hours of month: "))

            emp_wage_builder.add_and_compute_wage(company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours)
        
        elif choice == '2':
            emp_wage_builder.display_companies()
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
