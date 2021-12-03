#!/usr/bin/python3
import sys

# Get distance from user
def inputnumber():
    inputted = input("Input a distance in meters: ")
    try:
        dinstance_in_meters = float(inputted)
    except:
        sys.exit(f"'{inputted}' is not a valid number")
    return dinstance_in_meters
    # sys.stderr.write(f"{inputted} is not a valid number"

# convert meters to feet
def meters_to_feet(meters: float):
    return meters * 3.28

# output meters and feet
def output(meters: float, feet: float):
    sys.stdout.write(f"{meters} meters is {feet} feet \n")

inputtedmeters = inputnumber()

convertedfeet = meters_to_feet(inputtedmeters)

output(inputtedmeters, convertedfeet)