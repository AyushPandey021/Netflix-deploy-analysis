import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ================== Load Dataset ==================
df = pd.read_csv("netflix_titles.csv")

# ✅ Convert date_added to datetime for correct `.dt` operations
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# ================== Handle Missing Values ==================
df['director'] = df['director'].fillna("Not Disclosed")
df['cast'] = df['cast'].fillna("Not Mention")
df['country'] = df['country'].fillna("Not Mention")
df['date_added'] = df['date_added'].fillna(pd.Timestamp("2000-01-01"))
df['rating'] = df['rating'].fillna("Not Added")
df['duration'] = df['duration'].fillna("Not Added")

# ================== Plot 1: Distribution by Type ==================
type_count = df['type'].value_counts()
sns.barplot(x=type_count.index, y=type_count.values, color='green')
plt.title("Distribution of Content by Type")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# ================== Plot 2: Content Ratings ==================
rating_count = df['rating'].value_counts()
sns.barplot(x=rating_count.index, y=rating_count.values, color='purple')
plt.title("Content Rating on Netflix")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()

# ================== Plot 3: Yearly Trends ==================
df['release_year'] = df['date_added'].dt.year
yearly_counts = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o', color='green', markerfacecolor='red')
plt.title("Yearly Trends in Content Addition")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()

# ================== Plot 4: Top 10 Genres ==================
df['genres'] = df['listed_in'].apply(lambda x: x.split(', '))
genre_count = pd.Series(sum(df['genres'], [])).value_counts().head(10)

sns.barplot(x=genre_count.values, y=genre_count.index, palette='rainbow')
plt.title("Top 10 Most Common Genres")
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()

# ================== Plot 5: Top Countries ==================
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='cool')
plt.title("Top 10 Countries with Most Titles")
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()

# ================== Plot 6: Monthly Content Additions ==================
df["monthly_added"] = df['date_added'].dt.month
monthly_count = df['monthly_added'].value_counts().sort_index()

sns.barplot(x=monthly_count.index, y=monthly_count.values, palette='Blues')
plt.title("Monthly Content Additions")
plt.xlabel("Months")
plt.ylabel("Number of Titles")
plt.xticks(range(1, 13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.show()

# ================== Plot 7: Top Directors ==================
top_director = df['director'].value_counts().head(10)
sns.barplot(x=top_director.values, y=top_director.index, palette='deep')
plt.title("Top 10 Directors with Most Titles", fontsize=16)
plt.xlabel('Number of Titles', fontsize=14)
plt.ylabel('Director', fontsize=14)
plt.tight_layout()
plt.show()

# ================== WordCloud of Titles ==================
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(' '.join(df['title']))
plt.figure(figsize=(8, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Netflix Titles')
plt.show()

# ================== Plot 8: Movie Duration Distribution ==================
df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(float)
plt.figure(figsize=(10, 6))
sns.histplot(df[df['type'] == 'Movie']['duration_num'], bins=30, kde=True, color='blue')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

# ================== Plot 9: Top 10 Years with Most Titles ==================
titles_per_year = df.groupby('release_year').size()
top_10_year = titles_per_year.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.lineplot(x=top_10_year.index, y=top_10_year.values, marker='o', color='green', markersize=8, markerfacecolor='red')
plt.title('Top 10 Years with Most Titles Released', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Titles', fontsize=14)
plt.grid()
plt.show()

