# Employee Management System - OOP Case Study

## **Overview**
A **large IT company** wants to build an **Employee Management System** to keep track of different types of employees, such as **Permanent Employees**, **Contract Employees**, and **Interns**. 
Each employee has a **salary structure**, but the method to **calculate salary** is different for each type.

## **Key Features**
1. **Base Class (`Employee`)**:  
   - Stores common attributes like `name`, `employee_id`, and `department`.
   - A method `calculate_salary()` that will be overridden by child classes.
   - A method `display_details()` to print employee details.

2. **Derived Classes**:
   - `PermanentEmployee`: Fixed salary with **bonus**.
   - `ContractEmployee`: Paid **per hour**.
   - `Intern`: Receives a **stipend**.

3. **OOP Concepts Applied:**
   - **Inheritance**: All employee types inherit from `Employee`.
   - **Encapsulation**: Private attributes with controlled access.
   - **Method Overriding**: `calculate_salary()` is overridden in each subclass.
   - **Polymorphism**: Single function handling different employee types.
   - **Abstract Class (`ABC`)**: Ensures `calculate_salary()` must be implemented.


---

## **Sample Output**
```
__init__ of Employee
__init__ of PermanentEmployee
__init__ of Employee
__init__ of ContractEmployee
__init__ of Employee
__init__ of Intern

--- Employee Details ---
Employee ID: P123
Name: Alice Johnson
Department: IT
Basic Salary: $60000.00
Bonus: $5000.00
Total Salary: $65000.00

--- Employee Details ---
Employee ID: C456
Name: Bob Smith
Department: HR
Hourly Rate: $50.00
Hours Worked: 160
Total Salary: $8000.00

--- Employee Details ---
Employee ID: I789
Name: Charlie Brown
Department: Finance
Stipend: $1500.00
Total Salary: $1500.00
```

---

## **Summary**
| Class | Attributes | `calculate_salary()` Logic |
|--------|-------------|---------------------------|
| **Employee** | `employee_id`, `name`, `department` | --- |
| **PermanentEmployee** | `basic_salary`, `bonus` | `basic_salary + bonus` |
| **ContractEmployee** | `hourly_rate`, `hours_worked` | `hourly_rate * hours_worked` |
| **Intern** | `stipend` | Fixed `stipend` |


