# session-8-assingment-shane-rodricks
# Session 8 Assignment - Advanced Python Decorators
Name: Shane Rodricks
Email: spiderpig27570@gmail.com
Session: 8: Advanced Python Decorators

# Project Description
This project focuses on the application of advanced Python decorators and the generation of synthetic data using the Faker library. The tasks include generating random profiles and calculating statistics using namedtuples and dictionaries, simulating stock market data for 100 companies, and comparing the performance of different data structures. The project is designed to demonstrate both the practical application of decorators and the handling of large datasets in Python.

# Functionality
# 1. Generating Random Profiles Using Namedtuples and Dictionaries
The first part of the project involves generating 10,000 random user profiles using the Faker library. The profiles include information such as blood type, current location, birthdate, and age. These profiles are stored in namedtuples and dictionaries, and the project compares the speed of generating and processing these data structures.

# Functionality:

Namedtuples: Used to create a structured, immutable representation of each profile.
Dictionaries: Provide a flexible, mutable alternative to namedtuples.
Statistics Calculated:
Largest blood type
Mean current location
Oldest person age
Average age
Code Example:

from collections import namedtuple
from faker import Faker
import statistics

# Initialize Faker
fake = Faker()

# Create a namedtuple to store profile data
Profile = namedtuple('Profile', 'blood_type current_location birthdate age')

def generate_profiles(num_profiles):
    profiles = []
    for _ in range(num_profiles):
        profile = fake.profile()
        blood_type = profile['blood_group']
        current_location = profile['current_location']
        birthdate = profile['birthdate']
        age = (fake.date_this_year().year - profile['birthdate'].year)
        profiles.append(Profile(blood_type, current_location, birthdate, age))
    return profiles
# 2. Simulating Stock Market Data for 100 Companies
This section of the project involves simulating stock market data for the top 100 companies using the Faker library. Each company is assigned a random name, stock symbol, opening value, highest value during the day, and closing value. The project calculates the weighted stock market value based on random weights assigned to each company.

# Functionality:

Stock Market Simulation: Generates stock data for 100 companies.
Weighted Stock Market Value Calculation: Based on the formula:
Stock Market Value
=
∑
𝑖
=
1
100
(
close value
𝑖
×
random weight
𝑖
)
∑
𝑖
=
1
100
random weight
𝑖
Stock Market Value= 
∑ 
i=1
100
​
 random weight 
i
​
 
∑ 
i=1
100
​
 (close value 
i
​
 ×random weight 
i
​
 )
​
 
Statistics Calculated:
Market start value
Market highest value
Market end value
Code Example:


from random import uniform
from collections import namedtuple

# Create a namedtuple to store stock data
Stock = namedtuple('Stock', 'name symbol open high close random_weight')

# def generate_stocks(num_stocks):
    stocks = []
    for _ in range(num_stocks):
        name = fake.company()
        symbol = name[:4].upper()  # Simple approach for a stock symbol
        open_value = round(uniform(100, 500), 2)
        high_value = round(open_value * uniform(1.01, 1.2), 2)
        close_value = round(open_value * uniform(0.9, 1.1), 2)
        random_weight = uniform(1, 10)
        stocks.append(Stock(name, symbol, open_value, high_value, close_value, random_weight))
    return stocks

# Calculate Stock Market Value
weighted_sum = sum([s.close * s.random_weight for s in stocks])
total_weight = sum([s.random_weight for s in stocks])
stock_market_value = weighted_sum / total_weight
# 3. Performance Comparison of Namedtuples and Dictionaries
The project includes a comparison of the time taken to generate and process 10,000 profiles using namedtuples versus dictionaries. This comparison highlights the performance differences between these two data structures, particularly in terms of speed and efficiency.

# Functionality:

Time Measurement: Uses the time module to measure the time taken for operations.
Comparison: Outputs the time taken for both namedtuples and dictionaries.
Code Example:



import time

# Timing comparison
start_time_namedtuple = time.time()
profiles_namedtuple = generate_profiles(10000)
end_time_namedtuple = time.time()

start_time_dict = time.time()
profiles_dict = generate_profiles_dict(10000)
end_time_dict = time.time()

print(f"NamedTuple generation took {end_time_namedtuple - start_time_namedtuple} seconds")
print(f"Dictionary generation took {end_time_dict - start_time_dict} seconds")
# 4. README File
The README file is an essential part of the project, providing a comprehensive description of the project, its functionality, and instructions on how to run the code and tests. It includes the following sections:

Project Title: Stock Market Simulation with Faker
Description: Overview of the project, including its goals and functionality.
Setup: Instructions for setting up the environment, including installing necessary libraries.
Usage: Detailed steps on how to run the code and interpret the results.
Tests: Information on the tests included in the project and how to run them using pytest.
# 5. Testing
The project includes comprehensive testing to ensure the functionality works as expected. The tests cover a range of scenarios, including:

Profile Generation: Ensures correct statistics are calculated.
Stock Market Simulation: Validates that the market value calculations are correct.
Performance Testing: Confirms that the timing functions correctly measure the performance of namedtuples and dictionaries.
Example Test Case:


import pytest
from datetime import datetime

def test_odd_it_even():
    from assignment_code import odd_it  # Import the relevant functions

    @odd_it
    def adder(a: int, b: int) -> int:
        return a + b

    if datetime.now().second % 2 != 0:
        assert adder(1, 2) is not None
    else:
        assert adder(1, 2) is None
# 6. GitHub Repository
The project is hosted on a public GitHub repository, which includes the following:

Code: The full Python script implementing the project functionality.
README: A comprehensive README file explaining the project.
Tests: A test_assignment.py file containing all the tests to validate the code.
GitHub Actions: Configured to automatically run the tests on each push, ensuring continuous integration.
Public Link
Once the code is complete and all tests pass, the project is pushed to a public GitHub repository. The public link to the repository is shared to allow others to access the code, notebook, and results.