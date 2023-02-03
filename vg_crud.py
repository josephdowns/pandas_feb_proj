import pandas as pd

df = pd.read_csv("Video_Games.csv", header = 0)

game_df = pd.Series({
  "Name": "Breath of the Wild",
  "Platform": "Switch",
  "Year_of_Release": 2016,
  "Genre": "Adventure",
  "Publisher": "Nintendo",
  "NA_Sales": "2.01",
  "JP_Sales": "3.01",
  "EU_Sales": "4.88",
  "Other_Sales": "",
  "Global_Sales": "",
  "Critic_Score": 10,
  "Critic_Count": 10,
  "User_Score": 10,
  "User_Count": 10,
  "Developer": "Nintendo",
  "Rating": "T",
})

def create_game(df, game): 
  return pd.concat([df, pd.DataFrame(game).transpose()])

def read_games(df):
  return df

def get_games_by_name(df, name):
  return df.query(f'Name == "{name}"')

def update_game_column(df, index, column, new_value):
  df.loc[index, [f'{column}']] = [f'{new_value}']

def delete_game(df, index):
  df.drop(index) 
