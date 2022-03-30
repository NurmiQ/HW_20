from unittest.mock import MagicMock
import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie_1 = Movie(id=1, title="Film1", description="description1",
                    trailer="trailer1", year=2010, rating=1,
                    genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="Film2", description="description2",
                    trailer="trailer2", year=2012, rating=2,
                    genre_id=2, director_id=2)

    objects = {1: movie_1, 2: movie_2}
    movie_dao.get_one = MagicMock(side_effect=objects.get)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=Movie(id=3, title="Film3", description="description3",
                                                    trailer="trailer3", year=2013, rating=3,
                                                    genre_id=3, director_id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None
        # assert movie.id != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "id": 3,
            "title": "Film3",
            "description": "description3",
            "trailer": "trailer3",
            "year": 2013, "rating": 3,
            "genre_id": 3, "director_id": 3}
        movie = self.movie_service.create(movie_d)
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 4,
            "title": "Film4",
            "description": "description4",
            "trailer": "trailer4",
            "year": 2014, "rating": 4,
            "genre_id": 4, "director_id": 4
        }
        self.movie_service.update(movie_d)
