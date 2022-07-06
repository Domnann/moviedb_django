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

api_version = 3
api_key = "99558ae618ca3adc4cfcf6b988a999dd"
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/multi"


def index(request):
    if request.method == 'POST':
        searh_query = request.POST['search']
        endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}&language=en-US"
        # print(endpoint)
        r = requests.get(endpoint)
        # pprint.pprint(r.json())
        if r.status_code in range(200, 299):
            data = r.json()
            results = data['results']
            if len(results) > 0:
                print(results[0].keys())
                for result in results:
                    _id = result['id']
                    print(result['title'],"ID:", _id,"\nRelease Date:",result['release_date'],"\nOverview:" ,result['overview'],"\nVote Average:", result['vote_average'] ,"\n\n")
    return render(request, "movie/index.html")