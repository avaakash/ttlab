weekdays = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
}

day = int(input("Enter day number: "))

try:
    print(weekdays[day])
except KeyError:
    print('Please enter a day between 1-7')