import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud



df=pd.read_csv("netflix_titles.csv")
df.info()
df.isnull().sum()
# fill empty values 
df['director']= df['director'].fillna("Not Disclosed")
df['cast']= df['cast'].fillna("Not Mention")
df['country']= df['country'].fillna("Not Mention")
df['date_added']= df['date_added'].fillna("Not Added")
df['rating']= df['rating'].fillna("Not Added")
df['duration']= df['duration'].fillna("Not Added")
type_count = df['type'].value_counts()
sns.barplot(x=type_count.index,y=type_count.values,color='green')
plt.title("Distribution  of content by type ")
plt.xlabel("Type")
plt.ylabel("count")
plt.show()
rating_count = df['rating'].value_counts()
sns.barplot(x=rating_count.index,y=rating_count.values,color='purple')
plt.title("Content Rating on Netflix  ")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
yearly_counts = df['release_year'] = df['date_added'].dt.year
yearly_counts

yearly_counts = df['release_year'].value_counts().sort_index()
yearly_counts
plt.figure(figsize=(12,6))
sns.lineplot(x=yearly_counts.index,y=yearly_counts,marker='o', c='green',mfc='r')
plt.title("Yearly Trends In content Addition ")
plt.xlabel("Year Added ")
plt.ylabel('Number oF Title')
plt.grid(True)
plt.show()
df['genres'] = df['listed_in'].apply(lambda x:x.split(', '))
genre_count = pd.Series(sum(df['genres'],[])).value_counts().head(10)
genre_count
sns.barplot(x=genre_count.values, y=genre_count.index, hue=genre_count,palette='rainbow')
plt.title("Top 10 Most Common Genres")
plt.xlabel('Number Of Titles ')
plt.ylabel('Genre')
plt.show()
top_countries = df['country'].value_counts().head(10)
top_countries

sns.barplot(x=top_countries.values, y=top_countries.index, hue=genre_count,palette='cool')
plt.title("Top 10 Most Common Genres")
plt.xlabel('Number Of Titles ')
plt.ylabel('Genre')
plt.show()
df["monthly_added"] = df['date_added'].dt.month  # Step 1: extract month (1-12)
monthly_count = df['monthly_added'].value_counts().sort_index()  # Step 2: count & sort
monthly_count

sns.barplot(x=monthly_count.index , y=monthly_count.values,hue=
            monthly_count.index,palette='Blues')
plt.title("Monthly Content Additions")
plt.xlabel("Months")
plt.ylabel("Number Of Titles")
plt.xticks(range(1,13),['jan','feb','mar','apr','mar','jun','jul','aug','sep','oct','nov','dec'])
plt.show
top_director =df['director'].value_counts().head(10)
print(top_director)
sns.barplot(x=top_director.values, y=top_director.index,hue=top_director,palette='deep')
plt.title("Top 10 Most Common Genres",fontsize=16)
plt.xlabel('Number Of Titles ',fontsize=14)
plt.ylabel('Director ',fontsize=14)
plt.tight_layout()
plt.show()

WordCloud= WordCloud(width=800,height=400,background_color='black').generate(''.join(df['title']))
WordCloud
plt.Figure(figsize=(8,6))
plt.imshow(WordCloud,interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud Of Netflix Titles')
plt.show()
Duration = df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(float)
Duration
plt.Figure(figsize=(10,6))
sns.histplot(df[df['type'] == 'Movie']['duration_num'],bins=30,kde=True,color='Blue')
plt.title('Ditribution of Movie Durations')
plt.xlabel('Duration (miutes)')
plt.ylabel('Frequency')
plt.show()
titles_per_year = df.groupby('release_year').size()
titles_per_year

top_10_year = titles_per_year.sort_values(ascending=False).head(10)
top_10_year
plt.Figure(figsize=(10,6))

sns.lineplot(x=top_10_year.index ,y=top_10_year.values,marker='o',c='g',ms=8,mfc='r')
plt.title('Top 10 Year with the most Tiles Released ', fontsize=16)
plt.xlabel('Year',fontsize=14)
plt.ylabel('Number of Titles ',fontsize=14)
plt.grid()
plt.show()