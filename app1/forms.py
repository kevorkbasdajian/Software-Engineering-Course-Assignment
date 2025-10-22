from django.forms import ModelForm
from .models import Movie
from django import forms



class UpdateMovie(forms.Form):
	movie_id = forms.IntegerField()
class DeleteMovie(forms.Form):
	movie_id = forms.IntegerField()	
class CreateMovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ['ID', 'title', 'genre','year','rating','director','description']

class DisplayMovie(forms.Form):
	movie_id = forms.IntegerField()