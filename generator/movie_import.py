import requests
from bs4 import BeautifulSoup
import generator.models
from django.conf import settings

# def filmweb(apps, schema_editor, n=10):
def filmweb(n=10):
    # movie_model = apps.get_model('generator', 'Movie')
    Movie_model = generator.models.Movie

    host = 'https://www.filmweb.pl/'
    get_h = 'films/search?orderBy=popularity&descending=true&page='

    for page in range(1,n):

        query = get_h + str(page)

        response = requests.get(host + query)
        markup = response.text
        soup = BeautifulSoup(markup, 'html.parser')
        movies_list = soup.find_all('li', {'class': 'hits__item'})

        for movie in movies_list:
            title = movie.find('h3', {'class': 'filmPreview__title'}).text

            movie_attrs = movie.find('div').attrs
            movie_id = movie_attrs['data-id']
            try:
                release_world = movie_attrs['data-release-world-public']
            except:
                release_world = None

            try:
                release_country = movie_attrs['data-release-country-public']
            except:
                release_country = None


            if Movie_model.objects.filter(movie_id=movie_id).exists():
                next
            else:
                try:
                    directors = [director.find('a').text for director in
                             movie.find_all('div', {'class': 'filmPreview__info--directors'})]
                except:
                    directors = None

                try:
                    countries = [country.find('a').text for country in
                             movie.find_all('div', {'class': 'filmPreview__info--countries'})]
                except:
                    countries = None

                try:
                    genres = [genre.find('a').text for genre in
                          movie.find_all('div', {'class': 'filmPreview__info--genres'})]
                except:
                    genres = None

                try:
                    rating_attrs = movie.find('div', {'class': 'filmPreview__rateBox rateBox'}).attrs
                    rating_score = rating_attrs['data-rate']
                    rating_count = rating_attrs['data-count']
                except:
                    rating_score = None
                    rating_count = None

                try:
                    poster = movie.find('div', {'class': 'filmPreview__poster'})
                    poster_attrs = poster.find('img', {'class': 'filmPoster__image'}).attrs
                    poster_alt = poster_attrs['alt']
                    poster_url = poster_attrs['data-src']
                except:
                    poster_alt = None
                    poster_url = None

                try:
                    cover = movie_attrs['data-cover-photo']
                except:
                    cover = None

                new_movie = Movie_model(title=title, release_world=release_world, release_country=release_country,
                                                          directors=', '.join(directors), countries=', '.join(countries),
                                                          rating_score=rating_score, rating_count=rating_count,
                                                          genres=', '.join(genres), poster_alt=poster_alt, poster_url=poster_url,
                                                          cover=cover, movie_id=movie_id)
                new_movie.save()











