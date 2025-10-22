from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CreateMovieForm,UpdateMovie,DeleteMovie,DisplayMovie
from .models import Movie


def index(request):
	return render(request,'index.html')

def add_movie(request):
	if request.method == 'POST':
		form = CreateMovieForm(request.POST, request.FILES)
		if form.is_valid():
			movieform = form.cleaned_data
			ID = movieform['ID']
			title = movieform['title']
			genre = movieform['genre']
			year = movieform['year']
			rating = movieform['rating']
			director = movieform['director']
			description = movieform['description']
			Movie.objects.create(ID=ID,title=title,genre=genre,year=year,rating=rating,director=director,description=description)
			return render(request, 'index.html')
	else:
		form = CreateMovieForm()
	return render(request, 'add_movie.html', {'form': form})

def update_movie(request):
	movie = None
	message = None
	if request.method == "POST":
		if "movie_id" in request.POST:
			movie_id = request.POST.get("movie_id")
			try:
				movie = Movie.objects.get(ID=movie_id)
				form = CreateMovieForm(instance=movie)
			except Movie.DoesNotExist:
				form = UpdateMovie()
				movie = None
				message = 'The movie with the provided ID does not exist !'

		else:
			movie_id = request.POST.get("ID")
			movie = get_object_or_404(Movie, ID=movie_id)
			form = CreateMovieForm(request.POST, request.FILES, instance=movie)
			if form.is_valid():
				form.save()
				return redirect("index")
	else:
		form = UpdateMovie()

	return render(request, "update_movie.html", {"form": form, "movie": movie,'message':message})

def display_movie(request):
	movie = None
	message = None
	if request.method =="POST":
		form = DisplayMovie(request.POST)
		if form.is_valid():
			Movieform=form.cleaned_data
			movie_id = request.POST.get("movie_id")
			try:
				movie = Movie.objects.get(ID = movie_id)
			except Movie.DoesNotExist:
				movie = None
				message = 'The movie with the provided ID does not exist !'
			return render(request,"Display_movie.html",{"form":form,"movie":movie,'message':message})

	else:
		form = DisplayMovie()
	return render(request, "Display_movie.html", {"form": form, "movie": movie,'message':message})

def delete_movie(request):
	movie = None
	message = None
	if request.method == "POST":
			form = DeleteMovie()
			movie_id = request.POST.get("movie_id")
			try:
				movie = Movie.objects.get(ID=movie_id)
			except Movie.DoesNotExist:
				movie = None
				message = 'The movie with the provided ID does not exist !'
			if(movie):
				movie.delete()
				return redirect("index")
			else:
				return render(request,"Delete.html",{"form":form, movie:"movie","message":message})
	else:
		form = DeleteMovie()
	return render(request,"Delete.html",{"form":form,'message':message})

def display_movies(request):
    movies = Movie.objects.all()
    return render(request, "display_movies.html", {"movies": movies})

