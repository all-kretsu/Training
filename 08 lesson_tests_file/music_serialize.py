import pickle
import json

my_favourite_music = {
    'name': 'modern talking',
    'tracks': ['cherry lady', 'geronimo caddilac'],
    'albums': [{
        'name': 'lets talk about love',
        'year': '1985',
    }]

}

music_str = my_favourite_music

with open('favourite_band.pickle', 'wb') as g:
    pickle.dump(my_favourite_music, g)

with open('favourite_band.json', 'w', encoding= 'utf-8') as f:
    json.dump(my_favourite_music, f)


