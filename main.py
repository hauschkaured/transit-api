from San_Antonio import *
from Pittsburgh import *

cityList = ["Pittsburgh", "San Antonio"]

print("Welcome to TransitFoamer!")

response = input("Select your city: ")

if response == "Pittsburgh":
    print_running_buses()
