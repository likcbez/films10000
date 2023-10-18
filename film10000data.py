import pandas as pd
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

file_path=("C:/temp/data.csv")
df = pd.read_csv(file_path)
        
#Проверка на различные ошибки
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')
df = df.drop_duplicates()
missing_values = df.isnull().sum()
negative_gross = df[df['Gross'] < 0]



df['Year of Release'] = pd.to_numeric(df['Year of Release'], errors='coerce')
df['Run Time in minutes'] = pd.to_numeric(df['Run Time in minutes'], errors='coerce')
average_duration_by_year = df.groupby('Year of Release')['Run Time in minutes'].mean()
average_duration_by_year.plot(kind='line', title='Средняя длительность фильмов по годам')
plt.xlabel('Год выпуска')
plt.ylabel('Средняя длительность (минуты)')
plt.show()


director_counts = df['Director'].value_counts()
most_prolific_director = director_counts.idxmax()
number_of_films = director_counts.max()
print(f"Режиссер {most_prolific_director} снял наибольшее количество фильмов: {number_of_films} фильмов.")


df['Year of Release'] = pd.to_numeric(df['Year of Release'], errors='coerce')
last_decade_start = 2010
last_decade_end = 2019
last_decade_movies = df[(df['Year of Release'] >= last_decade_start) & (df['Year of Release'] <= last_decade_end)]
last_decade_movies['Genre'] = last_decade_movies['Genre'].str.split(',')
all_genres = [genre for genres_list in last_decade_movies['Genre'] for genre in genres_list]


genre_counts = pd.Series(all_genres).value_counts()
print("Наиболее популярные жанры в последние десятилетия:")
print(genre_counts.head(10))    
print(df)


df['Stars'] = df['Stars'].str.split(',')
actor_combinations = [combo for stars in df['Stars'] for combo in combinations(stars, 2)]
most_common_combinations = Counter(actor_combinations).most_common(10)
print("Наиболее часто снимающиеся вместе актеры:")
for combination, count in most_common_combinations:
    print(f"{', '.join(combination)}: {count} раз")