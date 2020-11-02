import requests
from bs4 import BeautifulSoup
import generator.models

# w2s , count , popularity

def games_filmweb(n=10, orderby='popularity'):
    games_model = generator.models.Game

    host = 'https://www.filmweb.pl/'
    get_h = 'games/search?orderBy=' + orderby + '&descending=true&page='

    for page in range(1, n + 1):
        query = get_h + str(page)

        response = requests.get(host + query)
        markup = response.text
        soup = BeautifulSoup(markup, 'html.parser')
        games_list = soup.find_all('li', {'class': 'hits__item'})

        for games in games_list:
            try:
                title = games.find('h2', {'class': 'filmPreview__title'}).text
            except AttributeError as error:
                continue
            games_attrs = games.find('div', {'class': 'FilmPreview filmPreview filmPreview--VIDEOGAME Film'}).attrs
            game_id = games_attrs['data-id']

            try:
                release_world = games_attrs['data-release']
            except AttributeError as error:
                release_world = None
            except KeyError:
                release_world = None

            try:
                release_country = games_attrs['data-release']
            except AttributeError as error:
                release_country = None
            except KeyError:
                release_country = None

            if games_model.objects.filter(game_id=game_id).exists():
                continue
            else:

                try:
                    original_title = games.find('div', {'class': 'filmPreview__originalTitle'}).text
                except AttributeError as error:
                    original_title = None

                try:
                    url_attrs = games.find('a', {'class': 'filmPreview__link'}).attrs
                    url = host + url_attrs['href'][1:]
                except AttributeError as error:
                    url = None
                except KeyError:
                    url = None

                try:
                    developer_info = games.find('div', {'class': 'filmPreview__info filmPreview__info--developers'})
                    developer = developer_info.find('h3').text
                except AttributeError as error:
                    developer = None

                try:
                    countries = [country.find('a').text for country in
                                 games.find_all('div', {'class': 'filmPreview__info--countries'})]
                except AttributeError as error:
                    countries = None

                try:
                    genres = [genre.find('a').text for genre in
                              games.find_all('div', {'class': 'filmPreview__info--genres'})]
                except AttributeError as error:
                    genres = None

                try:
                    rating_attrs = games.find('div', {'class': 'filmPreview__rateBox rateBox'}).attrs
                    rating_score = rating_attrs['data-rate']
                    rating_count = rating_attrs['data-count']
                except AttributeError as error:
                    rating_score = None
                    rating_count = None
                except KeyError:
                    rating_score = None
                    rating_count = None

                try:
                    poster = games.find('div', {'class': 'filmPreview__poster'})
                    poster_attrs = poster.find('img', {'class': 'poster__image'}).attrs
                    poster_alt = poster_attrs['alt']
                    poster_url = poster_attrs['content']
                except AttributeError as error:
                    poster_alt = None
                    poster_url = None
                except KeyError:
                    poster_alt = None
                    poster_url = None

                try:
                    cover = games_attrs['data-cover-photo']
                except AttributeError as error:
                    cover = None
                except KeyError:
                    cover = None

                new_games = games_model(title=title, original_title=original_title, release_world=release_world,
                                          release_country=release_country,
                                          developer=developer, countries=', '.join(countries),
                                          rating_score=rating_score, rating_count=rating_count,
                                          genres=', '.join(genres), poster_alt=poster_alt, poster_url=poster_url,
                                          cover=cover, url=url, game_id=game_id)
                new_games.save()

