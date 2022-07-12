import django
from django.shortcuts import render
from django.http import HttpResponse
import pprint
import requests
import urllib.request
import pandas as pd

# posts = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# def home(request):
    
#     return render(request, 'movie/home.html')



# def result(request):
#     context ={
#         "post": posts
#     }
#     return render(request, 'movie/result.html', {'title': 'Result'})

def index(request):
    return render (request, "movie/index.html")

api_version = 3
api_key = "99558ae618ca3adc4cfcf6b988a999dd"
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"

poster_path ='https://image.tmdb.org/t/p/original/'

def search(request):
    search_query = request.GET.get('q')
    # print(search_query)

    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
    # print(endpoint)
    r = requests.get(endpoint)
        
    if r.status_code in range(200, 299):
        data = r.json()
        print(data)
            # results = data['results']
            # movie_list = []
            # movie_id_list = []
            # if len(results) > 0:
            #     # print(results[0].keys())
            #     for result in results:
            #         stuff ={
            #             "movie_id" : str(result['id']),
            #             "movie_title" : str(result['original_title']),
            #             "movie_release_date" : result['release_date'],
            #             "movie_overview" : str(result['overview']),
            #             "movie_voteavg" : str(result['vote_average']),
            #             "movie_poster" : str(("https://image.tmdb.org/t/p/original/"+ str(result['poster_path']))),
            #         }
            #         if result['id'] not in movie_id_list:
            #             movie_id_list.append(result['id'])
            #             movie_list.append(stuff)
            #         else:
            #             pass
                          
            #     print (movie_list)
            #     print (movie_id_list)
         
        return render(request,"movie/search.html", {"data": data})
    else:
        return render (request, "movie/index.html")


    