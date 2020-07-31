{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests_with_caching\
import json\
\
def get_movies_from_tastedive(title):\
    endpoint = 'https://tastedive.com/api/similar'\
    param = \{\}\
    param['q'] = title\
    param['limit'] = 5\
    param['type'] = 'movies'\
    this_page_cache = requests_with_caching.get(endpoint, params=param)\
    return json.loads(this_page_cache.text)\
\
def extract_movie_titles(dic):\
    list = []\
    for i in dic['Similar']['Results']:\
        list.append(i['Name'])\
    return(list)\
\
def get_related_titles(titles_list):\
    list = []\
    for i in titles_list:\
        new_list = extract_movie_titles(get_movies_from_tastedive(i))\
        for i in new_list:\
            if i not in list:\
                list.append(i)\
    print(list)\
    return list\
\
def get_movie_data(title):\
    endpoint = 'http://www.omdbapi.com/'\
    param = \{\}\
    param['t'] = title\
    param['r'] = 'json'\
    this_page_cache = requests_with_caching.get(endpoint, params=param)\
    return json.loads(this_page_cache.text)\
\
def get_movie_rating(data):\
    rating = 0\
    for i in data['Ratings']:\
        if i['Source'] == 'Rotten Tomatoes':\
            rating = int(i['Value'][:-1])\
            #print(rating)\
    return rating \
\
def get_sorted_recommendations(list):\
    new_list = get_related_titles(list)\
    new_dict = \{\}\
    \
    for i in new_list:\
        rating = get_movie_rating(get_movie_data(i))\
        new_dict[i] = rating\
    print(new_dict)\
    \
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]\
    \
    \
    \
    }