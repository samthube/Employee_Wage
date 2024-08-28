"""
@Author: Samadhan Thube
@Date: 2024-08-28
@Last Modified by: Samadhan Thube
@Last Modified time: 2024-08-28
@Title : Employee Wage Computation Problem 
"""

import random
from abc import ABC, abstractmethod


class IEmpWageBuilder(ABC):
    @abstractmethod
    def add_company(self, company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours):
        pass

    @abstractmethod
    def add_employee(self, company_name, employee_name):
        pass

    @abstractmethod
    def display_companies(self):
        pass

    @abstractmethod
    def edit_company_details(self, company_name, wage_per_hour=None, full_day_hour=None, max_working_days=None, max_working_hours=None):
        pass


class Company:
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
        self.employees = []

    def add_employee(self, employee_name):
        """
        Description:
            Adds an employee to the company.
        
        Parameters:
            employee_name (str): Name of the employee.
        
        Return:
            None
        """
        employee = {
            "name": employee_name,
            "daily_wages": [],
            "full_time_count": 0,
            "part_time_count": 0,
            "leaves_count": 0,
            "total_hours": 0
        }
        self.employees.append(employee)

    def compute_wages(self):
        """
        Description:
            Computes the wages for all employees in the company.
        
        Parameter:
            None
        
        Return:
            None
        """
        wage_expenses = 0

        for employee in self.employees:
            total_days = 0
            total_hours = 0

            while total_days < self.max_working_days and total_hours < self.max_working_hours:
                attendance = random.randint(0, 2)  

                match attendance:
                    case 1:
                        daily_wage = self.wage_per_hour * self.full_day_hour
                        employee["full_time_count"] += 1
                        total_hours += self.full_day_hour
                    case 2:
                        daily_wage = (self.wage_per_hour // 2) * self.full_day_hour
                        employee["part_time_count"] += 1
                        total_hours += self.full_day_hour / 2
                    case 0:
                        daily_wage = 0
                        employee["leaves_count"] += 1

                employee["daily_wages"].append(daily_wage)
                total_days += 1

            employee["total_hours"] = total_hours
            total_month_wage = sum(employee["daily_wages"])

            print(f"Employee Name: {employee['name']}")
            print(f"Daily Wages: {employee['daily_wages']}")
            print(f"Full-time days: {employee['full_time_count']}")
            print(f"Part-time days: {employee['part_time_count']}")
            print(f"Leaves: {employee['leaves_count']}")
            print(f"Total hours worked: {employee['total_hours']}")
            print(f"Total wage for the month: {total_month_wage}")
            print("-" * 50)

            wage_expenses += total_month_wage

        print(f"Total wage expenses for {self.company_name}: {wage_expenses}")
        print("=" * 50)


class EmpWageBuilder(IEmpWageBuilder):
    def __init__(self):
        """
        Description:
            Initializes the EmpWageBuilder with an empty list of companies.
        
        Parameter:
            None
        """
        self.companies = []  

    def add_company(self, company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours):
        """
        Description:
            Adds a company to the list of companies.
        
        Parameters:
            company_name (str): Name of the company.
            wage_per_hour (int): The wage rate per hour.
            full_day_hour (int): The number of hours in a full working day.
            max_working_days (int): The maximum number of working days in a month.
            max_working_hours (int): The maximum number of working hours in a month.
        
        Return:
            None
        """
        company = Company(company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours)
        self.companies.append(company)
        print(f"Company {company_name} added successfully.")

    def display_companies(self):
        """
        Description:
            Displays the list of companies.
        
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
            print("-" * 50)

    def add_employee(self, company_name, employee_name):
        """
        Description:
            Adds an employee to the specified company.
        
        Parameters:
            company_name (str): Name of the company.
            employee_name (str): Name of the employee.
        
        Return:
            None
        """
        for company in self.companies:
            if company.company_name == company_name:
                company.add_employee(employee_name)
                print(f"Employee {employee_name} added to {company_name}.")
                return
        
        print(f"Company {company_name} not found.")

    def compute_wages_for_company(self, company_name):
        """
        Description:
            Computes wages for all employees in a specific company.
        
        Parameter:
            company_name (str): Name of the company to compute wages for.

        Return:
            None
        """
        for company in self.companies:
            if company.company_name == company_name:
                print(f"Computing wages for {company.company_name}...")
                company.compute_wages()
                return

        print(f"Company {company_name} not found.")

    def edit_company_details(self, company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours):
        """
        Description:
            Edits the details of the specified company.
        
        Parameters:
            company_name (str): Name of the company to be edited.
            wage_per_hour (int, optional): New wage rate per hour.
            full_day_hour (int, optional): New number of hours in a full working day.
            max_working_days (int, optional): New maximum number of working days in a month.
            max_working_hours (int, optional): New maximum number of working hours in a month.
        
        Return:
            None
        """
        for company in self.companies:
            if company.company_name == company_name:
                if wage_per_hour is not None:
                    company.wage_per_hour = wage_per_hour
                if full_day_hour is not None:
                    company.full_day_hour = full_day_hour
                if max_working_days is not None:
                    company.max_working_days = max_working_days
                if max_working_hours is not None:
                    company.max_working_hours = max_working_hours
                
                print(f"Details updated for company: {company_name}.")
                return
        
        print(f"Company {company_name} not found.")


def main():
    
    emp_wage_builder = EmpWageBuilder()

    while True:
        print("\nEmployee Wage Computation System")
        print("1. Add Company")
        print("2. Add Employee")
        print("3. Compute Wages for a Company")
        print("4. Display Companies")
        print("5. Edit Company Details")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            company_name = input("Enter company name: ")
            wage_per_hour = int(input("Enter wage per hour: "))
            full_day_hour = int(input("Enter full day hour: "))
            max_working_days = int(input("Enter total working days of month: "))
            max_working_hours = int(input("Enter total working hours of month: "))
            
            emp_wage_builder.add_company(company_name, wage_per_hour, full_day_hour, max_working_days, max_working_hours)

        elif choice == '2':
            company_name = input("Enter company name: ")
            employee_name = input("Enter employee name: ")
            emp_wage_builder.add_employee(company_name, employee_name)

        elif choice == '3':
            company_name = input("Enter company name to compute wages for: ")
            emp_wage_builder.compute_wages_for_company(company_name)
        
        elif choice == '4':
            emp_wage_builder.display_companies()
        
        elif choice == '5':
            company_name = input("Enter company name to edit: ")
            
            wage_per_hour = input("Enter new wage per hour (or press enter to skip): ")
            if wage_per_hour is not None:
                wage_per_hour = int(wage_per_hour)
            else:
                wage_per_hour = None

            full_day_hour = input("Enter new full day hour (or press enter to skip): ")
            if full_day_hour:
                full_day_hour = int(full_day_hour)
            else:
                full_day_hour = None

            max_working_days = input("Enter new total working days of month (or press enter to skip): ")
            if max_working_days :
                max_working_days = int(max_working_days)
            else:
                max_working_days = None

            max_working_hours = input("Enter new total working hours of month (or press enter to skip): ")
            if max_working_hours:
                max_working_hours = int(max_working_hours)
            else:
                max_working_hours = None

            
            emp_wage_builder.edit_company_details(company_name,wage_per_hour,full_day_hour,max_working_days,max_working_hours)


        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()



