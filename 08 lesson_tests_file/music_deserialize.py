import pickle
import json

with open('favourite_band.pickle', 'rb') as g:
    music = pickle.load(g)
    print(music)

with open('favourite_band.json', 'r') as f:
    json_music = json.load(f)
    print(json_music)

