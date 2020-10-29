#!/usr/bin/env python
# coding: utf-8

# # Star Wars Survey
# 
# For this project, I will be cleaning and exploring data from a Star Wars survey conducted by the team at FiveThirtyEight.

# # Read in the Data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")
star_wars.head(5)


# In[2]:


star_wars.columns


# In[3]:


star_wars = star_wars[star_wars['RespondentID'].notnull()]
star_wars.head(15)


# In[4]:


# Convert some columns to Boolean type using map
yes_no = {"Yes": True, "No": False}

star_wars['Have you seen any of the 6 films in the Star Wars franchise?'] = star_wars['Have you seen any of the 6 films in the Star Wars franchise?'].map(yes_no)
star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'] = star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'].map(yes_no)
    
print(star_wars['Have you seen any of the 6 films in the Star Wars franchise?'].head(3))
print(star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?'].head(3))


# In[5]:


# Converting the checkbox columns to Boolean type and renaming column names to be more intuitive
movie_name_map = {
    'Star Wars: Episode I  The Phantom Menace': True,
    'Star Wars: Episode II  Attack of the Clones': True,
    'Star Wars: Episode III  Revenge of the Sith': True,
    'Star Wars: Episode IV  A New Hope': True,
    'Star Wars: Episode V The Empire Strikes Back': True,
    'Star Wars: Episode VI Return of the Jedi': True,
     np.NaN: False}

for c in star_wars.columns[3:9]:
    star_wars[c] = star_wars[c].map(movie_name_map)

star_wars = star_wars.rename(columns={
    "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
    "Unnamed: 4": "seen_2",
    "Unnamed: 5": "seen_3",
    "Unnamed: 6": "seen_4",
    "Unnamed: 7": "seen_5",
    "Unnamed: 8": "seen_6"
})  

star_wars[star_wars.columns[3:9]].head()


# In[6]:


# Cleaning next ranking columns
star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
star_wars = star_wars.rename(columns={
    "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
    "Unnamed: 10": "ranking_2",
    "Unnamed: 11": "ranking_3",
    "Unnamed: 12": "ranking_4",
    "Unnamed: 13": "ranking_5",
    "Unnamed: 14": "ranking_6"
})

star_wars[star_wars.columns[9:15]].head()


# In[7]:


# Mean ranking of movies. A lower rank is better.
mean_rankings = star_wars[star_wars.columns[9:15]].mean()


# In[8]:


plt.bar(range(1, 7, 1), mean_rankings)


# A lower ranking is better. "Star Wars: Episode V The Empire Strikes Back" had the best ranking, whereas "Star Wars: Episode III  Revenge of the Sith" had the worst. Overall the "originals" had the best rankings.

# In[9]:


# How many people saw each film
seen = star_wars[star_wars.columns[3:9]].sum()
seen


# In[10]:


plt.bar(range(1, 7, 1), seen)


# More people saw the original films. This reinforces our findings from the previous chart, that the earlier films were more popular.

# In[11]:


# Split data by gender and plot mean and total views for both.
males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]

plt.bar(range(1, 7, 1), males[males.columns[9:15]].mean())
plt.show()
plt.bar(range(1, 7, 1), females[females.columns[9:15]].mean())
plt.show()


# In[12]:


plt.bar(range(1, 7, 1), males[males.columns[3:9]].sum())
plt.show()
plt.bar(range(1, 7, 1), females[females.columns[3:9]].sum())
plt.show()


# Possible next steps:
# 
# - Segment the data based on columns like Education, Location (Census Region), and Which character shot first?, which aren't binary.
# - Clean up columns 15 to 29, which contain data on the characters respondents view favorably and unfavorably.
#  - Which character do respondents like the most?
#  - Which character do respondents dislike the most?
#  - Which character is the most controversial (split between likes and dislikes)?

# In[ ]:




