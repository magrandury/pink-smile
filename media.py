from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get the movies
title1 = ia.get_movie('2245003')
title2 = ia.get_movie('2083264')
title3 = ia.get_movie('2245003')
title4 = ia.get_movie('2245003')
title5 = ia.get_movie('2083264')


movie1 = {
    'title': title1,
    'director': title1['director'][0],
    'cast1': title1['cast'][0],
    'cast2': title1['cast'][1],
    'genres': title1['genres'],
    'plot': title1['plot'][0],
    'cover': title1['full-size cover url']
}

movie2 = {
    'title': title2,
    'director': title2['director'][0],
    'cast1': title2['cast'][0],
    'cast2': title2['cast'][1],
    'genres': title2['genres'],
    'plot': title2['plot'][0],
    'cover': title2['full-size cover url']
}

movie3 = {
    'title': title3,
    'director': title3['director'][0],
    'cast1': title3['cast'][0],
    'cast2': title3['cast'][1],
    'genres': title3['genres'],
    'plot': title3['plot'][0],
    'cover': title3['full-size cover url']
}

movie4 = {
    'title': title4,
    'director': title4['director'][0],
    'cast1': title4['cast'][0],
    'cast2': title4['cast'][1],
    'genres': title4['genres'],
    'plot': title4['plot'][0],
    'cover': title4['full-size cover url']
}

movie5 = {
    'title': title5,
    'director': title5['director'][0],
    'cast1': title5['cast'][0],
    'cast2': title5['cast'][1],
    'genres': title5['genres'],
    'plot': title5['plot'][0],
    'cover': title5['full-size cover url']
}


print(title5['cast'][0])
