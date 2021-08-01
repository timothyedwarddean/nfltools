import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import two players URLs.

url = 'https://www.pro-football-reference.com/players/G/GoreFr00.htm'
url_2 = 'https://www.pro-football-reference.com/players/B/BettJe00.htm'

# Use four digit name for differentiating variable.

player_one_name = url[49:53]
player_two_name = url_2[49:53]

# Remove list to drop added years in Football-Reference's player page.

removal = ['Career', '1 yr']

# Get range of 2 through 25 years to append to above removal list.

for x in range(2, 25):
  values = str(x) + " yrs"
  removal.append(values)

# Defining functions to pull certain stats. 
# Reads HTML of player page, pulls stats, then indexes at column of year.
# Drops anything not containing a year as a row (career, etc.).
# Defines label of "Name" which then adds onto each row and returns.

def overview_stats(url):
  df = pd.read_html(url, index_col=0)
  df = df[0]
  df = df.drop(labels=removal, errors='ignore')
  df['Name'] = name
  for index, row in df.iterrows():
    return df

def rushing_stats(url, name):
  df = pd.read_html(url, index_col=0)
  df = df[0]
  df = df['Rushing']
  df = df.drop(labels=removal, errors='ignore')
  df['Name'] = name
  df['Year'] = df.index.astype(str).str[:4]
  for index, row in df.iterrows():
    return df

def receiving_stats(url):
  df = pd.read_html(url, index_col=0)
  df = df[0]
  df = df['Receiving']
  df = df.drop(labels=removal, errors='ignore')
  df['Name'] = name
  for index, row in df.iterrows():
    return df

# Define the two combined players dataset into one, and sort by year.

player_one_rushing_stats = rushing_stats(url, player_one_name)
player_two_rushing_stats = rushing_stats(url_2, player_two_name)

combined_stats = pd.concat([player_one_rushing_stats, player_two_rushing_stats])
combined_stats = combined_stats.sort_values(by = ['Year'], ascending = True)

# Plot how you please!

sns.lineplot(x='Year', y='Yds', data=combined_stats, hue="Name", style="Name")
plt.show()

# One last test again