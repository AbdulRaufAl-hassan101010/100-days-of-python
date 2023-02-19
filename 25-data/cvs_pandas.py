# # open file
# with open("./002 weather-data.csv") as weather_file:
#     try:
#         data = weather_file.readlines()
#         print(data)
#     except:
#         pass


# import csv
# with open("./002 weather-data.csv") as weather_file:
#     try:
#         data = csv.reader(weather_file)
#         temperatures = []
#         for row in data:
#             temperature = row[1]
#             if temperature != 'temp':
#                 temperatures.append(temperature)
#         print(temperatures)
#     except:
#         pass


import pandas
# read file
data = pandas.read_csv("./002 weather-data.csv")
print(data["temp"])
