movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

a = [name.strip() for name in input().split(',')]

def score(movies, a):
    sum = 0
    c = 0
    
    for name in a:
        for movie in movies:
            if movie["name"] == name:
                sum += movie["imdb"]
                c+= 1
    
    if c > 0:
        average_score = sum / c
        print(average_score)
    else:
        print("wring movie")

score(movies, a)























'''
a_list=[name for name in input().split()]

def score(movies, a_list):
    sum=0
    for name in a_list:
        for movies in movies:
            if(movies["name"]==name):
                sum+=movies["imdb"]
    print(sum/len(a_list))

score(movies, a_list)
'''