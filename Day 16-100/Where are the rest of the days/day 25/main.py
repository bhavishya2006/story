# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#
# print(data)
# import csv
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
#
# print(data["condition"])
# print(data.condition)
#
# print(data[data.day == "Monday"])
# import pandas as pd
# data = pd.read_csv("weather_data.csv")
# max_temp_row = data[data["temp"] == data["temp"].max()]
# print(max_temp_row)
import pandas

# monday = data[data.day == "Monday"]
# monday_temp_c = monday.temp.iloc[0]
# monday_temp_f = monday_temp_c * 9/5 + 32
# print(f"Monday's temperature in Fahrenheit is {monday_temp_f}")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = data[data["Primary Fur Color"] == "Gray"]
print(gray_squirrels_count)




