import pandas as pd
from rda import rda_values

data = pd.read_csv("food.csv", index_col=0)


food_intake = {
'spinach' : 100, 
'egg' : 120, 
'rice_basmati' : 300, 
'olive_oil' : 20, 
'carrot' : 100, 
'rapeseed_oil' : 20,
'rice_milk' : 120, 
'rice_cake' : 80, 
'frozen_raspberries' : 65, 
'rice_flour' : 125, 
'chicken' : 320,
'cheddar_cheese' : 50, 
'red_pepper' : 100, 
'salmon' : 140,
'almonds' : 10
}

intake = pd.Series(food_intake)

consumed = data.multiply(intake, axis = "index")

totals = consumed.sum(axis=0).rename("totals")

print(totals.shape)

rda_vals = rda_values()

daily_data = pd.concat([totals, rda_vals], join = "inner", axis = 1)


print(daily_data["totals"]/daily_data["rda"])






