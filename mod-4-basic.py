'''Module 2: Individual Programming Assignment 1
Useful Business Calculations
This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.
    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee
    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos
    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def savings(gross_pay, tax_rate, expenses):
    savings = ((gross_pay - (gross_pay * tax_rate)) - expenses)
    return savings
    
# ask employee for hourly rate
hourlyrate = float(input("What was your hourly rate? "))

# ask employee how many hours worked for the month
hoursworked = float(input("How many hours did you work for this month? "))

# compute for employee gross pay
gross_pay = hourlyrate * hoursworked
print(gross_pay)

tax_rate = 0.22

# ask for expenses
expenses = float(input("How much was your expenses for this month? "))

# display the savings
print("Total amount of savings is", savings(gross_pay, tax_rate, expenses), 'Centavos')


def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.
    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.
    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.
    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.
    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job
    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    material_waste = (str(int(total_material - total_consumed)) + material_units)
    return material_waste

def compute_total_consumed(num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    return total_consumed

# enter unit of material
material_units = str(input("Enter unit of material: "))

# enter total number of material available
total_material = float(input("Enter total number of material available: "))

# enter number of jobs to run
num_jobs = float(input("Enter the number of jobs: ")) 

# enter the amount of material consumed per job
job_consumption = float(input("Enter amount of material consumed per job: "))

# compute for the total material consumed
total_consumed = compute_total_consumed(num_jobs, job_consumption)

# compute for remaining material
print("The amount of remaining material is", material_waste(total_material, material_units, num_jobs, job_consumption,))

def interest(principal, rate, periods):
    '''Interest.
    3 points.
    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.
    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.
    Round down the final amount.
    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested
    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def interest(principal, rate, periods):
  x = principal * rate
  y = x * periods
  final = principal + y
  return final

principal = int(input('Enter principal value (in pesos):'))
print('₱', principal)

rate = float(input('Enter interest rate in decimal: '))

periods = int(input('Enter number of periods invested (in months): '))

final = interest(principal, rate, periods)

print('The final value of your investment is ₱', round(final, 2), sep='')

def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.
    This function calculates the body mass index (BMI) of a person
        given their weight and height.
    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)
    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].
    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def body_mass_index(weight, feet, inches):
    kg = weight / 2.2
    x = feet * .3048
    y = inches * 0.0254
    height = x + y
    BMI = kg / (height ** 2)
    return BMI

weight = float(input('Enter weight in lbs: '))
feet = int(input('Enter foot component of height: '))
inches = int(input('Enter inches component of height: '))
BMI = body_mass_index(weight, feet, inches)
print('Your body mass index is',round(BMI,4))
