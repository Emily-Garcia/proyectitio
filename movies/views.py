from django.shortcuts import render, redirect

# Create your views here.

from django import views

from .models import Movie

from django.http import HttpResponse

from .forms import MovieForm



#Hay dos formas de crear  vistas
# 1- Creando una clase -> Tenemos dos o mas metodos HTTP es la misma ruta
# 2- Creando una funcion -> Solo tenemos un metodo HTTP en la ruta

def GetMovies(request):
    #Vamos a traer todas las peliculas
    movies = Movie.objects.all() #Estamos haciendo el SELECT * FROM movies_movie,,, queryset
    template_name = 'movies/list.html'
    context = { 
        'movies': movies
    }
    return render(request, template_name, context)

def GetMovie(request, id):
    movie = Movie.objects.get(pk=id)
    template_name = 'movies/detail.html'
    context = {
        'movie': movie
    }
    return render(request, template_name, context)

class CreateMovie(views.View):
    def get(self, request):
        template_name ='movies/form.html'
        return render(request, template_name)

    def post(self, request):
        data = request.POST
        new_movie = Movie.objects.create(
            title = data['title'],
            sinopsis = data['sinopsis'],
            duration = data['duration'],
            calif = data['calif'],
            gender = data['gender']     
        )
        if new_movie:
            print('PELICULA CREADA CON EXITO')
            return redirect('/movies/')
        else:
            print('PELICULA NO SE PUDE CREAR')
            return redirect('/movies/create/')


class CreateMovieEasy(views.View):
    def get(self, request):
        form = MovieForm()
        template_name = 'movies/form_easy.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request):
        new_form = MovieForm(request.POST)
        if new_form.is_valid():
            new_movie = new_form.save()
            print('Se creó la película corerctamente', new_movie)
            return redirect('movies:list')
        else:
            template_name = 'movies/form_easy.html'
            context = {
                'form': new_form
            }
            return render(request, template_name, context)

class UpdateMovie(views.View):
    def get(self, request, id):
        movie = Movie.objects.get(pk=id)
        form = MovieForm(instance=movie)
        template_name = 'movies/form_easy.html'
        context = {
            'form': form,
            'id': id
        }
        return render(request, template_name, context)

    def post(self, request, id):
        movie = Movie.objects.get(pk=id)
        update_form = MovieForm(request.POST, instance=movie)
        if update_form.is_valid():
            form_updated = update_form.save()
            return redirect(f'/movies/{id}')
        else:
            template_name = 'movies/form_easy.html'
            context = {
                'form': form,
                'id': id
            }
            return render(request, template_name, context)

def DeleteMovie(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect(f'movies:list')