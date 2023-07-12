import json
# an array of propberly formed json objects
json_string = '''
[{ 
    "title": "Dangal", 
    "country": "India",
    "year": 2016, 
    "cast": {
        "Director": "Nitesh Tiwari", 
        "LeadActor": "Aamir Khan", 
        "BoxOfficeUSDMn": 330
    }, 
    "genres": ["Biograhpy", "Drama"], 
    "ratings": {"imdb": 8.4,"tomatoes": 4.55}
},
{
    "title": "Fight Club", 
    "country": "USA", 
    "year": 1999, 
    "cast": {
        "Director": "David Fincher", 
        "LeadActor": "Brad Pitt", 
        "BoxOfficeUSDMn": 104
    }, 
    "genres": ["Action", "Drama"], 
    "ratings": {"imdb": 8.8,"tomatoes": 4.46}
}]
'''
# json will deserialize a proberly json formed string
movies = json.loads(json_string)
# list
type(movies) 
# dict
type(movies[0])

# write the json to a file
# to write to a file like object  json.dump
file_for_writing_json = 'D:/tmp/moviesdump.json'
with open(file_for_writing_json, 'w') as f:
    json.dump(movies, f)

# to deseriallize to a python strng json.dumps
type(json.dumps(movies))
#  str

# to deserialize a file containing json objects
movies_fm_file = json.load(open(file_for_writing_json))
# list of json objects decoded to dicts
type(movies_fm_file)
# json is decoded as a dictionary
type(movies_fm_file[0])

# movies_mflix is a jsonl file
# one can use a generator expression and json.loads to load the file
mmfl = (open('D:/tmp/movies_mflix.json', encoding='utf8'))
for x in mmfl:
    print(json.loads(x))

# encoding custom types
def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
    
json.dumps(23 + 17j, default=encode_complex)

# The other common approach is to subclass the standard JSONEncoder and override its default() method:
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)
json.dumps(23 + 17j, cls=ComplexEncoder)

encoder = ComplexEncoder()
encoder.encode(3 + 6j)

complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
json.loads(complex_json)

import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
