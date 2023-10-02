from jikanpy import Jikan
import pandas as pd
import time

jikan = Jikan()

dicti = {'page' : [],'raw' : []}
i=1
t_start = time.time()
while True:
    try:
        dicti['page'].append(i)
        tvAnime = jikan.search('anime','',page=i,parameters={'type': 'tv'})
        dicti['raw'].append(tvAnime)
        df = pd.DataFrame(dicti)
        df.to_csv('page_raw.csv',index = False)
        i+=1
        time.sleep(2)
        print('page added to the list')
    except:
        print('program ended')
        break
# print(jikan.anime(51179, extension='reviews'))

# print(recommendationDict)