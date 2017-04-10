import pandas as pd

rda_2000 = {
"Total lipid (fat)_g" : 65,
"Fatty acids, total saturated_g" : 20,
"Cholesterol_mg" :300,
"Sodium, Na_mg" : 2400,
"Potassium, K_mg" : 3500,
"Carbohydrate, by difference_g" : 300,
"Fiber, total dietary_g" : 25,
"Protein_g" : 50,
"Vitamin A, IU_IU" : 5000,
"Vitamin C, total ascorbic acid_mg" : 60, 
"Calcium, Ca_mg" : 1000,
"Iron, Fe_mg" : 18,
"Vitamin D_IU" : 400,
"Vitamin E (alpha-tocopherol)_mg" : 30,
"Vitamin K (phylloquinone)_µg" : 80,
"Thiamin_mg" : 1.5,
"Riboflavin_mg" : 1.7,
"Niacin_mg" : 20,
"Vitamin B-6_mg" : 2,
"Folate, total_µg" : 400,
"Vitamin B-12_µg" : 6,
"Biotin_µg" : 300,
"Pantothenic acid_mg" : 10,
"Phosphorus, P_mg" : 1000,
"Iodine__µg" : 150,
"Magnesium, Mg_mg" : 400,
"Zinc, Zn_mg" : 15,
"Selenium, Se_µg" : 70,
"Copper, Cu_mg" : 2,
"Manganese, Mn_mg" : 2,
"Chromium_µg" : 120,
"Molybdenum_µg" : 75,
"Chloride_mg" : 3400
}


def rda_values():
	return (pd.Series(rda_2000, name = "rda"))




