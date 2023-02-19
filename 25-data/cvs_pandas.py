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
"""
Data types in pandas
Dataframe refers to the whole spreadsheet
series refers to columns
"""
# read cvs file
data = pandas.read_csv("./002 weather-data.csv")

data_dict = data.to_dict()

data_list = data["temp"].to_list()
# print(data_list)

# get average temperature
average = sum(data_list) / len(data_list)
average = data['temp'].mean()


# get max temperature row
maximum_value = data.temp.max()
# print(data[data.temp == maximum_value])

# get temperature for for monday
monday = data[data.day == 'Monday']
monday_temp = int(monday.temp)
monday_temp_F = monday.temp * 9/5 + 32
# print(monday_temp_F)


# create a dataframe from scratch
data_dict = {
    "students": ["Kelvin", "Karen", "Jay"],
    "scores": [90, 34, 23]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
