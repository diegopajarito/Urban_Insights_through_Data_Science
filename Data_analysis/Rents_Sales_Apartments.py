from matplotlib import pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import read_excel
import seaborn as sns

# read file rents Rome
# read excel sheet
my_sheet = 'insert name of sheet'
file_name = 'insert name excel file'
df_rents = read_excel(file_name, sheet_name = my_sheet)
print(df_rents.head())

# drop line 4 of the dataset beacuse it is a NAN value
df_rents = df_rents.drop(df_rents.index[[4]])

# remove characters '€' and '/m²' in 'vendita' and 'affitto' columns
df_rents['vendita'] = df_rents['vendita'].map(lambda x: x.lstrip('€').rstrip('/m²'))
df_rents['affitto'] = df_rents['affitto'].map(lambda x: x.lstrip('€').rstrip('/m²/mese'))

# replace characters '.' and ',' in 'vendita' and 'affitto' columns
df_rents['vendita'] = [x.strip().replace('.', '') for x in df_rents['vendita']]
df_rents['affitto'] = [x.strip().replace(',', '.') for x in df_rents['affitto']]

# rename all columns 
df_rents.columns = ['Typology', 'Sale_€/m²', 'Rent_€/m²']

# how to convert dataframe columns from object to numeric
df_rents['Sale_€/m²']= df_rents['Sale_€/m²'].astype(int)
df_rents['Typology']= df_rents['Typology'].astype(str)
df_rents['Rent_€/m²']= df_rents['Rent_€/m²'].astype(float)

# sort the dataframe according to the sale price column
df_rents_sorted_1 = df_rents.sort_values(by="Sale_€/m²", ascending=False)

# sort the dataframe according to the rent price column
df_rents_sorted_2 = df_rents.sort_values(by="Rent_€/m²", ascending=False)

# make horizontal bar plot to show the most expensive typologies for sale 
sns.set(style="whitegrid")

# make the matplotlib bar chart 
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("pastel")
sns.barplot(x="Sale_€/m²", y="Typology", data=df_rents_sorted_1, label="Sale_€/m²", color="b")
plt.title('Rome properties sale prize by typologies ')
plt.show()

# make horizontal bar plot to show the most expensive typologies for rent
sns.set(style="whitegrid")

# make the matplotlib bar chart
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("pastel")
sns.barplot(x="Rent_€/m²", y="Typology", data=df_rents_sorted_2, label="Rent_€/m²", color="r")
plt.title('Rome properties rent prize by typologies ')
plt.show()

# read file rents Rome
# read excel sheet
my_sheet = 'SalePrice_byZone'
file_name = '../data_rome/housing/Sale_rent_apartments_rome.xlsx'
df_sale = read_excel(file_name, sheet_name = my_sheet)
print(df_rents.head())

# remove characters '€' and '/m²' in 'sale price' column
df_sale['sale price €/m²'] = df_sale['sale price €/m²'].map(lambda x: x.lstrip('€').rstrip('/m²'))

# replace character '.' in 'sale price €/m²' column
df_sale['sale price €/m²'] = [x.strip().replace('.', '') for x in df_sale['sale price €/m²']]

# how to convert dataframe columns from object to numeric
df_sale['sale price €/m²']= df_sale['sale price €/m²'].astype(int)
df_sale['zone']= df_sale['zone'].astype(str)

# make horizontal bar plot to show the most expensive sale price by typologies
sns.set(style="whitegrid")

# sort the dataframe accordin to the sale price column
df_sale_sorted = df_sale.sort_values(by="sale price €/m²", ascending=False)

# make the matplotlib bar chart
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("pastel")
sns.barplot(x="sale price €/m²", y="zone", data=df_sale_sorted, label="sale price €/m²", color="g")
plt.yticks(fontsize=4)
df_sale_sorted = df_sale.sort_values("sale price €/m²")
plt.title('Rome properties prizes by zones ')
plt.show()

# read rents Rome excel file
# read excel sheet
my_sheet = 'RentSaleprice_studioFlat_byZone'
file_name = '../data_rome/housing/Sale_rent_apartments_rome.xlsx'
df_sale_rent_studioflat = read_excel(file_name, sheet_name = my_sheet)
print(df_rents.head())

# remove characters '€' and '/m²' in 'sale price' column
df_sale_rent_studioflat['sale_price'] = df_sale_rent_studioflat['sale_price'].map(lambda x: x.lstrip('€').rstrip('/m²'))
df_sale_rent_studioflat['rent_price'] = df_sale_rent_studioflat['rent_price'].map(lambda x: x.lstrip('€').rstrip('/m²/mese'))
df_sale_rent_studioflat['ads_number'] = df_sale_rent_studioflat['ads_number'].map(lambda x: x.lstrip('~').rstrip('+'))

# replace character '.' in 'sale price €/m²' column
df_sale_rent_studioflat['sale_price'] = [x.strip().replace('.', '') for x in df_sale_rent_studioflat['sale_price']]
df_sale_rent_studioflat['rent_price'] = [x.strip().replace(',', '.') for x in df_sale_rent_studioflat['rent_price']]

# drop NAN values
df_cleaned = df_sale_rent_studioflat[~df_sale_rent_studioflat.rent_price.str.contains("-")]

# how to convert dataframe columns from object to numeric
df = df_cleaned.copy()
df['sale_price']= df['sale_price'].astype(int)
df['rent_price']= df['rent_price'].astype(float)
df['ads_number']= df['ads_number'].astype(int)

df_sorted_1 = df.sort_values(by='sale_price', ascending=False)
df_sorted_2 = df.sort_values(by='rent_price', ascending=False)
df_sorted_3 = df.sort_values(by='ads_number', ascending=False)

# make horizontal bar plot to show the most expensive typologies for rent
sns.set(style="whitegrid")

# make the matplotlib bar chart
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("pastel")
sns.barplot(x="sale_price", y="zone", data=df_sorted_1, label="sale_price", color="b")
plt.yticks(fontsize=4)
plt.title('Rome sale prize studio flats')
plt.show()

# make the matplotlib bar chart
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("pastel")
sns.barplot(x="rent_price", y="zone", data=df_sorted_2, label="sale_price", color="b")
plt.yticks(fontsize=4)
plt.title('Rome rent prize studio flats')
plt.show()

# make the matplotlib bar chart
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("pastel")
sns.barplot(x="ads_number", y="zone", data=df_sorted_3, label="sale_price", color="b")
plt.yticks(fontsize=4)
plt.title('Rome ads number studio flats')
plt.show()
