import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squrriels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squrriels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squrriels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squrriels_count)
print(red_squrriels_count)
print(black_squrriels_count)

data_dic = {
    "Fur color":["Gray","Cinnamon","Black"],
    "Count":[grey_squrriels_count,red_squrriels_count,black_squrriels_count]
}
df = pandas.DataFrame(data_dic)
df.to_csv("squrriels_count.csv")

