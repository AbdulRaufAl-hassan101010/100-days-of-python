import pandas

data = pandas.read_csv(
    "./004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# get the number for squirrels with gray, cinnamon and black primary fur color
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# create a new csv  file with fur count data
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrels_count.csv")
print(new_data)
