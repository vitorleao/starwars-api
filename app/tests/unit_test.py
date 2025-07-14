import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_movies(mocker):
    mocker.patch(
        "app.services.swapi_client.SWAPIClient.get_movies",
        return_value=[{"title": "A New Hope", "release_date": "1977-05-25"}],
    )
    response = client.get("/api/movies")
    assert response.status_code == 200
    assert response.json()[0]["title"] == "A New Hope"


def test_get_characters(mocker):
    mocker.patch(
        "app.services.swapi_client.SWAPIClient.get_people",
        return_value=[{"name": "Luke Skywalker"}],
    )
    response = client.get("/api/characters")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Luke Skywalker"


def test_get_planets(mocker):
    mocker.patch(
        "app.services.swapi_client.SWAPIClient.get_planets",
        return_value=[{"name": "Tatooine"}],
    )
    response = client.get("/api/planets")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Tatooine"


def test_get_ships(mocker):
    mocker.patch(
        "app.services.swapi_client.SWAPIClient.get_starships",
        return_value=[{"name": "X-wing"}],
    )
    response = client.get("/api/ships")
    assert response.status_code == 200
    assert response.json()[0]["name"] == "X-wing"


def test_filter_movies(mocker):
    mocker.patch(
        "app.services.swapi_client.SWAPIClient.get_movies",
        return_value=[
            {"title": "A New Hope", "release_date": "1977-05-25"},
            {"title": "The Empire Strikes Back", "release_date": "1980-05-17"},
        ],
    )
    response = client.get("/api/filter/movies?year=1977&title=hope")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "A New Hope"


def test_sort_characters(mocker):
    mocker.patch(
        "app.services.swapi_client.SWAPIClient.get_people",
        return_value=[{"name": "Leia"}, {"name": "Luke"}, {"name": "Anakin"}],
    )
    response = client.get("/api/sort/characters?sort_by=name")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["name"] == "Anakin"
    assert data[1]["name"] == "Leia"
    assert data[2]["name"] == "Luke"
