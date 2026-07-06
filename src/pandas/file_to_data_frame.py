import pandas

df = pandas.read_csv("../data/Order.csv")
print(df.to_string())

print(pandas.read_json("../data/anscombe.json"))
print(pandas.read_excel())
