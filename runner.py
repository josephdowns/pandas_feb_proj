import pandas as pd

df = pd.read_csv("Video_games.csv", header=0)

def max_NA_sales(df):
  return df["NA_Sales"].max()

def min_NA_sales(df):
  return df["NA_Sales"].min()

def avg_NA_sales(df):
  return df[["NA_Sales"]].mean()

def max_EU_sales(df):
  return df["EU_sales"].max()

def min_EU_sales(df):
  return df["EU_Sales"].min()

def avg_EU_sales(df):
  return df[["EU_Sales"]].mean()

def max_JP_sales(df):
  return df["JP_sales"].max()

def min_JP_sales(df):
  return df["JP_Sales"].min()

def avg_JP_sales(df):
  return df[["JP_Sales"]].mean()

def count_of_sales_per_platform(df):
  return df[["Platform", "JP_Sales", "NA_Sales", "EU_Sales"]].groupby("Platform").count()

def highest_selling_game_in_given_year(df, year, region):
  df1 = df[['Name', 'Platform', 'Year_of_Release', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales']]
  return df1.query(f'Year_of_Release == {year}').sort_values(f'{region}', ascending=False).head(1)

def top_user_scores_in_given_year(df, year):
  df2 = df[['Name', 'Platform', 'Year_of_Release', 'Publisher', 'User_Score']]
  return df2.query(f'Year_of_Release == {year}').sort_values("User_Score", ascending=False).head()

def top_games_by_platform_in_given_year(df, year, platform):
  df1 = df[['Name', 'Platform', 'Year_of_Release', 'Publisher', 'User_Score']]
  df1.query(f'Year_of_Release == {year} & Platform == "{platform}"').sort_values('User_Score', ascending=False).head()

import pdb; pdb.set_trace()