def series_filmweb(n=10, orderby='popularity'):
    Series_model = generator.models.Series

    host = 'https://www.filmweb.pl/'
    get_h = 'serials/search?orderBy=' + orderby + '&descending=true&page='

    for page in range(1, n + 1):
        query = get_h + str(page)

        response = requests.get(host + query)
        markup = response.text
        soup = BeautifulSoup(markup, 'html.parser')
        series_list = soup.find_all('li', {'class': 'hits__item'})

        for series in series_list:
            try:
                title = series.find('h2', {'class': 'filmPreview__title'}).text
            except AttributeError as error:
                continue
            series_attrs = series.find('div', {'class': 'FilmPreview filmPreview filmPreview--SERIAL Film'}).attrs
            series_id = series_attrs['data-id']

            try:
                release_world = series_attrs['data-release']
            except AttributeError as error:
                release_world = None
            except KeyError:
                release_world = None

            try:
                release_country = series_attrs['data-release']
            except AttributeError as error:
                release_country = None
            except KeyError:
                release_country = None

            if Series_model.objects.filter(series_id=series_id).exists():
                continue
            else:

                try:
                    original_title = series.find('div', {'class': 'filmPreview__originalTitle'}).text
                except AttributeError as error:
                    original_title = None

                try:
                    url_attrs = series.find('a', {'class': 'filmPreview__link'}).attrs
                    url = host + url_attrs['href'][1:]
                except AttributeError as error:
                    url = None
                except KeyError:
                    url = None

                try:
                    directors = [director.find('a').text for director in
                                 series.find_all('div', {'class': 'filmPreview__info--directors'})]
                except AttributeError as error:
                    directors = None

                try:
                    countries = [country.find('a').text for country in
                                 series.find_all('div', {'class': 'filmPreview__info--countries'})]
                except AttributeError as error:
                    countries = None

                try:
                    genres = [genre.find('a').text for genre in
                              series.find_all('div', {'class': 'filmPreview__info--genres'})]
                except AttributeError as error:
                    genres = None

                try:
                    rating_attrs = series.find('div', {'class': 'filmPreview__rateBox rateBox'}).attrs
                    rating_score = rating_attrs['data-rate']
                    rating_count = rating_attrs['data-count']
                except AttributeError as error:
                    rating_score = None
                    rating_count = None
                except KeyError:
                    rating_score = None
                    rating_count = None

                try:
                    poster = series.find('div', {'class': 'filmPreview__poster'})
                    poster_attrs = poster.find('img', {'class': 'poster__image'}).attrs
                    poster_alt = poster_attrs['alt']
                    poster_url = poster_attrs['content']
                except AttributeError as error:
                    poster_alt = None
                    poster_url = None
                except KeyError:
                    poster_alt = None
                    poster_url = None

                try:
                    cover = series_attrs['data-cover-photo']
                except AttributeError as error:
                    cover = None
                except KeyError:
                    cover = None

                new_series = Series_model(title=title, original_title=original_title, release_world=release_world,
                                          release_country=release_country,
                                          directors=', '.join(directors), countries=', '.join(countries),
                                          rating_score=rating_score, rating_count=rating_count,
                                          genres=', '.join(genres), poster_alt=poster_alt, poster_url=poster_url,
                                          cover=cover, url=url, series_id=series_id)
                new_series.save()

def movie_filmweb(n=10, orderby='popularity'):
    Movie_model = generator.models.Movie

    host = 'https://www.filmweb.pl/'
    get_h = 'films/search?orderBy=' + orderby + '&descending=true&page='

    for page in range(1, n + 1):
        query = get_h + str(page)

        response = requests.get(host + query)
        markup = response.text
        soup = BeautifulSoup(markup, 'html.parser')
        movies_list = soup.find_all('li', {'class': 'hits__item'})

        for movie in movies_list:
            try:
                title = movie.find('h2', {'class': 'filmPreview__title'}).text
            except AttributeError as error:
                continue
            movie_attrs = movie.find('div', {'class': 'FilmPreview filmPreview filmPreview--FILM Film'}).attrs
            movie_id = movie_attrs['data-id']

            try:
                release_world = movie_attrs['data-release-world-public']
            except AttributeError as error:
                release_world = None
            except KeyError:
                release_world = None

            try:
                release_country = movie_attrs['data-release-country-public']
            except AttributeError as error:
                release_country = None
            except KeyError:
                release_country = None

            if Movie_model.objects.filter(movie_id=movie_id).exists():
                continue
            else:

                try:
                    original_title = movie.find('div', {'class': 'filmPreview__originalTitle'}).text
                except AttributeError as error:
                    original_title = None

                try:
                    url_attrs = movie.find('a', {'class': 'filmPreview__link'}).attrs
                    url = host + url_attrs['href'][1:]
                except AttributeError as error:
                    url = None
                except KeyError:
                    url = None

                try:
                    directors = [director.find('a').text for director in
                                 movie.find_all('div', {'class': 'filmPreview__info--directors'})]
                except AttributeError as error:
                    directors = None

                try:
                    countries = [country.find('a').text for country in
                                 movie.find_all('div', {'class': 'filmPreview__info--countries'})]
                except AttributeError as error:
                    countries = None

                try:
                    genres = [genre.find('a').text for genre in
                              movie.find_all('div', {'class': 'filmPreview__info--genres'})]
                except AttributeError as error:
                    genres = None

                try:
                    rating_attrs = movie.find('div', {'class': 'filmPreview__rateBox rateBox'}).attrs
                    rating_score = rating_attrs['data-rate']
                    rating_count = rating_attrs['data-count']
                except AttributeError as error:
                    rating_score = None
                    rating_count = None
                except KeyError:
                    rating_score = None
                    rating_count = None

                try:
                    poster = movie.find('div', {'class': 'filmPreview__poster'})
                    poster_attrs = poster.find('img', {'class': 'poster__image'}).attrs
                    poster_alt = poster_attrs['alt']
                    poster_url = poster_attrs['content']
                except AttributeError as error:
                    poster_alt = None
                    poster_url = None
                except KeyError:
                    poster_alt = None
                    poster_url = None

                try:
                    cover = movie_attrs['data-cover-photo']
                except AttributeError as error:
                    cover = None
                except KeyError:
                    cover = None

                new_movie = Movie_model(title=title, original_title=original_title, release_world=release_world,
                                        release_country=release_country,
                                        directors=', '.join(directors), countries=', '.join(countries),
                                        rating_score=rating_score, rating_count=rating_count,
                                        genres=', '.join(genres), poster_alt=poster_alt, poster_url=poster_url,
                                        cover=cover, url=url, movie_id=movie_id)
                new_movie.save()
