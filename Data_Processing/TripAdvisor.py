import glob
import pandas as pd

# dataframes cleaning
df1 = pd.read_csv('insert csv file path')
df1 = df1.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])

df2 = pd.read_csv('insert csv file path')
df2 = df2.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df3 = pd.read_csv('insert csv file path')
df3 = df3.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df4 = pd.read_csv('insert csv file path')
df4 = df4.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df5 = pd.read_csv('insert csv file path')
df5 = df5.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df6 = pd.read_csv('insert csv file path')
df6 = df6.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df7 = pd.read_csv('insert csv file path')
df7 = df7.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df8 = pd.read_csv('insert csv file path')
df8 = df8.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df9 = pd.read_csv('insert csv file path')
df9 = df9.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df10 = pd.read_csv('insert csv file path')
df10 = df10.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

df11 = pd.read_csv('insert csv file path')
df11 = df11.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'index'])

# concatenate all dataframes together (from df1 to df11)
final_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], ignore_index=True, sort=False)

# drop rows with same coordinates
final_df_2 = final_df.drop_duplicates(subset=['Latitude', 'Longitude'], keep='last')

# reset index
final_df_2.reset_index(drop=True, inplace=True)

# drop rows with specific values (none and service time out)
final_df_3 = final_df_2[final_df_2.Latitude != 'none']
dataframe_final_tripadvisor = final_df_3[final_df_3.Latitude != 'service_time_out']

# export dataframe dataframe_cleaned_final in csv
dataframe_final_tripadvisor.to_csv('insert csv file path')
