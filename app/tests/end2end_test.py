import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_end_to_end_movies(mocker):
    mocker.patch(
        "app.services.swapi_client.SWAPIClient.get_movies",
        return_value=[{"title": "A New Hope", "release_date": "1977-05-25"}],
    )
    response = client.get("/movies")
    assert response.status_code == 200
    assert response.json()[0]["title"] == "A New Hope"
