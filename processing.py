import os
import glob
import pandas

data = pandas.concat(map(pandas.read_csv, glob.glob(os.path.join("data", "*.csv"))))
pink_morsel = data[data["product"] == "pink morsel"].copy()
pink_morsel["price"] = pandas.to_numeric(pink_morsel["price"].replace({"\$": ""}, regex=True))
pink_morsel["sales"] = pink_morsel["price"] * pink_morsel["quantity"]
pink_morsel.to_csv("pink_morsel_data.csv", columns=["sales", "date", "region"], header=["Sales", "Date", "Region"], index=False)