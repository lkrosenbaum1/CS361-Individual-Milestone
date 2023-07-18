import requests
import json

# response retrieves theme park json file and data stores the information
theme_url = "https://queue-times.com/en-US/parks.json"
response = requests.get(theme_url)
data = json.loads(response.text)

# sets up command line interface for user
introduction = "Choose one of the options below: \n 1. Find popular Amusement Parks in a country \n 2. Find Amusement" \
               " Park Location \n 3. Find out regional time zone for an Amusement Park \n 4. Exit"
instructions = "\nBelow you will find several options to help plan your next trip to an Amusement Park! \n\nOption 1 will " \
               "show you all the Amusement Parks you can find in a particular country. Option 2 will show you where " \
               "you will travel to visit your desired Amusement Park. Option 3 will inform you of the timezone of the" \
               " park so you can call and make reservations ahead of time."
useful = True

# opens json file
with open('parks.json') as park_file:
    information = json.load(park_file)

def info_finder(entry, check, result):
    """searches the json file to match entries with entered parameter
    and return requested information"""
    for item in information:
    # prints corresponding information
        if item[check] == entry:
            print(item[result])
    # informs when no information is found based on their parameters
        else:
            found = False
    print(f"For more information go to https://{entry}. ***If you choose to follow the link it will take you "
          f"away from the program and take up more of your time.***\n\n")


# informs user on how to use program once at the beginning
print(instructions)

# as long as the user wants to utilize the program it will run
while useful is True:
    print(introduction)
    user = input("Enter the number of the option you would like to choose: ")
    if user == '1':
        location = input("Enter a country: ")
        info_finder(location, 'country', 'name')
    elif user == '2':
        park_locator = input("Enter the name of a Theme Park: ")
        info_finder(park_locator, 'name', 'country')
    elif user == '3':
        park_timezone = input("Enter the name of a Theme Park: ")
        info_finder(park_timezone, 'name', 'timezone')
    elif user == '4':
        useful = False
    else:
        print("Please choose a valid option")

