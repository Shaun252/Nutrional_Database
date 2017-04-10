import requests
import pandas as pd

food_dict_ndb = {"egg" : "01123", "rice_flour" : "20090", "rice_milk" : "14639", "frozen_raspberries" : "09306", "rice_basmati" : "20044", "chicken" : "05062", "olive_oil" : "04053", "rapeseed_oil" : "04582", "red_pepper" : "11821", "carrot" : "11124", "spinach" : "11457", "cheddar_cheese" : "01009", "rice_cake" : "19053", "coconut_oil" : "04047", "balsamic_vinegar" : "02069", "almonds" : "12061", "salmon" : "15078", "pumpkin_seeds" : "12163"}

headers = {'Content-Type': 'application/json'}
df = pd.DataFrame()

for key, val in food_dict_ndb.items():
	params = {"api_key":"o9Ra8M2RDQKU3XMI4d3XiUzzD8FtwTXeOiH0F2vV", "ndbno":val, "type":"f", "format":"JSON"}
	response = requests.get('https://api.nal.usda.gov/ndb/reports', headers=headers, params = params)

	data = response.json()

	for j in data["report"]["food"]["nutrients"]:
		df.loc[key, j["name"] + "_" + j["unit"]] = float(j["value"]) / 100

df = df.fillna(0)


df.to_csv('food.csv', encoding='utf-8')




	


