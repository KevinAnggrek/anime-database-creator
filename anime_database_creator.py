import pandas as pd
import json
import ast

df = pd.read_csv('tv_animes.csv')

dicti = {'mal_id' : [],
         'title_english' : [], 
         'genres': [],
         'studios': [], 
         'source': [], 
         'themes':[], 
         'demographics':[], 
         'rank':[], 
         'popularity':[]}

for raw in df['raw']:
    # raw = f"\"{raw}\""
    res = ast.literal_eval(raw)
    for data in res['data']:
        dicti['mal_id'].append(data['mal_id'])
        dicti['title_english'].append(data['title_english'])
        dicti['source'].append(data['source'])
        dicti['popularity'].append(data['popularity'])
        dicti['rank'].append(data['rank'])

        if data['demographics']:
            dicti['demographics'].append(data['demographics'])
        else:
            dicti['demographics'].append('')

        studioList = []
        genreList = []
        themeList = []
        for studio in data['studios']:
            studioList.append(studio['name'])
        dicti['studios'].append(studioList)
        for genre in data['genres']:
            genreList.append(studio['genre'])
        dicti['genres'].append(genreList)
        for theme in data['themes']:
            themeList.append(studio['theme'])
        dicti['themes'].append(themeList)
print(dicti)


