from django.shortcuts import render, redirect
from .helpers import recommend_movies, movie_name

# Create your views here.
def home(request):
    return redirect('recommend_movie')

def recommend_movie(request):
    context = {'movie_name':movie_name}

    if request.method == 'POST':
        selected_movie_name = request.POST.get('movie')
        recommended_movies_name, recommended_movies_poster = recommend_movies(selected_movie_name)
        context['recommended_movies_name'] = recommended_movies_name
        context['recommended_movies_poster'] = recommended_movies_poster
        context['selected_movie'] = selected_movie_name

    return render(request, 'movierecommenderapp/movie_recommender.html', context=context)
