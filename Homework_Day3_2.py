#2. Advanced Slicing Techniques
#Objective: The aim of this assignment is to master the art of slicing in Python lists.

#Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

#Task 1: Given the list of temperatures:

temperatures = ['72', '75', '78', '79', '80', '81', '82', '83', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106']

print("Temperature list: '72', '75', '78', '79', '80', '81', '82', '83', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106'")

# Extract the temperatures for the second week (7 days) 

second_week = temperatures[7:14]
print("Second week Temps:", second_week)
# of the month. Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

#Task 2: Extract all the temperatures above 100.

temps_above_100 = temperatures[24:30]
print("Temps above 100", temps_above_100)

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

print("Temperatures sorted in descending order:")
temperatures.sort(reverse=False)
print(temperatures)

day5_to_day10_temps = temperatures[4:10]
print("Temps on 5th day to 10th day:", day5_to_day10_temps)