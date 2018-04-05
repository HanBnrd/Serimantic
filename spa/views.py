from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Default index
def index(request):
    return render(request, "index.html")

def tvShowInfos(request, tmdb_id):
	fichier = open('data/default.tal','r',encoding="utf8")
	APIkey = open('api.key','r',encoding="utf8")
	key = APIkey.readline().split("\n")[0]
	APIkey.close()
	url = "https://api.themoviedb.org/3/tv/"+tmdb_id+"?api_key="+key+"&language=en-US"
	return redirect(url)