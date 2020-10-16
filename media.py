from imdb import IMDb


# Create an instance of the IMDb class
ia = IMDb()


# Get the movies
title1 = ia.get_movie('2245003')  # Miss you already
title2 = ia.get_movie('2083264')  # Mondays at Racine
title3 = ia.get_movie('1877740')  # Five
title4 = ia.get_movie('0356680')  # The family Stone
title5 = ia.get_movie('1464191')  # Decoding Annie Parker

print(title1['cast'])
# Write my summaries
myplot1 = 'This movie follows the story of two best friends, Jess and Milly, as one of them starts a family while the ' \
          'other is diagnosed with an aggressive form of breast cancer. Their friendship carries Milly through to the' \
          ' end. '
myplot2 = 'In this beautiful, heartfelt documentary, we watch sisters Rachel and Cynthia, owners Racine Salon and ' \
          'Spa, open their doors to women fighting breast cancer every third Monday of the month. The sisters give ' \
          'women a connection and the idea that the women don\'t need to fight alone. The process is easier when they ' \
          'have other women around to go through the insecurities as a sisterhood. '
myplot3 = 'Five stories following the lives of five women who are all diagnosed with breast cancer. This movie ' \
          'portrays what women go through when fighting breast cancer, from having to tell their family members to ' \
          'learn to deal with the life-changing news. '
myplot4 = 'This could be a typical, funny Christmas movie but it deals with deeper topics. In the middle of a chaotic ' \
          'dinner, the mother reveals her cancer diagnosis and makes everyone take a step back from petty grievances ' \
          'and consider the important things in life. '
myplot5 = 'Based on a true story, this film is about Annie Parker, the breast cancer survivor whose diagnosis helped ' \
          'doctors discover the BRCA-1 gene that shows that breast cancer can be hereditary in women. The movie ' \
          'centers around Annie Parker and her fight against the disease that took both her mother and sister. '


# Create the movies dictionary
movie1 = {
    'title': title1,
    'director': title1['director'][0],
    'cast1': title1['cast'][0],
    'cast2': title1['cast'][2],
    'cast3': title1['cast'][14],
    'genres': title1['genres'],
    'plot': title1['plot'][0],
    'myplot': myplot1,
    'cover': title1['full-size cover url']
}

movie2 = {
    'title': title2,
    'director': title2['director'][0],
    'cast1': title2['cast'][0],
    'cast2': title2['cast'][1],
    'genres': title2['genres'],
    'plot': title2['plot'][0],
    'myplot': myplot2,
    'cover': title2['full-size cover url']
}

movie3 = {
    'title': title3,
    'director1': title3['directors'][0],
    'director2': title3['directors'][1],
    'director3': title3['directors'][2],
    'director4': title3['directors'][3],
    'director5': title3['directors'][4],
    'cast1': title3['cast'][0],
    'cast2': title3['cast'][1],
    'cast3': title3['cast'][2],
    'cast4': title3['cast'][3],
    'cast5': title3['cast'][4],
    'genres': title3['genres'],
    'plot': title3['plot'][0],
    'myplot': myplot3,
    'cover': title3['full-size cover url']
}

movie4 = {
    'title': title4,
    'director': title4['director'][0],
    'cast1': title4['cast'][0],
    'cast2': title4['cast'][1],
    'cast3': title4['cast'][2],
    'cast4': title4['cast'][3],
    'cast5': title4['cast'][4],
    'cast6': title4['cast'][5],
    'cast7': title4['cast'][6],
    'genres': title4['genres'],
    'plot': title4['plot'][0],
    'myplot': myplot4,
    'cover': title4['full-size cover url']
}

movie5 = {
    'title': title5,
    'director': title5['director'][0],
    'cast1': title5['cast'][0],
    'cast2': title5['cast'][1],
    'genres': title5['genres'],
    'plot': title5['plot'][0],
    'myplot': myplot5,
    'cover': title5['full-size cover url']
}
