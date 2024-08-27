from collections import namedtuple
from faker import Faker
import statistics
import time
from random import uniform
import numpy as np

# Initialize Faker
fake = Faker()

# Create a namedtuple to store profile data
Profile = namedtuple('Profile', 'blood_type current_location birthdate age')

# Generate profiles using namedtuple
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

# Generate 10,000 profiles
profiles = generate_profiles(10000)

# Calculate the largest blood type, mean current location, oldest person age, and average age
blood_types = [p.blood_type for p in profiles]
largest_blood_type = max(set(blood_types), key=blood_types.count)

mean_location = (
    sum([p.current_location[0] for p in profiles]) / len(profiles),
    sum([p.current_location[1] for p in profiles]) / len(profiles)
)

oldest_person_age = max([p.age for p in profiles])
average_age = statistics.mean([p.age for p in profiles])

print(f"Largest Blood Type: {largest_blood_type}")
print(f"Mean Current Location: {mean_location}")
print(f"Oldest Person Age: {oldest_person_age}")
print(f"Average Age: {average_age}")

# Repeat the Above Using a Dictionary and Compare Speed
def generate_profiles_dict(num_profiles):
    profiles = []
    for _ in range(num_profiles):
        profile = fake.profile()
        blood_type = profile['blood_group']
        current_location = profile['current_location']
        birthdate = profile['birthdate']
        age = (fake.date_this_year().year - profile['birthdate'].year)
        profiles.append({
            'blood_type': blood_type,
            'current_location': current_location,
            'birthdate': birthdate,
            'age': age
        })
    return profiles

# Generate 10,000 profiles using dictionary
start_time_namedtuple = time.time()
profiles_namedtuple = generate_profiles(10000)
end_time_namedtuple = time.time()

start_time_dict = time.time()
profiles_dict = generate_profiles_dict(10000)
end_time_dict = time.time()

# Timing comparison
print(f"NamedTuple generation took {end_time_namedtuple - start_time_namedtuple} seconds")
print(f"Dictionary generation took {end_time_dict - start_time_dict} seconds")

# Create Fake Data for 100 Companies and Simulate Stock Market Value
# Create a namedtuple to store stock data
Stock = namedtuple('Stock', 'name symbol open high close random_weight')

def generate_stocks(num_stocks):
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

# Generate 100 stocks
stocks = generate_stocks(100)

# Calculate Stock Market Value
weighted_sum = sum([s.close * s.random_weight for s in stocks])
total_weight = sum([s.random_weight for s in stocks])
stock_market_value = weighted_sum / total_weight

# Show market start, highest value, and end
market_start = sum([s.open for s in stocks])
market_high = sum([s.high for s in stocks])
market_end = sum([s.close for s in stocks])

print(f"Stock Market Start Value: {market_start}")
print(f"Stock Market Highest Value: {market_high}")
print(f"Stock Market End Value: {market_end}")
